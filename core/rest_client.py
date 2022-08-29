import requests
from core.respon_result import set_result


class RestClient:

    def __init__(self, root_url):
        self.root_url = root_url
        self.session = requests.session()

    def request(self, path, method, data=None, json=None, params=None, headers=None, **kwargs):
        url = self.root_url + '/' + path
        files = kwargs.get("files", None)
        try:
            if method == "GET":
                r = self.session.get(url, params=params, headers=headers, **kwargs)
            elif method == "POST":
                r = self.session.post(url, data=data, json=json, params=params, files=files, headers=headers, **kwargs)
            elif method == "PUT":
                r = self.session.put(url, data=data, json=json, params=params, files=files, headers=headers, **kwargs)
            elif method == "PATCH":
                r = self.session.patch(url, data=data, json=json, params=params, files=files, headers=headers, **kwargs)
            elif method == "DELETE":
                r = self.session.delete(url, data=data, json=json, params=params, headers=headers, **kwargs)
            else:
                raise Exception("Don't support the method")
            return set_result(r)
        except Exception as e:
            return {"req_code": "fail", "fail_message": e.args}





