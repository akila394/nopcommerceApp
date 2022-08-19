import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.CustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_Customers:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customers(self,setup):
        self.logger.info(" ******************* Test_003_Customers Started *************** ")
        self.logger.info("****************** Login Started ****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
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
        self.cp.clickAddnew()

        def random_generator(size=8, chars=string.ascii_lowercase + string.digits): # Generate Random charactors in Email
            return ''.join(random.choice(chars) for x in range(size))
        self.email = random_generator() + "@gmail.com"
        self.cp.setEmail(self.email)
        self.cp.setPassword("abcd")
        self.cp.setFirstName("John")
        self.cp.setLastName("Day")
        self.cp.selectGender("Male")
        self.cp.setDateofBirth("04/18/1994")
        self.cp.setCompanyName("City")
        self.cp.checkTaxExcempt()
        self.cp.setNewsLetter("Your store name")
        #self.cp.setCustomerRoles("Guest")
        #self.cp.setCustomerRoles("Administrator")
        self.cp.selectManagerofVendor("Vendor1")
        #self.cp.selectIsActive()
        self.cp.setAdminComments("Added new Customer")
        self.cp.hitSavebtn()

        self.logger.info("************ Added a New Customer ************")
        self.logger.info("******** Test_003_Customers Verification Started ************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text # Take all the texts in the page

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*********** Add customer Test Passed ***********")
            self.driver.close()
        else:
            assert True == False
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("*********** Add customer Test Failed ************")
            self.driver.close()

        self.logger.info("******** Test_003_Customers Verification Finished **********")
        self.logger.info("********** Ending Add customer Test *************")




