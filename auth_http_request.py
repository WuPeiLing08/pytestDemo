import json
import requests
import hmac


def http_auth(addr, device, productID, secret):
    timestamp = "1567003778853"
    sign = get_sign(device, productID, timestamp, secret)
    payload = json.dumps(
        {
            "deviceIdentifier": device,
            "productID": productID,
            "timestamp": timestamp,
            "sign": sign,
        }
    )

    headers = {"Content-Type": "application/json"}
    r = requests.post(headers=headers, url="{}/auth".format(addr), data=payload)
    return r.json()["info"]["token"]


def get_sign(deviceIdentifier, productID, timestamp, secret):
    to_enc = "{}{}{}{}{}{}".format(
        "deviceIdentifier",
        deviceIdentifier,
        "productID",
        productID,
        "timestamp",
        timestamp,
    )
    enc_res = hmac.new(
        key=bytes(secret, encoding="utf8"),
        msg=bytes(to_enc, encoding="utf8"),
        digestmod="MD5",
    ).hexdigest()
    return enc_res


def post_data(
    addr="http://172.17.2.58:34246",
    url="/topic",
    json_data=None,
    data=None,
    query_data=None,
    headers=None,
):
    url = addr + url
    res = requests.post(
        url,
        json=json_data,
        data=data,
        params=query_data,
        headers=headers,
    )
    return res



if __name__ == "__main__":
    addr = "http://qnergtjv.qbjohpak-jiahuayun-iot-test.rocktl.com:30001"
    deviceIdentifier = "08291"
    productID = "1564168147263074310"
    device_secret = "D9g8URNjHOIhrteomyTzPKjiizLp_Pmo7XTpar768cs="  # 设备secret
    password = http_auth(
        addr, device=deviceIdentifier, productID=productID, secret=device_secret
    )
    print(password)

    headers = {"Content-Type": "text/plain", "password": password}
    json_data = {
        "deviceIdentifier": deviceIdentifier,
        "eventIdentifier": "ranging",
        "tilt": 11.98,
        "sfid": 80,
        "horizon": 88.78,
        "vertical": 0.99
    }
    r = post_data(addr=addr, json_data=json_data, headers=headers)
    print(r.status_code)
    print(r.text)