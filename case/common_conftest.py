import json
import requests
import re
import os
import pytest


class KeChengApi():
    def __init__(self,s,host):
        self.host = host
        self.s = s
    def login(self,username="test",password="123456"):
        url1 = self.host+"/api/v1/login"
        body = {
                 "username":username,
                 "password":password
            }
        r = self.s.post(url1,json=body)
        token = r.json().get("token") # 取出token
        h = {
            "Authorization": "Token %s" % token
        }
        self.s.headers.update(h) #更新头部
        return token



    def get_info(self):
        # 2.查询信息接口
        url2 = self.host + "/api/v1/userinfo"
        r2 = self.s.get(url2)
        print(r2.json())
        mail = r2.json()["data"][0]["mail"]
        print(mail)
        return r2
    def updata_info(self,
                    name="test",
                    sex="M",
                    age="20",
                    mail="283340479@qq.com"
                    ):
        # 3.修改信息个人信息
        url3 = self.host + "/api/v1/userinfo"
        body = {
            "name": name,
            "sex": sex,
            "age": age,
            "mail": mail
        }
        r3 = self.s.post(url3,json=body)
        print(r3.json()["data"])
        return r3.json()

if __name__ == '__main__':
    s = requests.session()
    host = os.environ["host"]
    shilihua = KeChengApi(s,host)
    shilihua.login(username="test1")
    shilihua.get_info()
    shilihua.updata_info(name="test1")



