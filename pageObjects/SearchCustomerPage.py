import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os


class SearchCustomerPage:
    textbox_email_xpath = "//input[@id='SearchEmail']"
    textbox_fname_xpath = "//input[@id='SearchFirstName']"
    textbox_lname_xpath = "//input[@id='SearchLastName']"
    button_search_id = "search-customers"
    table_rows_xpath  = "//table[@id='customers-grid']//tbody/tr"
    table_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    table_xpath = "//table[@id='customers-grid']"
    button_exportfile_xpath = "//button[@class='btn btn-success dropdown-toggle']"
    button_allexcel_xpath ="//button[normalize-space()='Export to Excel (all found)']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setFname(self, fname):
        self.driver.find_element(By.XPATH, self.textbox_fname_xpath).send_keys(fname)

    def setLname(self, lname):
        self.driver.find_element(By.XPATH, self.textbox_lname_xpath).send_keys(lname)


    def clickSearch(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def getNoofRaws(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoofCols(self):
       return len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))


    def getTablebyEmail(self,email):
        flag= False
        for r in range(1, self.getNoofRaws() + 1):
            for c in range(1, self.getNoofCols() + 1):
                emailid = self.driver.find_element(By.XPATH, "//table//tbody/tr["+str(r)+"]/td[2]").text
                if emailid == email:
                    flag =True
                    break
        return flag

    def getTablebyName(self,name):
        flag= False
        for r in range(1, self.getNoofRaws() + 1):
            for c in range(1, self.getNoofCols() + 1):
                cname = self.driver.find_element(By.XPATH, "//table//tbody/tr["+str(r)+"]/td[3]").text
                if cname == name:
                    flag =True
                    break
        return flag

    def downloadExportFile(self):
        self.driver.find_element(By.XPATH, self.button_exportfile_xpath).click()
        self.driver.find_element(By.XPATH, self.button_allexcel_xpath).click()

        # wait for download complete
        wait = True
        while (wait == True):
            for fname in os.listdir("C:\\Users\\dissanayake\\Downloads"):
                if ('Unconfirmed') in fname:
                    print('downloading files ...')
                    time.sleep(10)
                else:
                    wait = False
        print('finished downloading all files ...')
        return wait


