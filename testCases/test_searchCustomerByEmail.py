import pytest
from selenium.webdriver.common.by import By
from pageObjects.CustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time


class Test_004_SearchCustomerByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchcustomers(self,setup):
        self.logger.info(" ******************* Test_004_SearchCustomerByEmail Started *************** ")
        self.logger.info("****************** Login Started ****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        # Log in
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("****************** User Logged in *******************")

        # Add new customer
        self.logger.info("*********** Add Customer Details *************")
        self.cp = CustomerPage(self.driver)
        self.cp.clickCustomers()
        self.cp.clickCustomersSubmenu()

        self.logger.info("*********** Search Using Email *************")
        self.scp = SearchCustomerPage(self.driver)
        self.scp.setEmail("james_pan@nopCommerce.com")
        self.scp.clickSearch()
        time.sleep(5)
        self.logger.info("*********** Clicked search button *************")
        status = self.scp.getTablebyEmail("james_pan@nopCommerce.com")
        if status:
            assert True
            self.logger.info("*************** TC_004_SearchCustomerByEmail Passed ***************")
            self.driver.close()
        else:
            self.logger.error("*************** TC_004_SearchCustomerByEmail Failed ***************")
            self.driver.close()
            assert False



