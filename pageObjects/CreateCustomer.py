from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class CreateCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver


    def clickCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickAddnewButton(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).clear()
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(2)
        if role == "Administrators":
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)

        elif role == "Guests":
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        elif role == "Vendors":
            self.listitem=self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

        elif role == "Registered":
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectGender(self,gender):
        if gender =="male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender =="female":
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setlastName(self,lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setDate(self,date):
        self.driver.find_element_by_xpath(self.txtDob_xpath).clear()
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(date)

    def setCompanyName(self, companyName):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(companyName)

    def setAdminComment(self, AdminComment):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).clear()
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(AdminComment)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_value(value)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()












