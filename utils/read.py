import yaml

from utils.get_filepath import get_yaml_path

path = get_yaml_path()


def read_yaml():
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data
