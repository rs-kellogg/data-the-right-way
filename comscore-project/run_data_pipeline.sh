#!/usr/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'ERROR: provide the AWS profile name to use'
    exit 1
fi

python main.py ${1} comscore-filter.jinja 2019-01-01 2019-01-03 --dir ./output/logs
aws s3 sync s3://kdc-comscore/parquet-extracts ./output/parquet --profile ${1}
pytest tests
