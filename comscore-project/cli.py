import typer
import csv
import pandas as pd
from pathlib import Path
from rich import console as cons
from typing import Dict, Optional
import datetime as dt
from jinja2 import Environment, BaseLoader
from wrangler.aws import aws_sso, athena


# -----------------------------------------------------------------------------
app = typer.Typer()
console = cons.Console(style="green on black")
CONFIG: Dict[str, str] = {}


# -----------------------------------------------------------------------------
@app.command()
def set_profile_credentials(
    profile: str = typer.Argument(..., help="Profile name"),
):
    aws_sso.set_profile_credentials(profile)


# -----------------------------------------------------------------------------
@app.command()
def run_daily_sql_query(
    template_file: Path = typer.Argument(..., help="SQL template file path"),
    start_date: str = typer.Argument(..., help="start date in format yyyy-mmm-dd"),
    end_date: str = typer.Argument(..., help="end date in format yyyy-mmm-dd"),
    out_dir: Optional[Path] = typer.Option(
        Path("."),
        "--dir",
        help="The directory where the output output files will be created. Defaults to the current working directory",
    ),
):
    profile = CONFIG["aws"]["profile"]
    region = CONFIG["aws"]["region"]
    console.print(f"profile: {profile}")
    console.print(f"region: {region}")
    assert template_file.exists()
    start_date = [int(d) for d in start_date.split("-")]
    end_date = [int(d) for d in end_date.split("-")]
    template = Environment(loader=BaseLoader()).from_string(template_file.read_text())
    results = athena.run_daily(
        profile,
        region,
        template,
        start_date = dt.datetime(start_date[0], start_date[1], start_date[2]),
        end_date = dt.datetime(end_date[0], end_date[1], end_date[2]),
        database = "comscore",
        args = {
        },
        batch_size = 50
    )
    console.print(f"number of results: {len(results)}")
    rows = []
    for r in results:
        date = "-".join(r[0])
        query_id = r[1]['QueryExecution']['QueryExecutionId']
        query_sql = r[1]['QueryExecution']['Query']
        state = r[1]['QueryExecution']['Status']['State']
        rows.append((date, query_id, query_sql, state))

    results_df = pd.DataFrame(rows, columns=['date', 'query_id', "query_sql", "state"])
    now = f"{dt.datetime.now()}".replace(" ", "_")
    results_df.to_csv(f"{out_dir/'query_results_'}{now}.csv", quoting=csv.QUOTE_NONNUMERIC, index=False)

    
    