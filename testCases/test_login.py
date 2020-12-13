import pytest
from selenium import webdriver
import logging
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import time


class Test_001_Login():

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger=LogGen.test_loggen()

    @pytest.mark.regression
    def test_homepageTitle(self, setup):

        self.logger.info("******************** Test_001_Login **********************")
        self.logger.info("******************** Verifying test_homepageTitle **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        act_title = self.driver.title
        if act_title == 'Your store. Logi':
            assert True
            self.driver.close()
            self.logger.info("******************** Verifying test_homepageTitle [PASSED] **********************")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\rajso\\PycharmProjects\\nopCommerceApplication\\Screenshots\\test_homepageTitle.png")
            time.sleep(4)
            self.driver.close()
            self.logger.error("******************** Verifying test_homepageTitle [FAILED] **********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************** Verifying test_login **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        login = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        login.setUserName(username=self.username)
        login.setPassword(password=self.password)
        login.clickLogin()
        self.driver.implicitly_wait(5)
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administratio":
            assert True
            self.driver.close()
            self.logger.info("******************** Verifying test_login [PASSSED] **********************")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\rajso\\PycharmProjects\\nopCommerceApplication\\Screenshots\\test_login.png")
            self.logger.error("******************** Verifying test_login [FAILED] **********************")
            self.driver.close()
            assert False
