import pytest
from selenium import webdriver
import logging
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtility

import time

class Test_001_Login():

    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.test_loggen()
    path= ".//TestData/TestData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********************Test_001_Login***************************")
        self.logger.info("******************** Verifying test_login_ddt **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.rows= XLUtility.getRowCount(self.path,"Sheet1")
        print("no of rows in the excel",self.rows)
        test_list = []

        for r in range (2,self.rows+1):
            self.username = XLUtility.readData(self.path,"Sheet1",r,1)
            self.password = XLUtility.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtility.readData(self.path,"Sheet1",r,3)

            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.login.setUserName(self.username)
            self.login.setPassword(self.password)
            self.login.clickLogin()
            self.driver.implicitly_wait(5)
            act_title= self.driver.title

            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("****PASSED*****")
                    self.login.clickLogout()
                    test_list.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("*****FAILED******")
                    self.login.clickLogout()
                    test_list.append("Fail")

            elif act_title!="Dashboard / nopCommerce administration":
                if self.exp =="Pass":
                    self.logger.info("******FAILED*********")
                    test_list.append("Fail")

                elif self.exp =="Fail":
                    self.logger.info("******PASSED*********")
                    test_list.append("Pass")


        if "Fail" not in test_list:
            self.logger.info("***********test_login_ddt [PASSED]*************")
            self.driver.close()
            assert True
        else:
            self.logger.error("***********test_login_ddt [FAILED]*************")
            self.driver.close()
            assert False

        self.logger.info("*************** End of test_login_ddt *******************")











