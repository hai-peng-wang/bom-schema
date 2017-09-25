# Protocol Documentation
<a name="top"/>

## Table of Contents
* [dataset.proto](#dataset.proto)
 * [Coverage](#bom.Coverage)
 * [DataFile](#bom.DataFile)
 * [DataTimeInfo](#bom.DataTimeInfo)
 * [Dataset](#bom.Dataset)
 * [DatasetAction](#bom.DatasetAction)
 * [DatasetSource](#bom.DatasetSource)
 * [Dimension](#bom.Dimension)
 * [License](#bom.License)
 * [NWPDataSetForSingleBaseTime](#bom.NWPDataSetForSingleBaseTime)
 * [Rights](#bom.Rights)
 * [SpatialCoverage](#bom.SpatialCoverage)
 * [TemporalCoverage](#bom.TemporalCoverage)
 * [Variable](#bom.Variable)
* [task.proto](#task.proto)
 * [TaskContext](#bom.TaskContext)
 * [TaskEvent](#bom.TaskEvent)
 * [TaskGroupLimits](#bom.TaskGroupLimits)
 * [TaskInfo](#bom.TaskInfo)
 * [TaskInteraction](#bom.TaskInteraction)
 * [TaskManagerContext](#bom.TaskManagerContext)
 * [TaskQueue](#bom.TaskQueue)
 * [TaskResource](#bom.TaskResource)
 * [TaskRetry](#bom.TaskRetry)
 * [TaskSettings](#bom.TaskSettings)
 * [TaskStatus](#bom.TaskStatus)
 * [TaskTimes](#bom.TaskTimes)
 * [Taskid](#bom.Taskid)
* [actor.proto](#actor.proto)
 * [Actor](#bom.Actor)
* [address.proto](#address.proto)
 * [Address](#bom.Address)
 * [URI](#bom.URI)
* [component.proto](#component.proto)
 * [ClusterInfo](#bom.ClusterInfo)
 * [Component](#bom.Component)
 * [Component.Info](#bom.Component.Info)
 * [Component.Relation](#bom.Component.Relation)
 * [Device](#bom.Device)
 * [ProductionStatus](#bom.ProductionStatus)
* [contact.proto](#contact.proto)
 * [Contact](#bom.Contact)
* [debug_settings.proto](#debug_settings.proto)
 * [DebugSettings](#bom.DebugSettings)
* [diagnostic.proto](#diagnostic.proto)
 * [Diagnostic](#bom.Diagnostic)
 * [ModelDiagnostic](#bom.ModelDiagnostic)
* [ensemble_member.proto](#ensemble_member.proto)
 * [EnsembleMember](#bom.EnsembleMember)
* [event_header.proto](#event_header.proto)
 * [EventHeader](#bom.EventHeader)
* [log_info.proto](#log_info.proto)
 * [LogInfo](#bom.LogInfo)
* [priority.proto](#priority.proto)
 * [Priority](#bom.Priority)
* [producer.proto](#producer.proto)
 * [Producer](#bom.Producer)
* [security_marking.proto](#security_marking.proto)
 * [SecurityMarking](#bom.SecurityMarking)
* [tag.proto](#tag.proto)
 * [Id](#bom.Id)
 * [Tag](#bom.Tag)
* [time.proto](#time.proto)
 * [TimePointOrRange](#bom.TimePointOrRange)
 * [TimeRange](#bom.TimeRange)
* [userid.proto](#userid.proto)
 * [Userid](#bom.Userid)
* [version.proto](#version.proto)
 * [SemVer](#bom.SemVer)
 * [Version](#bom.Version)
* [component_level.proto](#component_level.proto)
 * [ComponentLevel](#bom.component_level.ComponentLevel)
* [component_relation.proto](#component_relation.proto)
 * [ComponentRelation](#bom.component_relation.ComponentRelation)
* [computing_resource.proto](#computing_resource.proto)
 * [ComputingResource](#bom.computing_resource.ComputingResource)
* [computing_resource_scope.proto](#computing_resource_scope.proto)
 * [ComputingResourceScope](#bom.computing_resource_scope.ComputingResourceScope)
* [data_coverage_content_type.proto](#data_coverage_content_type.proto)
 * [DataCoverageContentType](#bom.data_coverage_content_type.DataCoverageContentType)
* [dataset_action_type.proto](#dataset_action_type.proto)
 * [DatasetActionType](#bom.dataset_action_type.DatasetActionType)
* [dataset_compression_type.proto](#dataset_compression_type.proto)
 * [DatasetCompressionType](#bom.dataset_compression_type.DatasetCompressionType)
* [dataset_feature_type.proto](#dataset_feature_type.proto)
 * [DatasetFeatureType](#bom.dataset_feature_type.DatasetFeatureType)
* [dataset_production_context.proto](#dataset_production_context.proto)
 * [DatasetProductionContext](#bom.dataset_production_context.DatasetProductionContext)
* [data_time_type.proto](#data_time_type.proto)
 * [DataTimeType](#bom.data_time_type.DataTimeType)
* [debug_level.proto](#debug_level.proto)
 * [DebugLevel](#bom.debug_level.DebugLevel)
* [error_type.proto](#error_type.proto)
 * [ErrorType](#bom.error_type.ErrorType)
* [impact.proto](#impact.proto)
 * [Impact](#bom.impact.Impact)
* [job_array_type.proto](#job_array_type.proto)
 * [JobArrayType](#bom.job_array_type.JobArrayType)
* [log_type.proto](#log_type.proto)
 * [LogType](#bom.log_type.LogType)
* [maturity.proto](#maturity.proto)
 * [Maturity](#bom.maturity.Maturity)
* [prod_status.proto](#prod_status.proto)
 * [ProdStatus](#bom.prod_status.ProdStatus)
* [realm.proto](#realm.proto)
 * [Realm](#bom.realm.Realm)
* [security_classification.proto](#security_classification.proto)
 * [SecurityClassification](#bom.security_classification.SecurityClassification)
* [security_delimiting_marker.proto](#security_delimiting_marker.proto)
 * [SecurityDelimitingMarker](#bom.security_delimiting_marker.SecurityDelimitingMarker)
* [severity.proto](#severity.proto)
 * [Severity](#bom.severity.Severity)
* [system_actor_type.proto](#system_actor_type.proto)
 * [SystemActorType](#bom.system_actor_type.SystemActorType)
* [task_communication_method.proto](#task_communication_method.proto)
 * [TaskCommunicationMethod](#bom.task_communication_method.TaskCommunicationMethod)
* [task_interaction_type.proto](#task_interaction_type.proto)
 * [TaskInteractionType](#bom.task_interaction_type.TaskInteractionType)
* [task_property.proto](#task_property.proto)
 * [TaskProperty](#bom.task_property.TaskProperty)
* [task_state.proto](#task_state.proto)
 * [TaskState](#bom.task_state.TaskState)
* [trace_level.proto](#trace_level.proto)
 * [TraceLevel](#bom.trace_level.TraceLevel)
* [Scalar Value Types](#scalar-value-types)

<a name="dataset.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dataset.proto



<a name="bom.Coverage"/>
### Coverage


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| subject_categories | [string](#string) | repeated | Subject categories covered by the dataset |
| temporal | [TemporalCoverage](#bom.TemporalCoverage) | optional |  |
| spatial | [SpatialCoverage](#bom.SpatialCoverage) | optional |  |


<a name="bom.DataFile"/>
### DataFile
Location and other metadata of a data file

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| data_uris | [URI](#bom.URI) | repeated | Where data can be found. Multiple URLs must lead to mirrored locationsof the same data file or set of data files |
| meta_uri | [URI](#bom.URI) | optional | Where additional metadata about the data can be found. |
| data_format | [string](#string) | optional | Format of data |
| digest | [Id](#bom.Id) | optional | Message digest/checksums/fingerprints of file |
| data_size | [int64](#int64) | optional | Size of data uris in bytes. |
| compressions | [DatasetCompressionType](#bom.dataset_compression_type.DatasetCompressionType) | repeated | Compression techniques applied.Multiple types can be specified; for example THINNED, PACKED and LOSSLESSare to be interpreted as data that has been thinned (a lossy operation)then packed (another lossy operation) and then this resultingthinned and packed data is further losslessly compressed |


<a name="bom.DataTimeInfo"/>
### DataTimeInfo
Temporal information pertaining to a subset of data in a dataset.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_model_time | [bool](#bool) | optional | True if datetime(s) represented are valid in in a model/simulatedtime space/coordinate or some relative notion of time.False implies real UTC clocktime. |
| time_type | [DataTimeType](#bom.data_time_type.DataTimeType) | optional |  |
| values | [TimePointOrRange](#bom.TimePointOrRange) | repeated |  |
| uncertainty | [Duration](#google.protobuf.Duration) | optional |  |


<a name="bom.Dataset"/>
### Dataset
Basic information about a Dataset.
A dataset comprises of data related in some way,
for example from a single instrument or collocated instruments,
or from a particular field campaign.
The Dataset message is a "base" message; most real datasets will include
this message as the "base_dataset" and add domain specific information
pertinent to the type of data being represented

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title | [string](#string) | optional | A succinct description of the dataset. |
| description | [string](#string) | optional | A longer description of what is in the dataset. |
| id | [Id](#bom.Id) | optional | An identifier for the dataset, if applicable |
| version | [Version](#bom.Version) | optional | The version of the dataset |
| source | [DatasetSource](#bom.DatasetSource) | optional | Information about the source of the data |
| coverage | [Coverage](#bom.Coverage) | optional | Overview of temporal, spatial and subject-matter coverage |
| feature_type | [DatasetFeatureType](#bom.dataset_feature_type.DatasetFeatureType) | optional | The global dataset feature type (if applicable, and if all of thedata variables contained in this dataset are of a single feature type.If this is not the case, dataset_feature_type can be set to MIXED andper-variable feature types specified). |
| production_context | [DatasetProductionContext](#bom.dataset_production_context.DatasetProductionContext) | optional | Dataset context information that may be critical to interpreting thedata, e.g. if the dataset is sample data or "live" operational data. |
| data_maturity | [Maturity](#bom.maturity.Maturity) | optional | Operational status of the system producing the dataset |
| data_files | [DataFile](#bom.DataFile) | repeated | URLs to where data can be found and data file metadata |
| contacts | [Contact](#bom.Contact) | repeated | Relevant contacts for further information or to report dataset issues |


<a name="bom.DatasetAction"/>
### DatasetAction
Description of some action that has taken place or
planned to take place concerning the dataset document
e.g. description of a modification, outcome of a validation,
approval process etc.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type_enum | [DatasetActionType](#bom.dataset_action_type.DatasetActionType) | optional | The type of action, e.g. CREATE for dataset creation |
| type_str | [string](#string) | optional | Can be used instead of action_type_enum to refer to moreesoteric actions, e.g. revision to the date a dataset/documentis planned to be adopted or a change to the intellectualproperty rights around a dataset |
| state | [TaskState](#bom.task_state.TaskState) | optional | If action has taken place and resulted in a successful or failedoutcome, or if the action is in-progress or is scheduled to happen.TaskState is used here as it offers a large range ofuseful action and action resolution states, although many willlikely not be applicable |
| times | [TimePointOrRange](#bom.TimePointOrRange) | repeated | The time the action reached action_state, or the timethe action is due to commence if it is a scheduled action.If a range is specified it represents the action begin and end timesof the action |
| time_uncertainty | [Duration](#google.protobuf.Duration) | optional |  |
| authority | [Actor](#bom.Actor) | optional | Who is the key contact/user associated with authorising ororganising the action/change |
| actor | [Actor](#bom.Actor) | optional | Who was responsible for carrying out the change, if different from theauthorising entity |
| reason | [string](#string) | optional | Why the action/change took place or is due to take place |
| outcome_details | [string](#string) | optional | Details about the action outcome, if relevant. e.g. if action typeand state indicate a review that failed, the outcome string canprovide an explanation for this outcome |
| comment | [string](#string) | optional | Any additional pertinent comments, e.g. where the action happened |


<a name="bom.DatasetSource"/>
### DatasetSource
Overview of the source of the original data, i.e. the system or processes
that generated this dataset
The source is the method of production of the data. For example, if the
data was model-generated, the details of the "source" component would
represent details at the relevant level of the boarder numerical model
system; if the data is observational, source would characterise the
observation platform.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| component | [Component](#bom.Component) | optional | A Component message describing the source |
| producer_source_component_id | [int64](#int64) | optional | Alternatively, the source component can be identified via referenceto the relevant component in the Producer message (if thesource component is listed in the Producer message) |
| config_id | [int64](#int64) | optional | ID to help track potentially unusual source configurations.config_id = 0 implies a normal configuration, other statesmap to a lookup table of configurable possibilities. This is sourcespecific and must be documented by the source system. |
| institution | [string](#string) | optional | Name of the organisation or institute that produced the dataset |


<a name="bom.Dimension"/>
### Dimension
Dimension used for variable array dimensional coordinates.
The dimensional coordinates of a data variable map from variable
index space (specified by a set of index dimensions) to coordinate space.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional |  |
| length | [uint64](#uint64) | optional |  |


<a name="bom.License"/>
### License
License under which a dataset is intended to be published, or the
license conditions for data obtainable from a service or repository via
an API.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | license name |
| url | [URI](#bom.URI) | optional | A URL to the license used |


<a name="bom.NWPDataSetForSingleBaseTime"/>
### NWPDataSetForSingleBaseTime


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| base_dataset | [Dataset](#bom.Dataset) | optional |  |
| run_start_clock_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | The datetime at which the source began generation of the dataset.This would represent the real clocktime a model simulation began in thecase of model data; in this case this timestamp can be used to distinguishbetween model re-runs. |
| number_of_ensemble_members | [int64](#int64) | optional | Total number of ensemble members run, if known. This includes membersthat may not be present in this dataset. 0 implies unknownif set to 1 implies a deterministic model. |
| ensemble_members | [EnsembleMember](#bom.EnsembleMember) | repeated | Optional information about each ensemble_member |
| observational_cutoff | [Duration](#google.protobuf.Duration) | optional | For models involving data assimilation, the observationaldata cut-off duration relative to the model (nominal) analysis time |
| dimensions | [Dimension](#bom.Dimension) | repeated |  |
| variables | [Variable](#bom.Variable) | repeated |  |


<a name="bom.Rights"/>
### Rights
IP or security rights for a resource

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| security_marking | [SecurityMarking](#bom.SecurityMarking) | optional |  |
| license | [License](#bom.License) | optional | License under which the dataset is intended to be published |


<a name="bom.SpatialCoverage"/>
### SpatialCoverage




<a name="bom.TemporalCoverage"/>
### TemporalCoverage


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| creation_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Approximate time dataset was originally created |
| reference_timestamp | [DataTimeInfo](#bom.DataTimeInfo) | optional | Reference datetime of the dataset. For example, the nominal("base") datetime for a NWP model run or the validity time ofan observational dataset or the start of a sequence of reanalyses etc |
| data_times | [DataTimeInfo](#bom.DataTimeInfo) | repeated | Summary-level temporal coverage information for the dataset, .eg.the range of times the dataset covers, or the discrete times data inin the dataset is valid for |


<a name="bom.Variable"/>
### Variable
A data, coordinate or auxiliary coordinate variable, as per CF
conventions.
A data variable is a multidimensional array of values that is the
result of sampling a continuous function at a discrete set of points.
In the case of observations the function represents the physical
system being observed.
A coordinate variable a one-dimensional variable with the same name
as its dimension [e.g., time(time) ], and it is defined as a numeric
data type with values that are ordered monotonically.
An auxiliary coordinate is a variable that contains coordinate
data, but unlike coordinate variables, there is no relationship between
the name of an auxiliary coordinate variable and the name(s) of
its dimension(s).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | From a controlled vocabulary |
| cf_standard_name | [string](#string) | optional | From CF conventions, if applicable |
| units | [string](#string) | optional | Units of the variable |
| dimensions | [string](#string) | repeated | List of dimensions that define the multidimensional array shape.Zero dimensions implies a scalar variable or coordinate (a "singleton") |
| aux_coordinates | [string](#string) | repeated | List of auxiliary coordinates |
| feature_type | [DatasetFeatureType](#bom.dataset_feature_type.DatasetFeatureType) | optional | Variable feature_type, if applicable. Should be set if global datasetconsists of a MIXED feature type |
| coverage_content_type | [DataCoverageContentType](#bom.data_coverage_content_type.DataCoverageContentType) | optional | additional qualifying information about the sourceof the variable's data to aid with interpretation |
| attributes | [Tag](#bom.Tag) | repeated | Other attributes, following CF conventions where relevant |






<a name="task.proto"/>
<p align="right"><a href="#top">Top</a></p>

## task.proto



<a name="bom.TaskContext"/>
### TaskContext
Summary context information pertaining to this task instance

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [Taskid](#bom.Taskid) | optional |  |
| settings | [TaskSettings](#bom.TaskSettings) | optional |  |
| cycle_point | [string](#string) | optional | Top-level cycle point information |
| retry | [TaskRetry](#bom.TaskRetry) | optional | Information about task retries |
| logs | [LogInfo](#bom.LogInfo) | repeated | Logs generated by or on behalf of this task |
| session | [URI](#bom.URI) | optional | A link to this task instance's run information/top-level debugoutputs etc (if such a location exists) |
| queue | [TaskQueue](#bom.TaskQueue) | optional | The queue to which the task belongs |
| submission_method | [string](#string) | optional |  |
| comms_method | [TaskCommunicationMethod](#bom.task_communication_method.TaskCommunicationMethod) | optional |  |
| priority | [Priority](#bom.Priority) | optional | Priority of task, as viewed by this scheduler. Priority may changedynamically based on the evolution of activities and business requirementsduring scheduling |
| group_limits | [TaskGroupLimits](#bom.TaskGroupLimits) | repeated | Limits placed on the running of this task (usually as part of a strategyto prevent saturating a particular resource) |
| resource_limits | [TaskResource](#bom.TaskResource) | repeated | Resource limits requested of and/or imposed/enforced by this manager |
| resource_use | [TaskResource](#bom.TaskResource) | repeated | Resources used by the task |
| managers | [TaskManagerContext](#bom.TaskManagerContext) | repeated | Task manager(s) associated with this task. The first managerlisted should correspond to, or be closely aligned with, the componentthat produced this message |
| exec_hosts | [Address](#bom.Address) | repeated | List of execution hosts for task |
| exec_vnodes | [Address](#bom.Address) | repeated | List of execution vnodes for task |


<a name="bom.TaskEvent"/>
### TaskEvent
A task event represents a change in state of a task, and/or an interaction
with a task by a user or system.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [EventHeader](#bom.EventHeader) | optional |  |
| event_type | [string](#string) | optional | Very brief elaboration on what type of task event this is.These would be most common:STATE_CHANGE, INTERACTION, STATE_CHANGE_WITH_AUTOMATIC_INTERACTION,Some more esoteric possibilities include:RESOURCE_LIMIT_CHANGE, PRIORITY_CHANGE etc |
| task_info | [TaskInfo](#bom.TaskInfo) | optional |  |
| task_context | [TaskContext](#bom.TaskContext) | optional |  |
| task_manager_context | [TaskManagerContext](#bom.TaskManagerContext) | optional |  |
| task_status | [TaskStatus](#bom.TaskStatus) | optional | The current status of the task. |
| task_interaction | [TaskInteraction](#bom.TaskInteraction) | optional | Interaction being performed on the task (if any).Note: the task_status in this particular event is not a result of thisparticular interaction. Rather, this task is in this event's task_statusstate when the task_interaction begins. Subsequent events may includetask_status changes as a result of this interaction |


<a name="bom.TaskGroupLimits"/>
### TaskGroupLimits
Limit placed on the number of simultaneously running tasks for tasks
belonging to a particular group/type/pool or using a particular resource

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | Name of the limit |
| description | [string](#string) | optional | Description of this limit |
| number | [int64](#int64) | optional | The limit number (maximum number of dispatched/running tasks) |
| group | [string](#string) | optional | The task group the limit applies to (if applicable) |
| resource | [string](#string) | optional | The resource the limit applies to (if applicable)Note: one of group or resource must be specified for the the limitto be meaningful |


<a name="bom.TaskInfo"/>
### TaskInfo
Descriptive, human meaningful information about the nature of the task.
This information should mostly be known ahead of the scheduling of the task.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional |  |
| namespace | [string](#string) | optional | Unique namespace for this task within a suite or workflow.This is typically the task families to which the task belongs |
| suite | [string](#string) | optional | The suite or workflow this task is a part of |
| type | [string](#string) | optional | Type of task |
| about | [URI](#bom.URI) | optional | Documentation/information about task |
| troubleshooting | [URI](#bom.URI) | optional | General troubleshooting information, if not covered by "about" |
| project | [string](#string) | optional | project (in the context of a batch system scheduler, or similar) |
| properties | [TaskProperty](#bom.task_property.TaskProperty) | repeated | Properties this task might have, such as IDEMPOTENT, RESERVATION.Note: some properties may not be known until runtime.TaskEvent.context.settings provides an additional opportunity to specifyadditional task/job properties. |
| groups | [string](#string) | repeated | The group(s) this task is part of, if relevant. Groups are generallya  grouping of similar tasks in the context of a workflow |
| resources | [string](#string) | repeated | Named resources this task interacts with, e.g. particular databases,services, archive storage systems etc |
| production_status | [ProductionStatus](#bom.ProductionStatus) | optional | Production status of task |
| priority | [Priority](#bom.Priority) | optional | Priority of task. Note this can include information about impact andurgency |
| tags | [Tag](#bom.Tag) | repeated | User-defined additional tags |


<a name="bom.TaskInteraction"/>
### TaskInteraction
Metadata about the entity involved in some interaction

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| action_type | [TaskInteractionType](#bom.task_interaction_type.TaskInteractionType) | optional |  |
| actor | [Actor](#bom.Actor) | optional | Details of the entity initiating or carrying out this interaction, ifknown |
| reason | [string](#string) | optional | Motivation for the interaction, if relevant |
| system | [Id](#bom.Id) | optional | The system/equipment/tool via which the interaction took place.This will generally be the scheduler, or a component of a scheduler |
| detail | [string](#string) | optional | Additional interaction details/context |
| id | [Id](#bom.Id) | optional | ID to track this interaction |
| on_behalf_of | [TaskInteraction](#bom.TaskInteraction) | optional | To be set when this interaction is on behalf or as a consequence ofanother entity or interaction |


<a name="bom.TaskManagerContext"/>
### TaskManagerContext
Task manager context contains information about a management
context of the task, as known by this message producer.
The task manager may be a workflow scheduler, batch scheduler,
orchestration system etc
Note: all metadata pertains to the task manager itself, in the context
of this task. Most task-specific metadata, even if controlled by a
manager, is exposed in the parent TaskContext message

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | e.g. PBS |
| component_id | [int64](#int64) | optional | The index in the Producer components list that corresponds to thistask manager component. |
| id | [Id](#bom.Id) | optional | Id of manager/scheduler if relevant |
| saga_id | [Id](#bom.Id) | optional | Additional id to track manager specific task context information,e.g. be used for dag_id (directed acyclic graph id), suite id etc |
| output_collection_task_ids | [Id](#bom.Id) | repeated | Tasks associated with collecting task outputs, if also managed bythis scheduler and if known |
| monitoring_task_ids | [Id](#bom.Id) | repeated | Tasks associated with monitoring tasks, if also managed bythis scheduler and if known |


<a name="bom.TaskQueue"/>
### TaskQueue
Information about the queue a tasks/job belongs to, as might be
managed by a job or batch scheduler

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | Name of the queue |
| type | [string](#string) | optional | Type of the queue |
| rank | [int64](#int64) | optional | Number indicating position of job/task within the queue. |
| time | [Timestamp](#google.protobuf.Timestamp) | optional | The time the task entered this queue |


<a name="bom.TaskResource"/>
### TaskResource
Computing resource associated with a task or job:

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [ComputingResource](#bom.computing_resource.ComputingResource) | optional | Type of computing resource |
| scope | [ComputingResourceScope](#bom.computing_resource_scope.ComputingResourceScope) | optional | The scope (level of applicability) of this particular resource; e.g. ifit is job-wide or at a host level. |
| chunk_id | [Id](#bom.Id) | optional | Identifier to help track resources belonging to a particular "chunk" orsome other grouping (if applicable) |
| qualifier | [string](#string) | optional | Qualifying description or name or model of resource,e.g. NVIDIA Tesla P100 |
| number | [uint64](#uint64) | optional | The number needed of this type of resource, when the resourcerepresents discrete entities (e.g. if type = ACCELERATOR,qualifier = i) |
| amount | [int64](#int64) | optional | Value per resource in milliseconds for duration,kibibytes (1024 bytes) for memory/disk,Mbit/s for network performance,MHz (megahertz) for CPU clock speeds; or a count in other contexts.If values represent a fractional increment using these units, the valuesshould be rounded up (i.e. int64 amount = ceiling(value)). Negativeamounts are permissible with a production-specific meaning. |
| is_hard_limit | [bool](#bool) | optional | If limit the amount represents a resource limit, whether it ishard (otherwise it is considered "soft"). To be ignored if thismessage does not correspond to a resource limit |
| steward | [SystemActorType](#bom.system_actor_type.SystemActorType) | optional | Entity responsible for measuring this resource, or for ensuringany limit (if applicable) is respected by some suitable means(e.g. the governor batch scheduler or native system) |


<a name="bom.TaskRetry"/>
### TaskRetry
Metadata about expected automatic retries/reruns for tasks.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| submit_number | [int64](#int64) | optional | Current known submit number |
| submit_retry_limit | [int64](#int64) | optional | Number of times this task's submit phase should be retried automatically |
| submit_retry_delay | [Duration](#google.protobuf.Duration) | optional | Delay before next submit retry is attempted. If retrying is underwaypresently, then this refers to the delay (if any) beforethis fresh retry attempt is progressed |
| try_number | [int64](#int64) | optional | Current known execution try number |
| retry_limit | [int64](#int64) | optional | Number of times this task should be retried automatically, asset in a top-level workflow scheduler before the task isconsidered to have failed/aborted |
| retry_delay | [Duration](#google.protobuf.Duration) | optional | Delay before next retry is attempted. If retrying is underwaypresently, then this refers to the delay (if any) beforethis fresh retry attempt is progressed |


<a name="bom.TaskSettings"/>
### TaskSettings


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| note | [string](#string) | optional | A note about the settings |
| user | [Userid](#bom.Userid) | optional | The user/account/identity that the task is to run as |
| subusers | [Userid](#bom.Userid) | repeated | Other users/accounts that processes/subcomponents launched by the taskwill run as (e.g. task involving sudo commands for another service account) |
| properties | [TaskProperty](#bom.task_property.TaskProperty) | repeated | Setting properties this task might have, such as RUNMODE_DUMMY,RUNMODE_TEST, ARRAY.Note 1: some properties may also be set in TaskEvent.task_infoNote 2: debug settings are handled separetely in "debug" below |
| debug | [DebugSettings](#bom.DebugSettings) | optional | Time from which the task is eligible to run (if applicable)/ Debug settings that apply to this task |
| eligible_time | [Timestamp](#google.protobuf.Timestamp) | optional |  |


<a name="bom.TaskStatus"/>
### TaskStatus
The task status is a combination of the task state and the
system reporting/interpreting the task state.
Note the time(s) relating to a task state change report
can be approximated by the time-stamp in the Kafka header
for real-time systems

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [TaskState](#bom.task_state.TaskState) | optional | Current or new task state |
| state_actor | [Actor](#bom.Actor) | optional | Details of entity that caused the task state (if relevant and known) |
| reporter_type | [SystemActorType](#bom.system_actor_type.SystemActorType) | optional | Type of entity reporting the new state |
| reporter | [string](#string) | optional | The name of the system or entity reporting the state, e.g. Cylc or PBS |
| diagnostics | [Diagnostic](#bom.Diagnostic) | repeated | Diagnostics about task including information about errors orwarnings that may be associated with this task state |
| message | [string](#string) | optional | A message/note about task state |
| severity | [Severity](#bom.severity.Severity) | optional | Severity of new task state. Each diagnostic also has a severity,and this may be left unset if it is possible to infer the task stateseverity from the diagnostic(s) |
| time_info | [TaskTimes](#bom.TaskTimes) | optional |  |
| number_of_consecutive_failures | [int64](#int64) | optional | Number of consecutive task failures in a task series |
| late | [Duration](#google.protobuf.Duration) | optional | If task is "late", set late to the length of time thetask is late by (valid at the time of event production) |


<a name="bom.TaskTimes"/>
### TaskTimes
Times to track significant changes in task state, from the
perspective of the event message producer.
This tracking is a convenience feature; if events are produced
with sufficient granularity this information can be inferred from
a sequence of changes in event state.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| series_created_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | The time when the first task in this task series wascreated (if applicable) |
| instance_created_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Datetime this instance of the task was created (as known by themessage producer) |
| series_start_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Datetime the first task in this task series started (if applicable) |
| instance_start_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Datetime this instance of the task started (if applicable) |
| instance_end_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Datetime this instance of the task ended (if applicable) |
| first_failure_timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Datetime of first task failure in a series (if known and applicable) |


<a name="bom.Taskid"/>
### Taskid
A rather imperfect mechanism to identify dynamic task IDs or IDs that
may relate to this task.
Note that interaction_id and correlation_ids (that might help track this task
if it is part of actions resulting from a user request or some other chain
of tasks) are included in the EventHeader

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| submit_name | [string](#string) | optional | The name the task was submitted as if this differs fromthe name in taskInfo (e.g. if the submit name is dynamically generated)Often this is referred to as the "jobname" |
| workflow_id | [Id](#bom.Id) | optional |  |
| batch_id | [Id](#bom.Id) | optional | Batch ststem jobid |
| session_id | [Id](#bom.Id) | optional | An ID used internally by the producer of this event |






<a name="actor.proto"/>
<p align="right"><a href="#top">Top</a></p>

## actor.proto



<a name="bom.Actor"/>
### Actor
An entity that interacts with a system/component

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| system_actor_type | [SystemActorType](#bom.system_actor_type.SystemActorType) | optional | System type of actor, if relevant/applicable |
| id | [Userid](#bom.Userid) | optional | Most relevant user/account identification (Security Principal) detailscorresponding to this actor, if relevant/applicable. |
| contact | [Contact](#bom.Contact) | optional | Contact details of actor, if known |






<a name="address.proto"/>
<p align="right"><a href="#top">Top</a></p>

## address.proto



<a name="bom.Address"/>
### Address
A network address.
May contain a hostname (or a similar registered address),
IP address, or both. Note: it is permissible for hostname
to represent a batch scheduler cluster address,
eg SGE_CLUSTER_NAME

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hostname | [string](#string) | optional |  |
| ip | [string](#string) | optional |  |
| port | [int32](#int32) | optional | port is Nullable |


<a name="bom.URI"/>
### URI
Represents a URI/URL.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scheme | [string](#string) | optional |  |
| username | [string](#string) | optional |  |
| password | [string](#string) | optional |  |
| address | [Address](#bom.Address) | optional |  |
| path | [string](#string) | optional |  |
| queries | [Tag](#bom.Tag) | repeated |  |
| fragment | [string](#string) | optional |  |






<a name="component.proto"/>
<p align="right"><a href="#top">Top</a></p>

## component.proto



<a name="bom.ClusterInfo"/>
### ClusterInfo


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | The cluster/cloud name |
| id | [Id](#bom.Id) | optional | ID of the cluster, if applicable |
| engine_name | [string](#string) | optional | The engine or controller managing the cluster/cloud environment |
| engine_version | [Version](#bom.Version) | optional | The version of the managing engine/controller |
| region | [string](#string) | optional | Each region is a separate geographic area, in the context of adistributed cloud platform |
| availability_zone | [string](#string) | optional | Availibility zones are isolated locations within a region |
| host_type | [string](#string) | optional | The host type aligns with specified hardware of the host computer forthis instance |
| placement_group_name | [string](#string) | optional | Placement group that launched the instance |
| namespace | [string](#string) | optional | The namespace this instance belongs to, if applicable |
| env_name | [string](#string) | optional | Reference to a named environment/configuration |
| vps_security_group_ids | [Id](#bom.Id) | repeated | A list that contains the security group IDs for virtual private cloudsecurity groups |
| security_groups | [string](#string) | repeated | A list that contains security group names registered for this instance |
| subnet_id | [Id](#bom.Id) | optional | Cluster subnet id. This may for example correspond to a virtual privatecloud subnet group id |
| additional_info | [string](#string) | optional |  |
| tags | [Tag](#bom.Tag) | repeated |  |


<a name="bom.Component"/>
### Component
Summary of application or device component.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [Component.Info](#bom.Component.Info) | optional | Component identifying information |
| relation_id | [int64](#int64) | optional | ID of component as used in component relationship descriptionThe set of relation_ids used across components in a Producer message needonly identify unique components for that particular Producer message. Thereis no need for such ids to be globally meaningful or consistent acrossmessages from different producers. |
| relationships | [Component.Relation](#bom.Component.Relation) | repeated | Relationship of this component to other component(s) at aworkflow/dataflow level, permitting a relational directed graph to beconstructed.NB: for any given pair of components there need only be one relationship.Multiple relationships for the same pair shall be treated in an additiveway where possible. The addition of two or more contradictoryrelationships may be undefined/ambiguous. |
| user | [Userid](#bom.Userid) | optional | Username or service account under which the relevant_component is running |
| instance_id | [Id](#bom.Id) | optional | In certain contexts different instances of the same component may beassigned a specific id, e.g. a UUID |
| host | [Device](#bom.Device) | optional | Information about the host device that the relevant_component isrunning on |
| logs | [LogInfo](#bom.LogInfo) | repeated | Relevant logs generated by this component |
| tags | [Tag](#bom.Tag) | repeated | Addtional user-defined information about this component |


<a name="bom.Component.Info"/>
### Component.Info
Component.Info: Information about the component that will mostly or
entirely be known at deploy time

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [ComponentLevel](#bom.component_level.ComponentLevel) | optional |  |
| name | [string](#string) | optional | Name of component |
| type | [string](#string) | optional | The type of the component, e.g. HTTP server, iOS app, Cylc suite etc |
| version | [Version](#bom.Version) | optional | Version of component |
| description | [string](#string) | optional | More detailed description of component |
| uri | [URI](#bom.URI) | optional | URI for more information about the component |
| production_status | [ProductionStatus](#bom.ProductionStatus) | optional | The level of support for the component |
| family | [string](#string) | optional | Family of systems that this component is part of, e.g. ACCESSNote: maps to stream for MDS model data |
| family_version | [Version](#bom.Version) | optional | Family-level version information, if relevant.Note: maps to stream version for MDS |
| project_name | [string](#string) | optional | Internal project name best aligned with the relevant component(if relevant) |
| contacts | [Contact](#bom.Contact) | repeated |  |
| universal_id | [Id](#bom.Id) | optional | This component may have a global/universally unique identifier |
| namespace | [string](#string) | optional | Component namespace, if applicable |


<a name="bom.Component.Relation"/>
### Component.Relation
Describes the relationship between this component and other components.
Consider Components representing labelled vertices/nodes of a graph; then
the Component Relations represent labelled edges that connect these
vertices.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [int64](#int64) | optional | ID of other component. ie the "other identified component" |
| relationship | [ComponentRelation](#bom.component_relation.ComponentRelation) | optional |  |
| relation_description | [string](#string) | optional | Description of the relationship/connection. eg the protocol used fora data transfer, the name of the network over which the connectionoccurs or information about the timing/rate of information flow etc |
| data_description | [string](#string) | optional | Description of any data involved/shared/passed via therelationship/connection (if applicable) |


<a name="bom.Device"/>
### Device
Summary-level information about a device, machine or server

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| realm | [Realm](#bom.realm.Realm) | optional | The "realm" classification of the device (e.g. DEV, STAGE, PROD) |
| type | [string](#string) | optional |  |
| physical_desc | [string](#string) | optional | String representation of the physical device |
| address | [Address](#bom.Address) | optional | Hostname (or a similar registered address) of the deviceIf service is distributed, the address of the interface or masterserver |
| device_id | [Id](#bom.Id) | optional | ID of the device, if applicable |
| image_id | [Id](#bom.Id) | optional | ID of the node or machine image (as built for a container orassigned by a container or cluster manager) or similar |
| container_path | [string](#string) | optional | Path of the device within a container, if applicable |
| architecture | [string](#string) | optional | Architecture of device, e.g. x86_64 |
| os | [string](#string) | optional | Operating system of the machine running the component, or name offirmware if applicable |
| os_version | [Version](#bom.Version) | optional | OS version/kernel information (or firmware version if applicable) |
| cluster_info | [ClusterInfo](#bom.ClusterInfo) | optional | More detailed information for applications running in a clusteror cloud context |
| tags | [Tag](#bom.Tag) | repeated | Additional annotations or tags to describe the device |


<a name="bom.ProductionStatus"/>
### ProductionStatus
The operational/production status of a system. This mainly relates to
the degree of support for the system along with the environment in which
it is running

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status | [ProdStatus](#bom.prod_status.ProdStatus) | optional |  |
| info | [string](#string) | optional | Additional information about the production status, e.g. caveats thatmight apply. |






<a name="contact.proto"/>
<p align="right"><a href="#top">Top</a></p>

## contact.proto



<a name="bom.Contact"/>
### Contact
Contact information for a person, team or organisation.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) | optional | Name of individual, team or organisation |
| role | [string](#string) | optional | Role/capability/context of the contact. Includes:researcher, developer, author, custodian, distributor,originator, owner, point_of_contact, principal_investigator,processor (when post-processing/modification occurs),publisher, resource_provider, sponsor, user, co_author,collaborator, contributor, editor, reviewer, funder,mediator, rights_holder, stakeholder |
| organisation | [string](#string) | optional | The organisation to which the contact belongs |
| url | [URI](#bom.URI) | optional | URL pointing to contact information |
| email | [string](#string) | optional | The email address of the contact person/group/organisation |
| phone_nums | [int64](#int64) | repeated | The phone numbers that can be used to call the contact |
| others | [Tag](#bom.Tag) | repeated | Other contact mechanisms, e.g. {"Skype", "SkypeUserId"} |






<a name="debug_settings.proto"/>
<p align="right"><a href="#top">Top</a></p>

## debug_settings.proto



<a name="bom.DebugSettings"/>
### DebugSettings
Debug and program trace related settings.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| debug_level | [DebugLevel](#bom.debug_level.DebugLevel) | optional |  |
| debug_level_int | [int64](#int64) | optional |  |
| debug_level_str | [string](#string) | optional |  |
| trace_level | [TraceLevel](#bom.trace_level.TraceLevel) | optional |  |






<a name="diagnostic.proto"/>
<p align="right"><a href="#top">Top</a></p>

## diagnostic.proto



<a name="bom.Diagnostic"/>
### Diagnostic
Diagnostic information related to the functioning of a component or task.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [ErrorType](#bom.error_type.ErrorType) | optional | The type of error or warning |
| severity | [Severity](#bom.severity.Severity) | optional | Severity of warning or error; distinguishes betweeninformational diagnostics, warnings that may warrantinvestigation, non-fatal errors and fatal errors |
| return_status | [int64](#int64) | optional | Return status/exit-code of process/task/sub-component |
| signal | [string](#string) | optional | Signal that was caught or trapped (irrespective of being handledor not) |
| timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | The timestamp the diagnostic was recorded, if expected tobe different to the event timestsamp or to help order a sequenceof diagnostic messages |
| phase | [string](#string) | optional | The phase of the component during which the warning or error occured.For example, "initialization", "execution", "data_write", "cleanup" etc. |
| message | [string](#string) | optional |  |
| cause | [string](#string) | optional |  |
| trace | [string](#string) | optional | A stack trace or similar |
| troubleshooting | [URI](#bom.URI) | optional | If a known error pattern, link to troubleshooting info |
| model_diagnostic | [ModelDiagnostic](#bom.ModelDiagnostic) | optional |  |


<a name="bom.ModelDiagnostic"/>
### ModelDiagnostic
Additional diagnostic information pertaining to a numerical model
(or similar system)

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ensemble_member | [EnsembleMember](#bom.EnsembleMember) | optional |  |
| model_validity_time | [Timestamp](#google.protobuf.Timestamp) | optional | For models, the simulation step/time that was reached. |
| iteration | [int64](#int64) | optional |  |






<a name="ensemble_member.proto"/>
<p align="right"><a href="#top">Top</a></p>

## ensemble_member.proto



<a name="bom.EnsembleMember"/>
### EnsembleMember


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ensemble_class | [string](#string) | optional | Ensemble_class can be used to distinguish between ensemble groupsin ensemble of ensemble systems. |
| ensemble_member_description | [string](#string) | optional | Description of ensemble member, if applicable |
| ensemble_member_number | [int64](#int64) | optional | Model member ensemble_number, if applicable. Member numbers can berepeated across different ensemble_classes if desirable |






<a name="event_header.proto"/>
<p align="right"><a href="#top">Top</a></p>

## event_header.proto



<a name="bom.EventHeader"/>
### EventHeader
Standard header to be included in all event messages.
Note unique message identifiers are tracked outside of the message content.
It is recommended the unique identifier:
KafkaTopic.kafka_message_timestamp.partition.offset
is used to allow agents to interact with events efficiently via Kafka.
The kafka_message_timestamp is a safeguard against the offset for
a particular partition being reset.
A suitable digital signature or other digest of the message could
alternatively be used.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| producer | [Producer](#bom.Producer) | optional | The producer of this message |
| timestamp | [Timestamp](#google.protobuf.Timestamp) | optional | Event timestamp for events where the message timestampmay not match the time of the event (e.g.for offline systems upon network sync) |
| sequence_number | [uint64](#uint64) | optional | For those producers that can support this: a number that starts at 1and increments by 1 with each new event message of this type over thelifetime of this event message producer's instance. Upon producer restarts,this seuqence number is permitted to be reset to 1.This metadata is useful in a number of contexts, e.g. a missing numberin a sequence is possible evidence of a lost event. An unexpected sequencenumber is possible evidence of spoofed message injection by a 3rd party. |
| correlation_id | [Id](#bom.Id) | optional | Correlation id (sometimes known as a transit id) is an id that refers toa particular event chain |
| interaction_id | [Id](#bom.Id) | optional | Interaction id for a event generated as a result of action(s)s initiatedfrom a (usually user) interaction (e.g. with a business system). This isideally tracked for all components handling the interaction |






<a name="log_info.proto"/>
<p align="right"><a href="#top">Top</a></p>

## log_info.proto



<a name="bom.LogInfo"/>
### LogInfo
Log information

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [LogType](#bom.log_type.LogType) | optional | The type of log file |
| logfiles | [URI](#bom.URI) | repeated | The location(s) of this log file. More than one location implies thesame log information is available in each location |






<a name="priority.proto"/>
<p align="right"><a href="#top">Top</a></p>

## priority.proto



<a name="bom.Priority"/>
### Priority
Priority

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| impact | [Impact](#bom.impact.Impact) | optional | Production impact/value/importance of task/component |
| urgency | [Impact](#bom.impact.Impact) | optional | How time-critical (this action is, or fixing a reported error state is) |
| priority | [int64](#int64) | optional | Priority, usually for task scheduling purposes.It may be helpful to derive this from impact and urgency. |






<a name="producer.proto"/>
<p align="right"><a href="#top">Top</a></p>

## producer.proto



<a name="bom.Producer"/>
### Producer
Event/message producer component and device details. Component is usually a
software component and device is usually the hardware the component is
running on, or the virtualised equivalent.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| components | [Component](#bom.Component) | repeated | Key components that contributed to the generation of this event. |
| producer_component_id | [int64](#int64) | optional | ID of component that corresponds to the system that most applies to thisevent. This normally corresponds to the system that created the event, butif monitoring components are involved it may refer to the system that isbeing monitored about which the event relates |






<a name="security_marking.proto"/>
<p align="right"><a href="#top">Top</a></p>

## security_marking.proto



<a name="bom.SecurityMarking"/>
### SecurityMarking
SecurityMarking specifies the classification and dissemination restrictions:

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| security_classification | [SecurityClassification](#bom.security_classification.SecurityClassification) | optional |  |
| dissemination_limiting_marker | [SecurityDelimitingMarker](#bom.security_delimiting_marker.SecurityDelimitingMarker) | optional |  |
| caveats | [string](#string) | repeated |  |






<a name="tag.proto"/>
<p align="right"><a href="#top">Top</a></p>

## tag.proto



<a name="bom.Id"/>
### Id
A generic ID, it may be an array of bytes, a string or an integer.
This message may also be used to represent a
message digest (checksum/fingerprint/hash)

One of id_str, id_bytes, id_int or id_uint is to be set

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id_str | [string](#string) | optional |  |
| id_bytes | [bytes](#bytes) | optional |  |
| id_int | [int64](#int64) | optional |  |
| id_uint | [uint64](#uint64) | optional |  |


<a name="bom.Tag"/>
### Tag
A generic (key, value) string pair used in various places for
parameters/tags/labels.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) | optional |  |
| value | [string](#string) | optional |  |






<a name="time.proto"/>
<p align="right"><a href="#top">Top</a></p>

## time.proto



<a name="bom.TimePointOrRange"/>
### TimePointOrRange


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| point | [Timestamp](#google.protobuf.Timestamp) | optional | A point (moment) in time |
| time_range | [TimeRange](#bom.TimeRange) | optional | A time range |


<a name="bom.TimeRange"/>
### TimeRange
A generic time range

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [Timestamp](#google.protobuf.Timestamp) | optional |  |
| end | [Timestamp](#google.protobuf.Timestamp) | optional |  |
| interval | [Duration](#google.protobuf.Duration) | optional | Intervals within range. Used to construct a list of times from"start" at regular intervals onward, but not greater than "end". |






<a name="userid.proto"/>
<p align="right"><a href="#top">Top</a></p>

## userid.proto



<a name="bom.Userid"/>
### Userid
User/account identification (Security Principal)

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| userid | [uint64](#uint64) | optional | User idID of account |
| name | [string](#string) | optional | Principal name / account name / username / access-ide.g. a simple username orusername/fully.qualified.domain.name@YOUR-REALM.COMdepending on the authorisation system in use |
| realm | [string](#string) | optional | Security realm, if applicable |
| id_str | [string](#string) | optional |  |
| id_bytes | [bytes](#bytes) | optional |  |
| principal_type | [string](#string) | optional | Type of principal, e.g. NT_USER_NAME, KERBEROS_V5_PRINCIPAL_NAME,NT_EXPORT_NAME, NT_HOSTBASED_SERVICE |






<a name="version.proto"/>
<p align="right"><a href="#top">Top</a></p>

## version.proto



<a name="bom.SemVer"/>
### SemVer
A semantic or compatible version representation with the format:
major.minor.patch.pre_release_id1.pre_release_id2+build_id1.build_ids

where major, minor and patch are integers >= 0 and
pre_release_ids and/or build_ids are optional and there can any number.

If all major, minor and patch levels are specified this complies with the
Semantic Version scheme (although with a upper bound imposed on the range
of integers).

If patch level is omitted it is compliant with the Common Version (ComVer)
versioning scheme, which is also often also used for versioning datasets

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| major | [uint64](#uint64) | optional |  |
| minor | [uint64](#uint64) | optional |  |
| patch | [uint64](#uint64) | optional | patch is Nullable |
| pre_release_ids | [string](#string) | repeated | pre_release_ids: alphanumeric with "-" chars allowed but integers with a0 prefix disallowed (but "0" by itself allowed) e.g. alpha, alpha-1, 30 |
| build_ids | [string](#string) | repeated | build_ids have the format as pre_release_ids |


<a name="bom.Version"/>
### Version
Flexible representation of a version.
One of semver, string_ver, int_ver or date_ver is allowed to be set

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| semver | [SemVer](#bom.SemVer) | optional |  |
| string_ver | [string](#string) | optional |  |
| int_ver | [int64](#int64) | optional |  |
| date_ver | [Timestamp](#google.protobuf.Timestamp) | optional |  |






<a name="component_level.proto"/>
<p align="right"><a href="#top">Top</a></p>

## component_level.proto




<a name="bom.component_level.ComponentLevel"/>
### ComponentLevel
ComponentLevel broadly describes terms useful to help delineate a software
component or devices hierarchy amongst other related components of a wider
system.
The hierarchical order of labels is dependent on the system and context.
Note: excludes "environmental" concepts, e.g. versions
      of libraries, runtime systems, virtual machine, OS for an application

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| SYSTEM | 2 | System-level / OS level |
| PLATFORM | 3 | Platform is an entity that allow multiple products to be built within thesame technical framework. e.g. an enterprise service bus,a workflow manager, a web platform, an overarching gaming "service/app"like Valve's steam would constitute a platform |
| SUITE | 4 | A suite of related software components. e.g. a suite of tasks thatconstitute the setup, running and post-processing of a NWP model |
| DEVICE | 5 | A physical or virtual device |
| APPLICATION | 6 | Application here means a computer program |
| COMPONENT | 7 | A component of an application or device |
| SUBCOMPONENT | 8 |  |
| CONNECTOR | 9 | A light-weight component responsible for serialising and forwardinginformation e.g. a log file reader daemon, a Kafka connector, a data relay |
| SERVICE | 10 |  |




<a name="component_relation.proto"/>
<p align="right"><a href="#top">Top</a></p>

## component_relation.proto




<a name="bom.component_relation.ComponentRelation"/>
### ComponentRelation
ComponentRelation describes the type of high-level data-flow, process or
hierarchical relationship (whichever is most relevant) that this component
has to the other identified component. The relationship is usually
directional, e.g.:
1. an outbound data-push or downstream (sequentially) processing
   connection or relationship from this component to the other component.
2. an inbound (data pull or upstream) relationship or connection from the
 other component to this component.
Note: inbound/output semantics vary between different flow chart/
      process or architectural diagram methodologies. The following
      definitions are intended to best represent simplified high-level
      data-flow/work-flow practices. In reality most actual relationships
      involve varying degrees of two-way interactions (e.g. a data
      push over TCP involves inbound traffic associated with the
      handshake and acknowledgements)

SUPERCOMPONENT through to EVENT_SRC describe "outbound" directed arcs/edges.
i.e. an outbound connection or relation from this component to the
other identified component

SUBCOMPONENT through to EVENT_SINK describe "inbound" directed arcs/edges.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| SUPERCOMPONENT | 2 | This component is a supercomponent of the other component. ie theother component is a subcomponent. Generally a supercomponent manages/delegates work or pushes instructions/data to the subcomponent, hencethis is principally an outbound relationship from the perspective ofsequential process workflow |
| UPSTREAM_REQUIREMENT | 3 | This component involves an upstream requirement that must be met beforethe other component can carry out its function. e.g. thiscomponent may be a task that must complete before the other taskcan begin |
| INSTRUCTOR | 4 | The two components are part of distinct ecosystems, yet thiscomponent is managing/directing (or delegating) activity in theother component. |
| SYS_MONITORED | 5 | System characteristics of this components operation are being monitoredby the other component (in a "pull"/"query"/"poll"/"listen"-likefashion). This component may indeed not be directly "aware" of thismonitoring. In some cases this component may be providing an API orevent-based mechanism which supports such monitoring."System"-level monitoring entails watching system processes,metrics or diagnostic/logged data generated by this component tohelp ascertain the health or state of this component |
| SYS_ANALYSED | 6 | As per SYS_MONITORED but the other system is also performing a moresignificant analysis of this components systems. Such analysis mayor may not be happening in real-time |
| DATA_MONITORED | 7 | This components output data is being watched/monitored by the othercomponent (in a "pull"/"query"/"poll"/"listen"-like fashion)."Data"-level monitoring entails tracking output generatedby this component (e.g. gridded model output, product generation,observations collected from sensors etc). Typically such tracking maytake place to monitor the progress of this components run-timeor operation, to create dataset events on behalf of thisapplication or to direct yet another component to perform someoperation with the data (e.g. copying, validating, ingesting,notifying etc) |
| DATA_SRC_FOR_VALIDATION | 8 | This components output data is read by the other componentfor a technical validation step. This component thereforerepresents a data source that is used by the other component |
| DATA_SRC_FOR_VERIFICATION | 9 | As per DATA_SRC_FOR_VALIDATION but where the other component formspart of a scientific verification step/process |
| DATA_SRC_FOR_INGEST | 10 | This components output data is ingested by the other componentfor further processing |
| DATA_SRC_FOR_ARCHIVAL | 11 | This components output data is archived by the other component(to a local or remote data store) |
| DATA_SRC_FOR_TRANSFER | 12 | This components output data is copied/transferred by the othercomponent to a local or remote destination (ie the other componentrelays this data onward or provides connectivity services for thisdata) |
| DATA_RELAY_OUTBOUND | 13 | this component is a data relayer/connector that receives data fromanother system and relays it to the identified component |
| SRC_FOR_CLONING | 14 | This components state is cloned/mirrored/replicated to the othercomponent |
| EVENT_SRC | 15 | This component issues event(s) for consumption by the other component |
| SUBCOMPONENT | 64 | This component is a subcomponent of the other component |
| DEPENDENT_ON | 65 | This components depends on the other component to perform someaction(s) or reach/set some state(s) before this component can progressits function |
| INSTRUCTED | 66 | This component is being instructed to perform work by a componentbelonging to a different system tier/suite/device ecosystem |
| SYS_MONITOR | 67 | This component pulls system-level data/metrics from the other componenti.e. this component is a consumer of system-related change of stateinformation generated by the other component |
| SYS_ANALYSER | 68 | As per SYS_MONITOR but this system is also performing a more intensiveanalysis of the data collected |
| DATA_MONITOR | 69 |  |
| DATA_RECEIVER_FOR_VALIDATION | 70 |  |
| DATA_RECEIVER_FOR_VERIFICATION | 71 |  |
| DATA_RECEIVER_FOR_INGEST | 72 |  |
| DATA_RECEIVER_FOR_ARCHIVAL | 73 |  |
| DATA_RECEIVER_FOR_TRANSFER | 74 | This component receives data from the other identified component withthe intention of transferring this data to another location/componentNote: DATA_RECEIVER_FOR_TRANSFER is equivalent to a"DATA_RELAY_INBOUND" (a relayer that receives data from the otheridentified component) |
| RECIPIENT_OF_CLONING | 75 | This component is cloned from the other identified component |
| EVENT_SINK | 76 | This component receives events produced by the other identifiedcomponent |




<a name="computing_resource.proto"/>
<p align="right"><a href="#top">Top</a></p>

## computing_resource.proto




<a name="bom.computing_resource.ComputingResource"/>
### ComputingResource
Computing related resources, as relating to
capabilities or limits of a computing environment or
limits imposed on jobs or processes by policy or
management systems.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| CPU | 2 | Physical CPU detailsnumber: number of physical CPUs (with respect to specified scope)amount: speed in MHzqualifier: specific model/type/variant |
| VCPU | 3 | Virtualised CPU details. Units as per CPU. |
| CORES | 8 | Physical CPU cores. Units as per CPU. |
| NUMA | 10 | NUMA detailsnumber: number of NUMAs (with respect to specified scope)amount: number of parallel environment per NUMAqualifier: specific variant of NUMA (if applicable) |
| ACCELERATOR | 14 | Accelerator details. Units as per CPU |
| MPIPROC | 18 | MPI process detailsnumber: number of MPI processes requestsamount: N/Aqualifier: specific type/mode or other details ofMPI process (if applicable) |
| OMPTHREADS | 19 | OMP thread detailsnumber: number of OMP threads (usually per "chunk" or process)amount: N/Aqualifier: notes/commentary on OMP threads or similar |
| NETWORK | 20 | Network detailsnumber: number of network interfaces comprising this resourceamount: speed of each interface in Mbit/squalifier: specific model/type/variant of network interface |
| NODE_COMPUTE | 30 | Specified resource is a type of nodenumber: number of this type of node comprising this resourceamount: N/Aqualifier: specific model/type/variant |
| NODE_LOGIN | 31 |  |
| NODE_DATAMOVER | 32 |  |
| NODE_MAMU | 33 | MAMU = "multi-application multi-user" |
| NODE_MOM | 34 | MOM = "machine oriented miniserver" |
| HOST | 35 | A specific single host.number: set to 1 or leave unsetamount: if more than one host is specified as independent resources for        a job/task, then set amount to 1 if work carried out by the job,        at the level set by the "scope", is allowed/intended to be run in        parallel across nominated hostsqualifier: hostname of host, or another unique string identifier ifa hostname is not suitable |
| SITE | 36 | Resources contained within a particular data-centre site. If more thannumber: N/Aamount: if more than one site is specified as independent resources for        a job/task, then set amount to 1 if work carried out by the job,        at the level set by the "scope", is allowed/intended to be run in        parallel across nominated sites (or leave unset if site affinity)        is required. If site affinity is required, it is intended that        the order that multiple site resources are specified reflects        an ordering preference (for resource requests) or the ordering        in which task execution took place (for resources reported/used)        in the case where a task was migrated between data-sets during        the course of execution.qualifier: name of site nominated to provide resource |
| ARCH | 40 | Specified resource is a specific architecture.number: N/Aamount: N/Aqualifier: specified architecture (and version if applicable). |
| AOE | 41 | AOE - Application Operating Environment. Units as per ARCH, exceptthis usually refers to an environment at the OS-level. |
| SOFTWARE | 42 | Software requirement. Unit as per ARCH, except this refers toa particular (usually unusual) software application/framework |
| WALLTIME | 50 | Execution walltime available. If MIN_WALLTIME also requested by jobthis job is considered to be a "shrink-to-fit" job and walltimeis interpreted as a "MAX_WALLTIME".amount units: milliseconds |
| MIN_WALLTIME | 51 | Minimum execution walltime requested for a "shrink-to-fit" job.amount units: milliseconds |
| CPUTIME | 52 | Execution cputime available. Set TaskResource.scope to distinguishbetween a job-wide resource or a per-process resourceamount: time in milliseconds |
| MEMORY | 70 | RAM/memory available (set TaskResource.scope to distinguish if thisapplies job-wide, chunk-wide, per process etc)amount units: kibibytes (1024 byte increments)qualifier: can be used to specify the name of a specialist memory variant |
| VIRT_MEMORY | 71 | Virtual memory available. Units as per MEMORY |
| ACCELERATOR_MEMORY | 72 | ACCELERATOR memory available. Units as per MEMORY |
| STACK | 75 | Stack size available. Units as per MEMORY |
| DISK | 80 | Persistent disk storage available (generally shared by job)number: number of disks, RAID arrays or similar providing this resourceamount: size of disk resource kibibytes (per disk if number > 1)qualifier: specific disk/storage technology model/variant |
| CACHE | 81 | Non-persistent cache/scratch storage available. Units as per DISK |
| SWAP | 85 | SWAP space storage available. Units as per DISK |
| NEW_FILES | 90 | Maximum supported/allowed individual file detailsnumber: maximum number of files created (if applicable)amount: maximum size of any individual files written or appended to        (in kibibytes)qualifier: a comment/explanation (optional) |
| OPEN_FILES | 91 | As per NEW_FILES, but pertaining to files opened(for reading or writing) |




<a name="computing_resource_scope.proto"/>
<p align="right"><a href="#top">Top</a></p>

## computing_resource_scope.proto




<a name="bom.computing_resource_scope.ComputingResourceScope"/>
### ComputingResourceScope
Scope of a computing resource; i.e. the level the resource is applicable.
e.g. a resource per process, per execution host or a job-wide shared.
resource etc

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| JOB | 2 | Generic shared task/job wide resource. |
| QUEUE | 3 | Resource global to a particular queue. More specific than JOB_WIDE. |
| SERVER | 4 | Resource global to a particular server/cluster.More specific than JOB_WIDE |
| CHUNK | 50 | Generic "sub-job" or execution host specific resource.Note: Resources specified in multiple distinct chunks may potentiallybe provided/provisioned on the same execution host if there is capacityand no other constraints |
| NODE | 55 | Resource available at a node level |
| PROCESS | 60 | Resource available per process spawned by the job |
| PROCESS_MPI | 61 | Resources available per MPI process |
| THREAD | 70 | Resources available per thread |
| THREAD_GPU | 71 | Resources available per GPU or GPU-like accelerator multiprocessingthread (e.g. CUDA) |




<a name="data_coverage_content_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## data_coverage_content_type.proto




<a name="bom.data_coverage_content_type.DataCoverageContentType"/>
### DataCoverageContentType
The coverage content type is an ISO codeList describing the general
content type of data

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| IMAGE | 2 | Meaningful numerical representation of a physical parameter that isnot the actual value of the physical parameter |
| THEMATIC_CLASSIFICATION | 3 | Value with no quantitative meaning, used to represent aphysical quantity |
| PHYSICAL_MEASUREMENT | 4 | Value in physical units of the quantity being measured |
| AUXILIARY_INFORMATION | 5 | Data, usually a physical measurement, used to support the calculationof another variable(e.g. grid of aerosol optical thickness used in the calculation of asea surface temperature product) |
| COORDINATE | 6 | Data used to provide coordinate axis values |
| MODEL_RESULT | 7 | Resources with values that are calculated using a model rather thanbeing observed or calculated from observations. |
| QUALITY_INFORMATION | 8 | Data used to characterize the quality of another variable |
| REFERENCE_INFORMATION | 9 | Reference information used to support the calculation of another variable(e.g. grids of latitude/longitude used to geolocate the physicalmeasurements) |
| AUXILIARY_DATA | 10 | Values of extraneous data |




<a name="dataset_action_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dataset_action_type.proto




<a name="bom.dataset_action_type.DatasetActionType"/>
### DatasetActionType
Actions/operations that can be performed on, with or in relation to a
dataset/document/resource.
Most entries from: ISO19115 code lists, see
https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115_and_19115-2_CodeList_Dictionaries#CI_DateTypeCode

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| CREATE | 2 | Resource created |
| PUBLISH | 3 | Resource issued/made available |
| REVISE | 4 | Resource updated or amended |
| REVIEW | 5 | Resource reviewed, e.g. manually checked |
| VALIDATE | 6 | Resource validated, generally an automated check |
| VERIFY | 7 | Resource verified |
| APPROVE | 8 | Resource approved at some gateway or by some authority |
| RELEASE | 9 | Resource released for external or public access |
| ACCESS | 10 | Resource accessed, as relevant in the context of this event message |
| ADOPT | 11 | Resource was adopted |
| DEPRECATE | 12 | Resource was deprecated |
| DISTRIBUTE | 13 | Resource was distributed |
| EXPIRE | 14 | Resource expired |
| IN_FORCE | 15 | Resource come into force |
| SUPERSEDED | 16 | Resource was superseded or replaced by another resource |
| REVOKE | 17 | Resource was revoked |
| REJECT | 18 | Resource was rejected |
| UNAVAILABLE | 19 | Resource became not available or obtainable |




<a name="dataset_compression_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dataset_compression_type.proto




<a name="bom.dataset_compression_type.DatasetCompressionType"/>
### DatasetCompressionType
General type of compression applied to a dataset.
Note interpolation and "reduce"/"aggregation" techniques are not considered
a form of compression for the purposes of DatasetCompressionType, even
though these techniques can result in reduced dataset sizes (or datasets
that may compress better). Instead these types of transformations are
considered to change the type of the data in the dataset.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| NONE | 2 | Dataset is uncompressed ("native" format) |
| LOSSLESS | 3 | Dataset is losslessly compressed ("native" data can be exactly restored) |
| NEAR_LOSSLESS | 4 | Dataset is compressed via techniques that are known to result inno significant degradation to the information content |
| LOSSY_MINIMAL | 5 | Some lossy compression algorithm has been used, the errorthe characteristics of which are thought to impact in a minimal way on thedata |
| LOSSY_MODERATE | 6 | More aggressive lossy compression settings, achieving a fairtrade-off between quality and size |
| LOSSY_AGGRESSIVE | 7 | Very aggressive lossy compression settings, used to conservebandwidth |
| PACKED | 10 | Data has been packing/rounding |
| THINNED | 11 | Data has been resampled to a coarser grid in one or more dimensions(e.g. reduced horizontal grid, subset of vertical levels,fewer time-steps) |




<a name="dataset_feature_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dataset_feature_type.proto




<a name="bom.dataset_feature_type.DatasetFeatureType"/>
### DatasetFeatureType
Dataset feature types describe arrangements of collections of
data (a set of measurements, analyses, forecasts etc), distinguished by
the geometry and topology of the collection.
Largely parallels CF Conventions Scientific Feature Types:
http://cfconventions.org/cf-conventions/cf-conventions.html#featureType
The most specific feature type should be chosen in the event of ambiguity.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| IMAGE | 2 |  |
| RADIAL | 3 | A set of data points in a two dimensional grid described by aconnected set of radials using polar coordinates(connected, 2D elevation, azimuth, distance; ordered time)/ Example: data from a fixed-position scanning radar or lidar |
| SWATH | 4 | A set of data points in a two dimensional grid, where eachcoordinate is connected and a function of 2 dimensions(connected, 2D x, y, z, t)Examples: a polar orbiting satellite, airborne or ship instrument. |
| STRUCTURED_GRID | 5 | Other cartesian, rectilinear or curvilinear grids(separable x, y, z, t) |
| UNSTRUCTURED_GRID | 6 | Other unstructured (tessellated) grids |
| HYBRID_GRID | 7 | Mix of structured and unstructured portions |
| MOVING_STRUCTURED_GRID | 8 | A structured grid that moves with time (or each t, separable x, y, z) |
| MOVING_UNSTRUCTURED_GRID | 9 |  |
| MOVING_HYBRID_GRID | 10 |  |
| POINT | 50 | A collection of one or more parameters, each parameter measured/valid ata single point in time and space. Includes point-cloud datasets.Examples: earthquake data, lightning dataNote: Each data point has no implied coordinate relationship to otherpoints.e.g. data(i) : x(i) y(i) t(i) |
| TIMESERIES | 51 | A time-series of data points at specified location(s)e.g. data(i,o) : x(i) y(i) t(i,o)Examples: Weather station data, idealized representation of moored buoysNote: sometimes referred to as as "STATION" data in meteorology |
| PROFILE | 52 | A set of data points along a vertical line for one or more locations(i.e. a vertical soundings) at fixed times.e.g. data(i,o) : x(i) y(i) z(i,o) t(i)Examples: Certain satellite profiles, vertical model soundings |
| TIMESERIES_PROFILE | 53 | A time-series of profile features at specified location(s).e.g. data(i,o) : x(i) y(i) t(i,o)Examples: Station profilers, idealized representations ofballoon soundingsNote: sometimes referred to as a "STATION_PROFILE" |
| TRAJECTORY | 54 | A set of data points along a 1D curve in time and spacee.g. data(i,o) : x(i,o) y(i,o) t(i,o)Examples: Aircraft data, ship data, drifting buoys |
| TRAJECTORY_PROFILE | 55 | A series of profile features located at points ordered along atrajectorydata(i,p,o) : x(i,p) y(i,p) z(i,p,o) t(i,p)Example: Ship soundingsNote: sometimes referred to as a "SECTION" |
| MIXED | 126 | The dataset is known to contain a mix of the above feature types.In this case, the mix is to be determined by inspection of eachvariable's feature type |
| OTHER | 127 | Use of OTHER is discouraged. Additional entries to this enumare preferred. |




<a name="dataset_production_context.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dataset_production_context.proto




<a name="bom.dataset_production_context.DatasetProductionContext"/>
### DatasetProductionContext
The context a dataset was generated under and should be interpreted
by upon receipt. The main purpose of this meta-data is to help distinguish
between data created as part of "normal" output of some system (e.g. a
routinely running forecast model) and more usual modes this system could
be made to run in to cater for particular purposes

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| NORMAL | 2 | Dataset created in a "normal" fashion with respect to the typical/valuable range of intended purposes of the system creating the dataset.e.g. a NWP "normal" routine or on-demand NWP forecast |
| SCENARIO | 3 | Dataset created as part of a hypothetical scenario/exercise of thesystem (not for or to support an actual real event).This data may be disseminated to 3rd parties as part of an exercise. |
| RETROSPECTIVE | 4 | A special retrospective dataset for systems that normally provide currentor forecast data. |
| TEST | 5 | Dataset is generated as part of an internal test of componentsinvolved in creation/manipulation/validation/verification. |
| REAL_SAMPLE | 6 | Dataset represents realistic sample data. |
| SYNTHETIC_SAMPLE | 7 | Dataset represents sample synthetic/mock data. |
| TRIAL | 8 | Dataset for a system being trialled. This is pertinent for example if thesystem producing this dataset has a stable "NORMAL" counterpart, but thisslightly modified system is being run in parallel for evaluation purposesas part of an end-user trial. |
| RESEARCH | 9 | Dataset for research or prototyping purposes |




<a name="data_time_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## data_time_type.proto




<a name="bom.data_time_type.DataTimeType"/>
### DataTimeType
Significance of a specified datetime involved in describing
the content of a dataset.
Generally used in the context of a reference time or validity
period for a series of observations, model outputs or other
calculations

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| ANALYSIS | 2 |  |
| NOMINAL_ANALYSIS | 3 |  |
| OBSERVATION | 4 | The datetime(s) represent times that a (near) real-time (varying)quantity was observed. |
| FORECAST | 5 | The datetime(s) represent model forecast times atwhich the data is valid |
| START_OF_FORECAST | 6 |  |
| VERIFYING_TIME_OF_FORECAST | 7 |  |
| MODEL_START | 20 | The datetime marking the start of some model/task/process thatlead to the generation of the dataset |
| START_OF_SEQUENCE | 21 | The start of a sequence of model runs or observations etc |
| VALIDITY | 22 | The datetime(s) represent validity times that are notOBSERVATIONs or FORECASTs |
| LAST_REVISION | 60 | When dataset was last revised |
| LAST_UPDATE | 61 | When dataset was last updated |
| NEXT_UPDATE | 62 | When dataset will next be updated |
| VALIDITY_BEGINS | 63 | When the data/resource is considered to become valid.NOTE: There could be quite a delay between creation and validity begins |
| VALIDITY_EXPIRES | 64 | When the data/resource is no longer considered to be valid |




<a name="debug_level.proto"/>
<p align="right"><a href="#top">Top</a></p>

## debug_level.proto




<a name="bom.debug_level.DebugLevel"/>
### DebugLevel
The debug level in the context of a software or hardware application/system
of the detail level in a log of such a system. 
Note: debug and trace levels are often related, but are distinct
concepts in some systems

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| NONE | 2 |  |
| BRIEF | 3 |  |
| NORMAL | 4 |  |
| VERBOSE | 5 |  |
| VERY_VERBOSE | 6 |  |
| ALL | 7 |  |




<a name="error_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## error_type.proto




<a name="bom.error_type.ErrorType"/>
### ErrorType
Task, service, process, model or other program error types.
Sometimes multiple error codes may apply. Services should return
the most specific error code that applies. For example, prefer
OUT_OF_RANGE over FAILED_PRECONDITION if both codes apply.
Similarly prefer NOT_FOUND or ALREADY_EXISTS over FAILED_PRECONDITION.
This list is inspired by TensorFlow's error_codes.proto (APACHE2 license)

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| INSTABILITY | 2 | Model became numerically unstable and crashed |
| SYNTAX | 3 |  |
| CONFIGURATION | 4 |  |
| BAD_REQUEST | 5 | Improperly-formatted request can't be fulfilled. |
| DATA_LOSS | 6 | Data loss or truncated file |
| DATA_SECURITY | 7 | Security validation of data failed, or sufficiently concerning tobe considered a security issue. Includes data not matching a hash orsigned digital fingerprint, invalid sequencing of data that suggestspossible tampering/man-in-the-middle attacks etc |
| DATA_INTEGRITY | 8 | Data fails an integrity test that is likely to be a data corruptionissue rather than due to a security threat |
| DATA_INVALID | 9 | Task involved in parsing invalid data. Note that this differsfrom FAILED_PRECONDITION. DATA_INVALID indicates inputsthat are problematic regardless of the state of the system(e.g., a malformed file name, invalid file type, input arguments etc)e.g. invalid input data |
| ID_EXISTS | 10 | e.g. assigned a duplicate ID/hash when they need to be unique |
| DEADLINE_EXCEEDED | 11 | Deadline expired before operation could complete.  For operationsthat change the state of the system, this error may be returnedeven if the operation has completed successfully.  For example, asuccessful response from a server could have been delayed longenough for the deadline to expire. |
| NOT_FOUND | 12 | Some requested entity (e.g., file or directory) was not found or arequired resource is missing |
| ALREADY_EXISTS | 13 | Creation of some entity (e.g., file or directory) is found toalready exist |
| UNAUTHORIZED | 14 | Authorization request failed |
| PERMISSION_DENIED | 15 | Insufficient permissions to execute the specifiedoperation.  PERMISSION_DENIED must not be used for rejectionscaused by exhausting some resource (use RESOURCE_EXHAUSTEDinstead for those errors). |
| SECURITY_VIOLATION | 16 |  |
| RESOURCE_EXHAUSTED | 17 | Some resource has been exhausted or a resource limit exceeded.e.g. a per-account disk quota or a file system running out of space. |
| TIMEOUT | 18 | A time-out error |
| ADDRESS_LOOKUP_ERROR | 19 | Unable to resolve an address/connection |
| RATE_LIMITED | 20 | Connection dropped due to a rate limit |
| UNAVAILABLE | 21 | A service is unavailable. This is a most likely a transientcondition and may be corrected by retrying with a backoff. |
| CONNECTION | 22 | Connection refused or dropped/aborted for other reasons |
| OUT_OF_RANGE | 23 | Operation tried to iterate past the valid input range.  E.g., seeking orreading past end of file.Unlike DATA_INVALID or DATA_LOSS, this error indicates a problem that maybe fixed if the system state changes. For example, a 32-bit filesystem will generate INVALID_ARGUMENT if asked to read at anoffset that is not in the range [0,2^32-1], but it will generateOUT_OF_RANGE if asked to read from an offset past the currentfile size. |
| FAILED_PRECONDITION | 24 | Operation was rejected because the system is not in a staterequired for the operation's execution.  For example, directoryto be deleted may be non-empty, an rmdir operation is applied toa non-directory, etc.A litmus test that may help a service implementer in decidingbetween FAILED_PRECONDITION, ABORTED, and UNAVAILABLE: (a) Use UNAVAILABLE if a client can retry just the failing call. (b) Use ABORTED if the client should retry at a higher-level     (e.g., restarting a read-modify-write sequence). (c) Use FAILED_PRECONDITION if the client should not retry until     the system state has been explicitly fixed.  E.g., if an "rmdir"     fails because the directory is non-empty, FAILED_PRECONDITION     should be returned since the client should not retry unless     they have first fixed up the directory by deleting files from it. (d) Use FAILED_PRECONDITION if the client performs conditional     REST Get/Update/Delete on a resource and the resource on the     server does not match the condition. E.g., conflicting     read-modify-write on the same resource. |
| ABORTED | 25 | The operation was aborted, typically due to a concurrency issuelike sequencer check failures, transaction aborts, etc.See litmus test above for deciding between FAILED_PRECONDITION,ABORTED, and UNAVAILABLE. |
| SEGFAULT | 26 |  |
| MEMORY | 27 | Memory allocation error, bus error, invalid/double free |
| MISSING_COMMAND | 28 | Command, alias or action type not found or known |
| NOT_IMPLEMENTED | 29 | Attempted invocation of an unimplemented method/function/command |
| DEPENDENCY_ERROR | 30 | Generic error due to a missing high-level dependency |
| DEAD_NODE | 31 | A required node was found to be dead or died during.Includes the situation when a multi-node job aborts due to one dead node. |
| IO | 32 | Other I/O errors not covered by previous entries (e.g. file unexpectedlyalready in use) |
| TRAP | 33 | Unhandled trap/signal/interrupt |
| BROKEN_PIPE | 34 |  |
| WRONG_TYPE | 35 | Program internal operation applied to an inappropriate type |
| ARITHMETIC | 36 | Program overflow, zero division, floating-point error |
| LOOKUP | 37 | Program internal index error, key error or similar |
| OS | 38 | Failure caused by a operating system error |
| OTHER | 127 | Error type assessed but does not fit into any other category defined here |




<a name="impact.proto"/>
<p align="right"><a href="#top">Top</a></p>

## impact.proto




<a name="bom.impact.Impact"/>
### Impact
Level of impact based on an assessment of the importance of a
suite/system/component/task, especially in the context of the
organisation-wide impact of a sustained outage.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| NONE | 2 | Of effectively no impact |
| VERY_LOW | 3 | Limited impact |
| LOW | 4 |  |
| NORMAL | 5 |  |
| MODERATE | 6 |  |
| HIGH | 7 |  |
| VERY_HIGH | 8 |  |
| CRITICAL | 9 | Extremely important, extensive "shared-fate" risk between multiplehighly important or sensitive systems |




<a name="job_array_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## job_array_type.proto




<a name="bom.job_array_type.JobArrayType"/>
### JobArrayType
Job array type (usually a batch-scheduler concept)

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| NOT_ARRAY | 2 | Not an array job nor subjob |
| IS_ARRAY | 3 | Is an array job |
| IS_ARRAY_SINGLE | 4 | A single subjob |
| IS_ARRAY_RANGE | 5 |  |




<a name="log_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## log_type.proto




<a name="bom.log_type.LogType"/>
### LogType
LogType allows categorisation of logs into general types based
on the type of information logged and/or the intent of the log.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| OUT | 2 | General stdout or info-level information |
| ERROR | 3 | For errors or for stderr |
| WARNING | 4 | Log for warnings, if applicable |
| TRACE | 5 | Log for additional trace-level output |
| SUBMIT | 6 | Task submission log |
| PID | 7 | Log for tracking tracking process ids or similar |
| TRANSACTION | 8 | Transactional or commit logs |
| CHECKPOINT | 9 | Checkpoint/snapshot files - generally self-contained files sufficientto allow resumption of running from that point/state |
| SCHEDULER | 10 | Log of job manager/scheduler/workflow or similar |
| ACCESS | 11 | Resource access type logs |
| MESSAGE | 12 | Logs that record conversations or similar |
| AUDIT | 13 | An audit log may contain a mix of information for audit purposes, e.g.user login/logoff, expired user sessions, output delivery times etc |
| AUTHENTICATION | 14 | Authentication related logs |
| SECURITY | 15 | Security warning log |
| SESSION | 16 | Session activities for components/services associated with user requests |
| PRODUCT | 17 | Log out generated/published outputs/products |
| EVENT | 18 | General event log |




<a name="maturity.proto"/>
<p align="right"><a href="#top">Top</a></p>

## maturity.proto




<a name="bom.maturity.Maturity"/>
### Maturity
Maturity is based on the "Data Stewardship Maturity Matrix (DSMM)"
Refer to: http://doi.org/10.2481/dsj.14-049
Note: INTERMEDIATE is the recommended minimal level for Operational
      products stewarded by NCEI/CICS-NC/NOAA National Data Centres

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| AD_HOC | 2 | Not managed |
| MINIMAL | 3 | Limited management |
| INTERMEDIATE | 4 | Managed, defined, partially implemented |
| ADVANCED | 5 | Managed, well-defined, fully implemented, partially verified |
| OPTIMAL | 6 | OPTIMAL: managed, well-defined, fully implemented, measured, controlled  &verified/audited |




<a name="prod_status.proto"/>
<p align="right"><a href="#top">Top</a></p>

## prod_status.proto




<a name="bom.prod_status.ProdStatus"/>
### ProdStatus
The operational/production status of a system. This mainly relates to
the degree of support for the system along with the environment in which
it is running

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| CAT1 | 2 | Production, CAT1 support |
| CAT2 | 3 | Production, CAT2 support |
| CAT3 | 4 | Production, CAT3 support |
| PRODUCTION_CONDITIONAL | 5 | Production, but support arrangements are |
| PRODUCTION_TEST | 6 | Production test product |
| PRODUCTION_OTHER | 7 | Production but support arrangements are not specified |
| PREOPERATIONAL | 8 | Stable, running in stage or being trialled in prod |
| STAGING | 9 | Trial runs in a staging environment |
| DEVELOPMENT | 10 | Test runs in development environment |
| RESEARCH | 11 | Experimental system |
| EXTERNAL | 12 | Service provided by external vendor with unknown guarantees |




<a name="realm.proto"/>
<p align="right"><a href="#top">Top</a></p>

## realm.proto




<a name="bom.realm.Realm"/>
### Realm
The production realm of a device/machine/cluster hosting the component.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| RESEARCH | 2 | A R&D environment that is separate to the official dev/stage/prodenvironments. |
| DEV | 3 |  |
| STAGE | 4 |  |
| PROD | 5 |  |
| EXTERNAL | 6 |  |




<a name="security_classification.proto"/>
<p align="right"><a href="#top">Top</a></p>

## security_classification.proto




<a name="bom.security_classification.SecurityClassification"/>
### SecurityClassification


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| UNCLASSIFIED | 2 | Security Classifications |
| PROTECTED | 3 |  |
| CONFIDENTIAL | 4 |  |
| SECRET | 5 |  |
| TOP_SECRET | 6 |  |




<a name="security_delimiting_marker.proto"/>
<p align="right"><a href="#top">Top</a></p>

## security_delimiting_marker.proto




<a name="bom.security_delimiting_marker.SecurityDelimitingMarker"/>
### SecurityDelimitingMarker
Dissemination Limiting Marker

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| UNCLASSIFIED | 2 |  |
| FOR_OFFICIAL_USE_ONLY | 3 |  |
| SENSITIVE | 4 |  |
| SENSITIVE_PERSONAL | 5 |  |
| SENSITIVE_LEGAL | 6 |  |
| SENSITIVE_CABINET | 7 |  |




<a name="severity.proto"/>
<p align="right"><a href="#top">Top</a></p>

## severity.proto




<a name="bom.severity.Severity"/>
### Severity
Inspired from: https://en.wikipedia.org/wiki/Syslog
The meaning of severity levels other than Emergency and Debug are relative
to the application. For example, if the purpose of the system is to
process transactions to update customer account balance information, an
error in the final step should be assigned Alert level. However, an error
occurring in an attempt to display the ZIP code of the customer may be
assigned Error or even Warning level.
The server process which handles the message (syslogd) usually includes
all lower (more severe) levels. That is, if messages are separated by
individual severity, a Warning level entry will also be included in Notice,
Info and Debug processing.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| DEBUG | 2 | Information is useful for debug purposes |
| TRACE | 3 | Debug information at a finer-grained level that DEBUG |
| INFO | 4 | Routine information, such as ongoing status or performance. |
| NORMAL | 5 | Normal but possibly more useful information that INFO. |
| NOTICE | 6 | Normal but significant conditions, such as start-up, shut-down, or aconfiguration change. May require investigation or special handlingin some cases. |
| WARNING | 7 | Warning events might cause problems. |
| ERROR | 8 | Error conditions, likely to cause problems, but not necessarily fatal |
| CRITICAL | 9 | A critical condition, likely to cause more severe problems or outages.e.g. task failure without retry, hard device errors etc |
| ALERT | 10 | A condition to be corrected immediately, such as a corrupted database,operational suite daemon failure |
| EMERGENCY | 11 | One or more systems are unusable. Panic condition. |




<a name="system_actor_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## system_actor_type.proto




<a name="bom.system_actor_type.SystemActorType"/>
### SystemActorType
Type of entity involved in some interaction with a system, task or similar.
For example, this type can be used to represent the entity
responsible for initiating the running of a task/process, the
entity/system reporting a change in state of a system or the type
of entity responsible for imposing/enforcing resource limits.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| USER | 2 |  |
| OPERATOR | 3 | An operator corresponds to an operational user with responsibility forhelping to manage a particular system. Has the same or higher privilegesthan USER-level but with additional operational responsibilities. |
| ADMIN | 4 |  |
| SELF | 5 | The entity which the interaction occurs (system, task) |
| SIMILAR | 6 | Another entity, similar to this entity that is also managedin a similar way to this entity |
| HOST_SYSTEM | 10 | Host system could be a physical machine, VM, container etc |
| BATCH_SCHEDULER | 11 |  |
| WORKFLOW_SCHEDULER | 12 |  |
| ORCHESTRATION_SYSTEM | 13 |  |
| SECURITY_SYSTEM | 20 |  |
| AUTHENTICATION_SYSTEM | 21 |  |




<a name="task_communication_method.proto"/>
<p align="right"><a href="#top">Top</a></p>

## task_communication_method.proto




<a name="bom.task_communication_method.TaskCommunicationMethod"/>
### TaskCommunicationMethod
The basic method of communication used by a task to indicate
a change in task status.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| EVENT | 2 | The task or the environment the task is running insignals back task status updates as events |
| RPC | 3 | RPC here represents a persistent and direct two-way connection betweenthe task or a process spawned by the task and a task manager vianetwork ports or similar mechanism |
| POLL | 4 | A task manager related component or diagnostic process pollsthe task's execution status or outputs of the task (e.g. log files) |




<a name="task_interaction_type.proto"/>
<p align="right"><a href="#top">Top</a></p>

## task_interaction_type.proto




<a name="bom.task_interaction_type.TaskInteractionType"/>
### TaskInteractionType
Interaction with a task performed by a user or system.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| READY | 2 | Put task in a ready state |
| QUEUE | 3 | Queue task |
| SUBMIT | 4 | Submit task for running |
| RUN | 5 | Directly run the task |
| RETRY | 6 | Retry a failed task |
| CONFIG_EDIT_RUN | 7 | Submit routine task with modified configuration |
| EDIT_RUN | 8 | Submit routine task with modified task content/logic |
| PREVALIDATE | 9 | Run a task check/validation step (e.g. syntax check) |
| PREPROCESS | 10 | Run a task preprocessing step (e.g. SMS preprocesor) |
| POSTVALIDATE | 11 | Run a final validation step on the task |
| HOLD | 12 | Hold job before execution/job submission |
| RELEASE | 13 | Release a hold |
| SUSPEND | 14 | Suspend task during execution |
| RESUME | 15 | Suspend task during execution |
| CONTINUE | 16 | Continue a task that is running but blocked |
| STOP | 17 | Stop or shutdown a running task in nice way |
| KILL | 18 | Kill a running task |
| ADD | 19 | This task was newly added/defined (e.g. to a workflow) |
| DELETE | 20 | This task was deleted/dropped (e.g. from a workflow) |
| MODIFY_CONFIG | 21 | Update a task config in a persistent fashion |
| MODIFY | 22 | Update a task content/logic in a persistent fashion |
| SET_COMPLETE | 23 | The task is forced to be successfully completed |
| SET_ABORTED | 24 | The task is forced to be in an error state |
| SKIP | 25 | Skip running the task |
| EXPIRE | 26 | Force the task to be put into an expired state. Usually an expiredstate implies a hard deadline was reached before the task executedor finished |
| DEFER | 27 | Delay running of the task |
| REMOVE_DEPENDENCY | 28 | Remove a task triggering condition |
| ADD_DEPENDENCY | 29 | Add a task triggering condition |
| DELAY | 30 | Delay the scheduled execution of a task by some time duration. |
| BRING_FORWARD | 31 | Bring forward the scheduled execution of a task by some time duration. |
| RESURRECT | 32 | Attempt to resurrect a task |
| MIGRATE | 33 | Migrate this task to another environment/scheduler |
| REFRESH | 34 | Attempt to force a task to reload/refresh it's state/configuration |
| DEBUG | 35 | Perform a debugging operation on the task, or activate adebug or trace mode |
| CHECKPOINT | 36 | Ask a model or system run by a task to create checkpoint |
| RESTORE | 37 | Restore a task/system/model from a saved state |
| REPRIORITISE | 38 | Change task urgency/priority |
| UPDATE_LIMIT | 39 | Change task resource limit(s) or other constraints |
| IGNORE | 127 | Ignore and do nothing |




<a name="task_property.proto"/>
<p align="right"><a href="#top">Top</a></p>

## task_property.proto




<a name="bom.task_property.TaskProperty"/>
### TaskProperty
A property a task can have

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| IDEMPOTENT | 2 | Are repeated re-runs of the task (even following a crash during taskexecution) safe and expected to produce the same outcome? |
| NOT_RERUNNABLE | 3 | Is the task specifically _not_ allowed to be automatically re-run forany reason? For example, known or suspected to not be IDEMPOTENT |
| RESERVATION | 4 | Does this task/job actually represent a reservation request job for abatch scheduler? |
| CHECKPOINTABLE | 5 | Set if this task supports "checkpointing" via some mechanism in the eventit is necessary. For example a task that is able to checkpoint prior toa system shut-down when it receives an appropriate signal in advance. |
| CHECKPOINTED_REGULAR | 6 | Set if this task is expected to be "checkpointed" automaticallyduring execution, from which the task could be resumed/restarted |
| ARRAY | 20 | Is an array job |
| ARRAY_SINGLE | 21 | A single subjob |
| ARRAY_RANGE | 22 |  |
| EXPECTED_TO_FAIL | 40 | Task is expected to fail, perhaps as part of some test suite. |
| EDITRUN_CONFIG | 70 | Manual "edit-run" performed where it is known only a "controlled" set oftask settings/configuration items have been adjusted |
| EDITRUN | 71 | Manual "edit-run" performed where any task changes may have been made |
| RUNMODE_TEST | 80 | Task is run in a test mode (what this means is specific to each task,e.g. a task run in this mode might run a set of unit tests that arenormally not run routinely in production. |
| RUNMODE_DUMMY | 81 | Task is a dummy task, usually a simple "sleep" type task |




<a name="task_state.proto"/>
<p align="right"><a href="#top">Top</a></p>

## task_state.proto




<a name="bom.task_state.TaskState"/>
### TaskState
Task state. Many states represented by TaskState won't
be applicable to most systems or may represent intermediate states
that are not tracked. Please choose an appropriate subset on
a workflow/batch system by system basis. More specific states are
preferred over their generic counterparts.
Note: a late task is represented by setting a late time duration in
the TaskStatus message; e.g. a task may have a TaskState of WAITING or
RETRYING and also be late

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 | Unknown/indeterminate state |
| CREATED | 2 | Newly created task |
| PREVALIDATING | 3 | Task configuration/content is being validated beforeor as part of a workflow, dispatch, submit or pre-run process |
| PREVALIDATING_FAIL | 4 | Pre-validation step failed |
| INVALID | 5 | Task found to be invalid prior to execution |
| DORMANT | 6 | Task proxy exists in a scheduler but is not currently in aconfiguration that permits it to be progressed to a waiting, queued orrun state |
| WAITING | 9 | Generic waiting state (waiting on one more conditions to be met). Better qualified waiting states follow below |
| WAITING_TIME | 10 | Waiting purely on a time condition |
| WAITING_PRECONDITIONS | 11 | Waiting on trigger(s)/event(s)/pre-condition(s) to be set/satisfied priorto execution. This includes a mix of a temporal trigger and otherdependencies. |
| WAITING_RUNAHEAD | 12 | Task is eligible to run (normal pre-conditions have been met) butis will not yet be submitted/executed due to a "runahead" restrictionwhich is a limit imposed on many cycles ahead/ tasks from a cycling suiteare permitted to run. |
| WAITING_QUEUE | 13 | Job waiting in a queue or is part of some group or allocation that hasreached a constraint/limit (e.g. there may be a maximum number of jobs aspecific user can run per day). |
| WAITING_RESOURCES | 14 | The resources requested by the job do not currently exist in an availablestate (e.g. they are busy, reserved or temporarily offline). |
| WAITING_AUTHORISATION | 15 | The task is ready to run pending an authorisation step (e.g. awaiting approval of an operator via a GUI) |
| HELD | 18 | Generic held/on-hold state. Better qualified held states follow below.Note: if HELD state is due to an administrator's actions,set state = HELD and TaskStatus.state_actor.system_actor_type = ADMIN.Similar possibilities exist for USER and OPERATOR holds. |
| HELD_BY_SYSTEM | 19 | System-level or resource-manager job hold. |
| HELD_BY_RESOURCES | 20 | The resources requested by the job do not currently exist in an availablestate and this is treated as a hold rather than a waiting(WAITING_RESOURCES) state. This is more specific than HELD_BY_SYSTEM. |
| DROPPED | 23 | Job deleted from queue by user before execution, or task/task-definitiondropped/omitted from scheduler prior to job submission.Note: if DROPPED state is due to action carried out by the job/taskuser/owner, then this can be indicated by setting state = DROPPED andTaskStatus.state_actor.system_actor_type = USER. |
| PREPROCESSING | 24 | In a task pre-processing step, probably run as part of theworkflow scheduler |
| PREPROCESSING_FAIL | 25 |  |
| PREPROCESSING_SUCCESS | 26 | Successful completion of a task preprocessing stage |
| QUEUED | 29 | Queued/getting ready to run |
| READY | 30 | Ready to run/submit, not waiting and not held |
| EXPIRED | 31 | A deadline has been passed and this task won't be completed |
| SUBMITTING | 35 | The task/job has is in the process of being submitted/dispatched |
| SUBMIT_SUCCESS | 36 | The task has been successfully submitted/dispatched |
| SUBMIT_FAIL | 37 | The task submit process failed or was killed before the start of taskexecution |
| SUBMIT_TIMEOUT | 38 | The task submit process appeared to hang/timed-out. |
| SUBMIT_RETRYING | 39 | As per SUBMIT_FAIL or SUBMIT_TIMEOUT but a resubmit (possibly after aconfigured delay) will be attempted automatically |
| REJECTED | 41 | Task rejected by batch scheduler or a security layer prior to execution |
| PREJOB | 42 | Running a pre-job/setup step, prior to execution of core task |
| PREJOB_FAIL | 43 |  |
| PREJOB_SUCCESS | 44 | Successful completion of the pre-job step(s) |
| AUTHENTICATING | 45 |  |
| AUTHENTICATE_SUCCESS | 46 |  |
| AUTHENTICATE_FAIL | 47 |  |
| AUTHENTICATE_TIMEOUT | 48 |  |
| STARTED | 50 | Task started running/reported commencement of execution,sometimes referred to as the "BEGUN" state |
| PROGRESS | 51 | Task in progress (used for possible progress updates) |
| ENV_SETUP | 52 | Environment setup, if distinct from PREJOB and INITIALISING phases. |
| ENV_SETUP_SUCCESS | 53 | Environment setup completed successfully. |
| ENV_SETUP_FAIL | 54 |  |
| INITIALISING | 55 | Following execution, task has reached an initialisation phase. |
| INITIALISE_SUCCESS | 56 | INITIALISING phase has been successfully completed |
| INITIALISE_FAIL | 57 |  |
| SUCCESS | 58 | Task appears to have concluded normally & successfully |
| STOPPED | 59 | Task stopped mid execution as part of workflow design |
| PAUSING | 60 | Task execution in process of pausing |
| PAUSED | 61 | Task execution paused; task still memory/process resident (not vacated) |
| PAUSE_FAIL | 62 | Pausing the task failed |
| PROMPTING | 63 | Task, during the course of execution, is requesting/promptingfor additional interactive input or authorisation |
| SUSPENDING | 64 | Task in the process of suspending. Usually used as a mechanismto free up resources for other higher priority jobs in a batch schedulercontext which usually involves some sort of snap-shotting of task stateand temporarily stopping task execution.Sometimes referred to as task vacating, a task vacation or job preemption. |
| SUSPENDED | 65 | Task suspended/vacated and needs to be resumed to progress/complete. |
| SUSPEND_FAIL | 66 | Suspending/vacating the task failed |
| SUSPEND_TIMEOUT | 67 | Suspending failed due to hanging or taking too long |
| CHECKPOINTING | 68 | Job/task is in the process of creating checkpoint |
| CHECKPOINT_SUCCESS | 69 |  |
| CHECKPOINT_FAIL | 70 | Failure during check-pointing |
| RESTORING | 72 | Restoring/resuming from a check-point or other saved state |
| RESTORE_FAIL | 73 |  |
| RESTORE_SUCCESS | 74 |  |
| POSTJOB | 76 | Running a post-job/clean step. Note: if prior task |
| POSTJOB_FAIL | 77 |  |
| POSTVALIDATING | 79 | Running a validation step as part of the task following execution |
| POSTVALIDATING_FAIL | 80 |  |
| ERROR_HANDLING | 82 | Task is in the process of handling an error |
| ERROR_HANDLING_SUCCESS | 83 | Task successfully handled an error |
| ERROR_HANDLING_FAIL | 84 | Failure during task error handling step |
| EXITING | 85 | Job is exiting after having run (normally in a batch scheduler context). |
| RETRYING | 86 | Retrying after having previously progressed to some |
| FAILED | 87 | Task failed (desired outcome of the task was not reached) |
| RETRY_LIMIT_REACHED | 88 | Multiple task retries have all failed. This is a failed state. |
| ABNORMAL_SUCCESS | 89 | Diagnostics suggest task appears to have succeededbut some warnings/errors/abnormalities were encountered |
| WARNING | 90 | Task is reporting a warning during execution but has notfinished. This is a potential intermediate state of a task:If it succeeds ABNORMAL_SUCCESS should be reported.If it fails one of the many failure modes should be reported. |
| ERROR_WITH_CONTINUATION | 91 | An error was found during execution but task is continuing. |
| KILLING | 93 | An attempt at killing the task has taken place |
| KILLING_FAIL | 94 | An attempt at killing the task has apparently failed |
| KILLING_TIMEOUT | 95 | An attempt at killing the task has apparently hung/timed-out and maynot have taken effect |
| KILLED_BY_COMMAND | 96 | For example via kill or qdel |
| KILLED_BY_TIME_LIMIT | 97 |  |
| KILLED_BY_CPU_LIMIT | 98 |  |
| KILLED_BY_MEMORY_LIMIT | 99 |  |
| KILLED_BY_PROCESS_LIMIT | 100 |  |
| KILLED_BY_FILE_SIZE_LIMIT | 101 |  |
| KILLED_BY_FILE_NUMBER_LIMIT | 102 |  |
| KILLED_BY_SECURITY_POLICY | 103 |  |
| KILLED | 106 | Killed by another or unspecified mechanism |
| CANCELLED | 107 | Program/model run cancelled during execution via some mechanism otherthan kill or a retry limit |
| SKIPPED | 110 | Task to be skipped |
| MIGRATING | 111 | Job control responsibility is being migrated to another system |
| MIGRATED | 112 |  |
| MIGRATING_FAIL | 113 |  |
| TRANSIT | 114 | The job/task itself is in the process of being routed or moved to a newdestination |
| TRANSIT_SUCCESS | 115 |  |
| TRANSIT_FAIL | 116 |  |
| BLOCKED | 117 | Task is executing but progress is blocked |
| HUNG | 118 | Execution has hung and become unresponsive. |
| UNREACHABLE | 119 | Attempts to determine task state have failed (e.g. network outage).It is unknown if the task is still running or not |
| LOST | 120 | Attempts to track a task have failed and it is now consideredlost by this system. |
| ZOMBIE | 121 | Process has become a zombie (process is still running but is becomedetached in some way from the managing process) |
| RESURRECTING | 122 | Resurrecting is the process of restoring a ZOMBIE or possibly apreviously UNREACHABLE task (or, from a workflow scheduler perspective,even a task that was hard killed by a resource manager then laterrestarted) to a "normal" task |
| RESURRECTED | 123 |  |
| RESURRECT_FAIL | 124 |  |
| FORCE_COMPLETED | 125 | Task forced to be in a completed state from the perspective of ascheduler/job manager. It may in-fact never have run ormay still be running if it had previously launched. |
| MODEL_STOP | 127 | Model progress was stopped by a model mechanism, for example numericalconvergence thresholds were not met. |
| LICENSE_ACQUISITION | 333 | If the task/job needs to acquire a license to execute (at the task orsub-task level) then it may be useful to track the license acquisitionphase: |
| LICENSE_ACQUISITION_SUCCESS | 334 |  |
| LICENSE_ACQUISITION_FAIL | 335 |  |
| LICENSE_ACQUISITION_TIMEOUT | 336 |  |




<a name="trace_level.proto"/>
<p align="right"><a href="#top">Top</a></p>

## trace_level.proto




<a name="bom.trace_level.TraceLevel"/>
### TraceLevel
The trace level in the context of a software or hardware
application/system of the corresponding detail level in a
log of such a system. Note: Trace and debug levels are often
related but are distinct concepts in some systems.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNSET | 0 |  |
| UNKNOWN | 1 |  |
| NO_TRACE | 2 |  |
| SOFTWARE_TRACE | 3 |  |
| HARDWARE_TRACE | 4 |  |
| FULL_TRACE | 5 |  |





<a name="scalar-value-types"/>
## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double"/> double |  | double | double | float |
| <a name="float"/> float |  | float | float | float |
| <a name="int32"/> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64"/> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32"/> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64"/> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32"/> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64"/> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32"/> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64"/> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32"/> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64"/> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool"/> bool |  | bool | boolean | boolean |
| <a name="string"/> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes"/> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |
