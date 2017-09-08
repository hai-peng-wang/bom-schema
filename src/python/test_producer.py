import sys
import functools
import calendar
from datetime import datetime

try:
    import urlparse
except: # For Python 3
    import urllib.parse as urlparse

# Protobuf messages
from producer_pb2 import Producer
from task_pb2 import TaskEvent
# Protobuf enums
from realm_pb2 import Realm
from prod_status_pb2 import ProdStatus
from impact_pb2 import Impact
from debug_level_pb2 import DebugLevel
from task_state_pb2 import TaskState
from component_level_pb2 import ComponentLevel
from component_relation_pb2 import ComponentRelation
from error_type_pb2 import ErrorType
from severity_pb2 import Severity
from task_actor_type_pb2 import TaskActorType

def uri_to_schema(uri):
    loc = urlparse.urlparse(uri)
    return {
      'scheme' : loc.scheme,
      'username' : loc.username,
      'password' : loc.password,
      'address' : {'hostname' : loc.hostname, 'port' : loc.port},
      'queries' : [dict(zip(['key','value'], x.split('='))) for x in
          loc.query.split('&')],
      'fragment' : loc.fragment
    }

def rgetattr(obj, attr):
# Recursive get attribut
    return functools.reduce(getattr, [obj]+attr.split('.'))

def proto_setattr(obj, **kwargs):
# Set protobuf message attributes using a mappable structure.
# keys should be strings representing message attributes.
# values can be primitive values, a dictionary representing a message,
# lists of primitive values, lists of dictionaries representing messages,
# or protocol buffer messages themselves.
    for attr,val in kwargs.items():
        pre, _, post = attr.rpartition('.')
        if isinstance(val, list):
            for v in val:
                o = getattr(rgetattr(obj, pre) if pre else obj, post)
                if isinstance(v, dict):
                    proto_setattr(o.add(), **v)
                elif hasattr(v, 'MergeFrom'):
                    o.MergeFrom(v)
                elif v is not None:
                    o.append(v)
        elif isinstance(val, dict):
            proto_setattr(getattr(rgetattr(obj, pre) if pre else obj, post), **val)
        elif hasattr(val, 'MergeFrom'):
            o = getattr(rgetattr(obj, pre) if pre else obj, post)
            o.MergeFrom(val)
        elif val is not None:
            setattr(rgetattr(obj, pre) if pre else obj, post, val)

# CREATING EVENT MESSAGE SAMPLE TEST CODE
# --------- PART 1 ----------
# Generally a "Producer" message will remain constant over the life-time of
# an event producing application. This can be created now, cached and used
# later when events need to be produced:
producer = Producer()

cylc_component = {
  'info' : {
    'level' : ComponentLevel.Value("PLATFORM"),
    'name' : 'Cylc',
    'version.semver' : {'major' : 2, 'minor' : 3, 'patch' : 1},
    'type' : "Workflow Scheduler"
  },
  'relation_id' : 1,
  'tags' : [
    {'key' : "audit_status", 'value' : 'passed'},
    {'key' : 'capability_level', 'value' : 'awesome'}
  ]
}

# Suite is a sub-component of cylc
suite_component = {
  'info' : {
    'level' : ComponentLevel.Value('SUITE'),
    'name' : 'ACCESS-GE3',
    'production_status.status' : ProdStatus.Value('STAGING'),
    'version.semver' : {'major' : 3, 'minor' : 0, 'patch' : 1},
    'type' : 'Model',
    'description' : 'Ensemble Global NWP Model Suite',
    'uri' : uri_to_schema('http://example.au:80/reg/search?model=ACCESS#info')
  },
  'host' : {
    'realm' : Realm.Value("STAGE"),
    'type' : "VM",
    'physical_desc' : "VM@SDC",
    'address.hostname' : "scs-cylc-stage",
    'architecture' : "x86_64",
    'os' : "RHEL 7",
    'os_version.semver' : {'major' : 4, 'minor' : 11, 'patch' : 12,
      'build_ids' : ["200", "rhel7", "x86_64"]}
  },
  'relation_id' : 2,
  'relationships' : [
    {
    'id' : 1,
    'relationship' : ComponentRelation.Value("SUBCOMPONENT"),
    'relation_description' : 'This suite is composed of modelling tasks' +
      'designed to run under the Cylc workflow scheduler'
    },
    {
    'id' : 3,
    'relationship' : ComponentRelation.Value("INSTRUCTOR"),
    'relation_description' : 'This suite submits task jobs' +
      'dispatched via a PBS batch scheduler.'
    }
  ]
}

pbs_component = {
  'info' : {
    'level' : ComponentLevel.Value("SERVICE"),
    'name' : 'PBS',
    'type' : "Batch Scheduler"
  },
  'host' : {
    'address.hostname' : "scs-master-pbs",
  },
  'relation_id' : 3
}

proto_setattr(producer, **{
  'components' : [cylc_component, suite_component, pbs_component],
  'producer_component_id' : 2
})

# --------- PART 2 ----------
# Lets generate an event representing a change in state of a task, as managed
# by a hypothetical Cylc suite
# Construction of any subpart can of course be incremental and broken-up
# as desired

task_event = TaskEvent()

proto_setattr(task_event, **{
  'header.producer' : producer,
  'header.sequence_number' : 1,
  'event_type' : 'STATE_CHANGE',
  'task_info' : {
    'name' : 'fractalCloudCalc',
    'namespace' : 'ensemble05/cloud_micro',
    'suite' : 'ACCESS-GE3',
    'is_idempotent' : True,
    'project' : 'pr_G3',
    'production_status.status' : ProdStatus.Value('STAGING'),
    'priority.impact' : Impact.Value('MODERATE'),
    'priority.urgency' : Impact.Value('LOW'),
    'task_debug' : uri_to_schema('http://bom/help/G3/cloudfun')
  },
  'task_context' : {
    'id.workflow_id.id_str' : 'myworkflow_id123',
    'id.batch_id.id_uint' : 123456789,
    'retry' : {
      'submit_number' : 2,
      'try_number' : 2,
      'retry_limit' : 1
    },
    'settings' : {
      'user.name' : 'ACCESS_stage',
      'is_edit_run' : True,
      'note' : 'Edited fractal similarity parameter to 3.14159 just "because"',
      'debug.debug_level' : DebugLevel.Value('NORMAL')
    },
    'exec_vnodes' : [{'hostname' : 'compute_node_23'}]
  },
  'task_manager_context.name' : 'PBS',
  'task_manager_context.component_id' : 3,
  'task_status' : {
    'state' : TaskState.Value('KILLED_BY_MEMORY_LIMIT'),
    'diagnostics' : [
      {
        'type' : ErrorType.Value('RESOURCE_EXHAUSTED'),
        'severity' : Severity.Value('ERROR'),
        'return_status' : -27,
        'signal' : 'SIGUSR2',
        'timestamp.seconds' : calendar.timegm(datetime.utcnow().timetuple()),
        'model_diagnostic.iteration' : 54 # as signaled to cylc via task
                                          #(somehow!?) before task was killed
      }
    ],
    'reporter_type' : TaskActorType.Value('WORKFLOW_SCHEDULER'),
    'severity' : Severity.Value('ERROR'),
    'time_info.series_created_timestamp.seconds' : 1504840001,
    'time_info.instance_end_timestamp.seconds' : 1504840399,
    'number_of_consecutive_failures': 2
  }
})

# Print out a text representation of the event for fun
print(task_event)

# Note: task_events can be kept and updated  by either setting properties
# directly or merging or replacing sub-messages with updated versions

# Seralize the event message to disk
f = open("python_TaskEvent_sample", "wb")
f.write(task_event.SerializeToString())
f.close()
