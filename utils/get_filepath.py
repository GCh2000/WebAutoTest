import os.path


def get_logo_path():
    path = os.path.join((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "file", "spring.jpg")
    print(path)
    return path


def get_yaml_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "test_parametrize", "data.yaml")
    print(path)
    return path


if __name__ == '__main__':
    get_yaml_path()
    # print(os.path.realpath(__file__))
    # print(os.path.dirname(os.path.realpath(__file__)))




