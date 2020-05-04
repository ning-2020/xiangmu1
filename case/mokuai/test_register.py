import requests
import os
s = requests.session()
def test_register_1(delect_user):
    '''注册成功'''
    url = os.environ["xadmin_host"]+"/api/v1/register"

    body = {
        "username": "test_n",
        "password": "123456",
        "mail": "njb@123.com"
    }
    r = s.post(url,json=body)
    print(r.json())

    assert r.json()["msg"] == "注册成功!"

def test_register_2(insert_user):
    '''注册-注册失败-用户已注册'''
    url = os.environ["xadmin_host"]+"/api/v1/register"

    body = {
        "username": "test_1",
        "password": "123456",
        "mail": "njb@123.com"
    }
    r = s.post(url,json=body)
    print(r.json())

    assert r.json()["msg"] == "test_1用户已被注册"
