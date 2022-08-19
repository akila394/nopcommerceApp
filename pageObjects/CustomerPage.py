import random
import string

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerPage:
    link_customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_submenu_xpath = "//a[@href='/Admin/Customer/List']/p[contains(text(),'Customers')]"
    btn_addnew_xpath = "//a[@class='btn btn-primary']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_firstName_xpath = "//input[@id='FirstName']"
    textbox_lastName_xpath = "//input[@id='LastName']"
    radiobutton_male_xpath = "//input[@id='Gender_Male']"
    radiobutton_female_xpath = "//input[@id='Gender_Female']"
    textbox_dateofBirth_xpath = "//input[@id='DateOfBirth']"
    textbox_companyName_xpath = "//input[@id='Company']"
    checkbox_istaxExempt_xpath = "//input[@id='IsTaxExempt']"
    list_newsletter_xpath = "(//div[@role='listbox'])[1]"
    list_newsleter_storename_xpath = "//li[text()='Your store name']"
    list_newsletter_teststore_xpath = "//li[text()='Test store 2']"
    list_customerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    list_customerRoles_guest_xpath = "//li[text()='Guests']"
    list_customerRoles_registered_xpath = "//li[text()='Registered']"
    list_customerRoles_venders_xpath = "//li[text()='Vendors']"
    list_customerRoles_forumMederators_xpath = "//li[text()='Forum Moderators']"
    list_customerRoles_administrators_xpath = "//li[text()='Administrators']"
    dropdown_managerofVender_xpath = "//select[@id='VendorId']"
    checkbox_active_xpath = "//input[@id='Active']"
    textbox_adminComment_xpath = "//textarea[@id='AdminComment']"
    button_save_xpath ="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomers(self):
        self.driver.find_element(By.XPATH, self.link_customers_xpath).click()

    def clickCustomersSubmenu(self):
        self.driver.find_element(By.XPATH, self.link_customers_submenu_xpath).click()

    def clickAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.textbox_firstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.textbox_lastName_xpath).send_keys(lastname)

    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radiobutton_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.radiobutton_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radiobutton_male_xpath).click()

    def setDateofBirth(self, dateofbirth):
        self.driver.find_element(By.XPATH, self.textbox_dateofBirth_xpath).send_keys(dateofbirth)

    def setCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.textbox_companyName_xpath).send_keys(companyname)

    def checkTaxExcempt(self):
        self.driver.find_element(By.XPATH, self.checkbox_istaxExempt_xpath).click()

    def setNewsLetter(self, option):
        self.driver.find_element(By.XPATH, self.list_newsletter_xpath).click()
        if option == "Your store name":
            self.storeOption = self.driver.find_element(By.XPATH, self.list_newsleter_storename_xpath)
        else:
            self.storeOption = self.driver.find_element(By.XPATH, self.list_newsletter_teststore_xpath)

        self.driver.execute_script("arguments[0].click();",self.storeOption)

    def setCustomerRoles(self, customerRole):
        self.driver.find_element(By.XPATH, self.list_customerRoles_xpath).click()
        if customerRole == "Administrator":
            self.roleOption = self.driver.find_element(By.XPATH, self.list_customerRoles_administrators_xpath)
        elif customerRole == "Vendors":
            self.roleOption = self.driver.find_element(By.XPATH, self.list_customerRoles_venders_xpath)
        elif customerRole == "Forum Moderators":
            self.roleOption = self.driver.find_element(By.XPATH, self.list_customerRoles_forumMederators_xpath)
        elif customerRole == "Guest":
            try:
                self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.list_customerRoles_registered_xpath)))
                self.driver.execute_script("arguments[0].click();", self.element)
                self.roleOption = self.driver.find_element(By.XPATH, self.list_customerRoles_guest_xpath)
            except:
                None

        self.driver.execute_script("arguments[0].click();", self.roleOption)

    def selectManagerofVendor(self,vendor):
        sel = Select(self.driver.find_element(By.XPATH, self.dropdown_managerofVender_xpath))
        if vendor == "Vendor1":
            sel.select_by_visible_text("Vendor 1")
        elif vendor == "Vendor2":
            sel.select_by_visible_text("Vendor 2")

    def selectIsActive(self):
        self.driver.find_element(By.XPATH, self.checkbox_active_xpath).click()

    def setAdminComments(self,comment):
        self.driver.find_element(By.XPATH, self.textbox_adminComment_xpath).send_keys(comment)

    def hitSavebtn(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()










