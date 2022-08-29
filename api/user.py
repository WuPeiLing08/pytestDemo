from core.rest_client import RestClient
from common.read_data import data
import os

setting_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', "setting.ini")
api_root_url = data.load_ini(setting_file).get("host").get("api_root_url")


class User:
    def __init__(self):
        self.rest_client = RestClient(api_root_url)

    def get_all_users(self, params=None, headers=None, **kwargs):
        path = "/users"
        method = "GET"
        return self.rest_client.request(path, method, params=params, headers=headers, **kwargs)

    def get_user(self, path_data, params=None, headers=None, **kwargs):
        username = path_data.get("username")
        path = "/users/{}".format(username)
        method = "GET"
        return self.rest_client.request(path, method, params=params, headers=headers, **kwargs)














