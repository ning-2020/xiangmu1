import pytest
from case.readyaml import read_yaml
import os

data_test = read_yaml("testdata.yaml")["updata_info"]
print(data_test)

@pytest.mark.njb
@pytest.mark.parametrize("test_info,expect",data_test)
def test_update_297(login_fix,test_info,expect):
    ''' 修改个人信息-sex参数传F和M两种类型，成功(枚举类型) '''
    s = login_fix
    url = os.environ["xadmin_host"]+"/api/v1/userinfo"
    body = {
        "name": "test",
        "sex": test_info,
        "age": 20,
        "mail": "283340479@qq.com"
    }
    r = s.post(url=url,json=body)
    print(r.text)
    assert r.json()["message"] == expect["message"]
    assert r.json()["code"] == expect["code"]
# @pytest.mark.skip("BUG阻塞")
@pytest.mark.xfail #强制讲案例置为failed,需要在ini文件内配置xfail_strict = true
def test_updata_info_32(login_fix):
    '''修改个人信息成功'''
    s = login_fix
    url = os.environ["xadmin_host"]+"/api/v1/userinfo"
    body = {"name": "test","sex": "M","age": 20,"mail": "283340479@qq.com"}
    r = s.post(url=url,json=body)
    print(r.text)
    assert r.json()["message"] == "update some data!"
    assert r.json()["code"] == 0
