import requests
from core.respon_result import response


class RestClient:

    def __init__(self, root_url):
        self.root_url = root_url
        self.session = requests.session()

    def request(self, path, method, data=None, json=None, params=None, files=None, **kwargs):
        url = self.root_url + '/' + path
        try:
            if method == "GET":
                r = self.session.get(url, params=params, **kwargs)
            elif method == "POST":
                r = self.session.post(url, data=data, json=json, params=params, files=files, **kwargs)
            elif method == "PUT":
                r = self.session.put(url, data=data, json=json, params=params, files=files, **kwargs)
            elif method == "PATCH":
                r = self.session.patch(url, data=data, json=json, params=params, files=files, **kwargs)
            elif method == "DELETE":
                r = self.session.delete(url, data=data, json=json, params=params, **kwargs)
            else:
                raise Exception("Don't support the method")
            response.set_result(r)
        except Exception as e:
            response.result["code"] = 0
            self.result["message"] = "请求接口失败"
        return response.result


rest_client = RestClient()




