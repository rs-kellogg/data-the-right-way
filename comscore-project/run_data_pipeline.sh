#!/usr/bin/bash

if [[ "$1" != "" ]]; then
    PROFILE="$1"
else
    PROFILE="default"
fi

echo "The AWS profile is set to: $PROFILE"

python main.py run-daily ${PROFILE} comscore-filter.jinja 2019-01-01 2019-01-03 --dir ./output/logs
aws s3 sync s3://kdc-comscore/parquet-extracts ./output/parquet --profile ${PROFILE}
python main.py create-plots ./output/parquet/url_domain_twitch/ --dir ./output/plots/
pytest tests
