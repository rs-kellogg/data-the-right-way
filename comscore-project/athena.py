import boto3
import datetime as dt
import time
import jinja2
from typing import Dict, List, Tuple
from rich import console as cons


# -----------------------------------------------------------------------------
console = cons.Console(style="green on black")


# -----------------------------------------------------------------------------
def gen_dates(start_date: dt.datetime, end_date: dt.datetime) -> List:
    num_days = (end_date - start_date).days + 1
    dates = [start_date + dt.timedelta(days=i) for i in range(num_days)]
    return [(str(d.year), str(d.month).zfill(2), str(d.day).zfill(2)) for d in dates]


# -----------------------------------------------------------------------------
def remove_completed_jobs(
    client, 
    jobs: List, 
    results: List, 
    test_run: bool, 
    sec_delay: int = 1
) -> None:
    completed = []
    if test_run:
        while jobs:
            jobs.pop()
        return
    for d, resp in jobs:
        res = client.get_query_execution(QueryExecutionId=resp['QueryExecutionId'])
        if res['QueryExecution']['Status']['State'] not in ("QUEUED", "RUNNING"):
            results.append((d, res))
            completed.append(d)

    for d in completed:
        for j in jobs:
            if j[0] == d:
                jobs.remove(j)
                break

    if len(completed) > 0:
        console.print(f">>> Running: {len(jobs)}, Completed: {len(results)}")

    time.sleep(sec_delay)


# -----------------------------------------------------------------------------
def run_day(client, template, args, database, d) -> Tuple:
    args["year"] = d[0]
    args["month"] = d[1]
    args["day"] = d[2]
    sql = template.render(args)
    console.print(f"{d}: STARTED")
    return d, client.start_query_execution(
            QueryString=sql, 
            QueryExecutionContext={
                'Database':database,
            }
        )


# -----------------------------------------------------------------------------
def run_daily(
    profile,
    region,
    template: jinja2.environment.Template,
    start_date: dt.datetime,
    end_date: dt.datetime,
    database: str,
    batch_size: int = 50,
    args: Dict[str, str] = None,
) -> List:
    # create athena client
    session = boto3.Session(profile_name=profile, region_name=region)
    client = session.client('athena')
    
    # generate the list of dates from start to end
    remaining_dates: List = gen_dates(start_date, end_date)

    # check for valid parameters
    assert batch_size <= 100
    assert start_date <= end_date
    assert len(remaining_dates) <= 1000

    # display message to user
    console.print(f"#" * 80)
    console.print(f"# executing for date range: {remaining_dates[0]} -> {remaining_dates[-1]}")
    console.print(f"#" * 80)

    # results indexed by date
    results: List = []

    # job ids indexed by date
    running: List = []

    # initialize running jobs up to batch size or number of jobs requested
    for i in range(min(batch_size, len(remaining_dates))):
        running.append(run_day(client, template, args, database, remaining_dates.pop(0)))

    # keep adding jobs until no more are left
    while len(remaining_dates) > 0:
        if len(running) < batch_size:
            for i in range(min(len(remaining_dates), batch_size - len(running))):
                running.append(
                    run_day(client, template, args, database, remaining_dates.pop(0))
                )
        remove_completed_jobs(client, running, results, test_run=False)

    # wait until remaining jobs are completed
    while len(running) > 0:
        remove_completed_jobs(client, running, results, test_run=False)

    # results indexed by date
    return results
