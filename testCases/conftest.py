from common.read_data import data
import os
import pytest
from common.logger import log

BASE_PATH = os.path.dirname(os.path.dirname(__name__))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as e:
        pytest.skip(str(e))
        log.warning("未读取到{}文件的数据, 将跳过未涉及该文件的测试用例".format(yaml_file_name) + str(e))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_test_data = get_data("api_test_data.yml")
scenario_test_data = get_data("scenario_test_data.yml")








