import allure
from api.user import user
from common.logger import log
from testCases.conftest import api_test_data
import pytest


@allure.epic("单个接口测试用例")
@allure.feature("得到用户信息")
class TestGetUserInfo():
    @allure.story("用例：得到所有用户的信息")
    @pytest.mark.parametrize("data", api_test_data["test_get_all_users"])
    def test_get_all_users(self, data):
        r = user.get_all_users()
        assert r["req_code"] == data.get("except_req_code")
        assert r["code"] == data.get("except_code")
        assert r["msg"] == data.get("except_msg")

