import os
import allure

@allure.story("正确输入用户名，密码，登录系统成功")
def test_login_1(login_fix):
    s = login_fix
    url = os.environ["xadmin_host"] + "/api/v1/userinfo"
    r = s.get(url)
    print(r.text)
    assert r.json()["msg"] == "sucess!"
