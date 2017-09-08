#!/usr/bin/bash

ROOT=$( cd $( dirname $0 ); pwd; )

PP=build/generated/source/proto/main/python

export PYTHONPATH=$ROOT/$PP:$ROOT/$PP/common:$ROOT/$PP/common/enums

python $ROOT/src/python/test_TaskEvent.py
