from selenium import webdriver
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        print("-------------------Launching edge browser-------------------")
        driver = webdriver.Edge("C:\\Drivers\\msedgedriver.exe")
    elif browser=='firefox':
        print("--------------------Launching Firefox browser-----------------------------")
        caps = DesiredCapabilities.FIREFOX.copy()
        caps['marionette'] = False
        driver = webdriver.Firefox(capabilities=caps)
    else:
        print("----------------------------Launching Chrome browser---------------------------------")
        driver = webdriver.Chrome("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    return driver



def pytest_addoption(parser):     #this will get the value from CLI /Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):            #this will return the Browser value to setup method
    return request.config.getoption("--browser")

###################### Pytest HTML Reports#########################

#it is a Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']= 'nop commerse'
    config._metadata['Module Name']= 'Login'
    config._metadata['Tester']='Sooraj'

#It is Hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)