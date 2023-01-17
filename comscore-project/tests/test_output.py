import pytest
import pandas as pd


def test_smoke(log_path, parquet_path):
    assert log_path.exists()
    assert parquet_path.exists()


def test_queries_for_failures(log_path):
    log_files = [f for f in log_path.glob("*.csv")]
    log_files.sort()
    assert len(log_files) > 0
    log_df = pd.read_csv(log_files[-1])
    states = list(log_df['state'])
    num_successes = states.count("SUCCESS")
    num_failures = states.count("FAILED")
    assert num_successes == len(states), f"The last SQL run had {num_failures} failed queries. Check the log file {log_files[-1]} for more details"