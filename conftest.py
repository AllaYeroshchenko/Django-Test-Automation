from fixture.application import Application
import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target=json.load(f)
    return target


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption('--target'))["web"]
    if fixture is None or not fixture.is_valid():
        fixture=Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption('--target'))["db"]
    dbfixture = DbFixture(ssh=db_config["ssh"], 
        ssh_host=db_config["ssh_host"], 
        ssh_user=db_config["ssh_user"], 
        ssh_password=db_config["ssh_password"], 
        host=db_config["host"], 
        database_name=db_config["database_name"], 
        user=db_config["user"], 
        password=db_config["password"],
        user_id=db_config["user_id"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target_secure.json")


