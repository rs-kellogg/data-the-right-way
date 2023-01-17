import os
import pytest
import yaml
from pathlib import Path


dir_path = Path(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="session")
def config():
    config_file = dir_path / "config.yml"
    with open(config_file) as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        return conf
    
    
@pytest.fixture(scope="session")
def log_path(config):
    return dir_path/config['log_path']
    

@pytest.fixture(scope="session")
def parquet_path(config):
    return dir_path/config['parquet_path']