from common.logger import log


def set_result(r):
    result = {}
    result["req_code"] = "success"
    result["http_code"] = r.status_code
    if r.text:
        try:
            r_json = r.json()
            if isinstance(r_json, dict):
                result.update(r_json)
            elif isinstance(r_json, list):
                result["data"] = list
        except Exception as e:
            log.info(e)

    return result




