import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info(" ******************* Test_001_Login Started *************** ")
        self.logger.info(" ****************** Verifying Home Page Title *************** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        act_title= self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** Home Page Title test is Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("****************** Home Page title test is failed ***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************** Verifying Login Test ***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp= LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************** Login test is Passed  ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("****************** Login test is Failed ***************")
            assert False