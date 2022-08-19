import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser.............")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser.............")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser): # This wil get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

################  PyTest  HTML Report ################

#It is hook for adding Rnvironment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Modele Name'] = 'Custmers'
    config._metadata['Tester'] = 'Akila'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)