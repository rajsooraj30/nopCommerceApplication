import string
import random

import pytest
from selenium import webdriver
import logging
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateCustomer import CreateCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_003_AddCustomer():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger=LogGen.test_loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("******************** Test_003_AddCustomer **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************** Logged in **********************")
        self.driver.implicitly_wait(5)

        self.addCust=CreateCustomer(self.driver)
        self.addCust.clickCustomerMenu()
        self.addCust.clickCustomerMenuItem()
        time.sleep(5)
        self.logger.info("******************* Customer page opened *********************")
        self.addCust.clickAddnewButton()
        self.driver.implicitly_wait(5)
        self.logger.info("********************* Add a new customer page opened********************************")
        self.logger.info("********************* Start entering the values ********************************")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("root")
        self.addCust.setDate("12/10/2020")
        self.addCust.selectGender("male")
        self.addCust.setAdminComment("admin")
        self.addCust.setCompanyName("company")
        self.addCust.setCustomerRoles("Vendors")
        self.addCust.setFirstName("Amit")
        self.addCust.setlastName("Shah")
        self.addCust.setManagerOfVendor("1")
        self.logger.info("********************* End entering the values ********************************")
        self.addCust.clickSave()
        self.logger.info("********************* start Validation ********************************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        if 'customer has been added successfully.' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))









