import pytest
import requests
from case.common_conftest import KeChengApi
import os



def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:9000",
        help="test case project host address"
    )

@pytest.fixture(scope="session",autouse=True)
def host(request):
    '''获取环境变量，给到环境变量'''
    os.environ["xadmin_host"] = request.config.getoption("--cmdhost")
    print("当前运行环境为 %s" %os.environ["xadmin_host"])

@pytest.fixture(scope="session")
def login_fix():
    # 先登录前置
    s = requests.session()
    shilihua = KeChengApi(s,host=os.environ["xadmin_host"])
    shilihua.login()
    return s

@pytest.fixture(scope="session")
def unlogin_fix():
    # 不登录
    s = requests.session()
    shilihua = KeChengApi(s,host=os.environ["xadmin_host"])
    # shilihua.login()
    return s

from common.dbconnect import execute_sql


s = requests.session()

@pytest.fixture(scope="function")
def delect_user():
    # 执行前先删除数据
    delect_sql = "DELETE from auth_user WHERE username='test_n';"
    execute_sql(delect_sql)

@pytest.fixture(scope="function")
def insert_user():
    # 插入数据
    insert_sql = "INSERT INTO `apps`.`auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES ('3', 'pbkdf2_sha256$100000$2F3XChjcqHxN$ddJgxZU0zozEPoJ2ykbfjCT4E9KqG/jSoj52xE9bsdQ=', NULL, '0', 'test1', '', '', '283340479@qq.com', '0', '1', '2019-11-30 03:01:03.709769');';"
    execute_sql(insert_sql)