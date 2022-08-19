from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchCustomerPage:
    textbox_email_xpath = "//input[@id='SearchEmail']"
    textbox_fname_xpath = "//input[@id='SearchFirstName']"
    textbox_lname_xpath = "//input[@id='SearchLastName']"
    button_search_id = "search-customers"
    table_rows_xpath  = "//table[@id='customers-grid']//tbody/tr"
    table_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    table_xpath = "//table[@id='customers-grid']"

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

    def getTableRaws(self):
        rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)

    def getTableValues(self,email):
        flag= False
        rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)
        cols = self.driver.find_elements(By.XPATH, self.table_cols_xpath)
        for r in range(1, len(rows) + 1):
            for c in range(1, len(cols) + 1):
                emailid = self.driver.find_element(By.XPATH, "//table//tbody/tr["+str(r)+"]/td[2]").text
                if emailid == email:
                    flag =True
                    break
        return flag


