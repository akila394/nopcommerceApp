import pytest
from selenium.webdriver.common.by import By
from pageObjects.CustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time


class Test_006_DownloadCustomerFile:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_downoadcustomerfile(self,setup):
        self.logger.info(" ******************* Test_006_DownloadCustomerFile Started *************** ")
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

        self.logger.info("*********** Go to customer page *************")
        self.cp = CustomerPage(self.driver)
        self.cp.clickCustomers()
        self.cp.clickCustomersSubmenu()

        self.logger.info("*********** File Downloading ........ ************")
        scp = SearchCustomerPage(self.driver)
        status = scp.downloadExportFile()
        if status:
            assert False
            self.logger.info("*********** Error in file download........ ************")
            self.driver.close()

        else:
            assert True
            self.logger.info("*********** File Downloaded ........ ************")
            self.driver.close()







