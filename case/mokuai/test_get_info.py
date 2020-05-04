from case.common_conftest import KeChengApi
import os

def test_get_info(login_fix):
    s = login_fix
    url = os.environ["xadmin_host"] + "/api/v1/userinfo"
    result = s.get(url)
    assert result.json()["msg"] == "sucess!"
    assert result.json()["code"] == 0

