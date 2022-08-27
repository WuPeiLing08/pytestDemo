class ResponseResult:
    def __init__(self):
        self.result = {}
        self.result["code"] = 0
        self.result["message"] = ""

    def set_result(self, r):
        self.result["code"] = r.status_code
        self.result["message"] = "success"
        if r.text():
            try:
                r_json = r.json()
                if isinstance(r_json, dict):
                    self.result.update(r_json)
                elif isinstance(r_json, list):
                    self.result["data"] = list
            except Exception as e:
                import traceback
                print(traceback.print_exc())


response = ResponseResult()



