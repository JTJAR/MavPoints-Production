# # automated unit test to ensure a window to add a new client appears
# when the "+ New" button is clicked
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_cms(self):
        user = "test_user"
        pwd = "testinguser123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://unofall2020isqagroup2.pythonanywhere.com/")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
        continue_test = False
        try:
            # verify save button on sign up page appears
            elem = driver.find_element_by_xpath("/html/body/form/button")
            continue_test = True

        except NoSuchElementException:
            self.fail("Add new client does not appear = New Client button not present")
            assert False
            time.sleep(1)
        except:
            self.fail("Edit post NOT successful - error occurred: ")
            assert False
            time.sleep(1)
        time.sleep(2)
        # if test successful so far – set up the required inputs for a Client
        if continue_test:
            elem = driver.find_element_by_id("id_username")
            elem.send_keys(user)
            elem = driver.find_element_by_id("id_email")
            elem.send_keys("jtjarecki@unomaha.edu")
            elem = driver.find_element_by_id("id_full_name")
            elem.send_keys("testing user")
            elem = driver.find_element_by_id("id_address")
            elem.send_keys("testing address 123")
            elem = driver.find_element_by_id("id_city")
            elem.send_keys("test city")
            elem = driver.find_element_by_id("id_state")
            elem.send_keys("test state")
            elem = driver.find_element_by_id("id_zipcode")
            elem.send_keys("12345")
            elem = driver.find_element_by_id("id_phone_number")
            elem.send_keys("1112223333")
            elem = driver.find_element_by_id("id_password1")
            elem.send_keys(pwd)
            elem = driver.find_element_by_id("id_password2")
            elem.send_keys(pwd)
            time.sleep(6)
            # click the Save button
            elem = driver.find_element_by_xpath("/html/body/form/button").click()
            time.sleep(6)
            elem = driver.find_element_by_id("id_username")
            elem.send_keys(user)
            elem = driver.find_element_by_id("id_password")
            elem.send_keys(pwd)
            time.sleep(3)
            elem.send_keys(Keys.RETURN)
            time.sleep(3)
            driver.get("http://unofall2020isqagroup2.pythonanywhere.com/")
            time.sleep(3)
            try:
                # attempt to find the logout URL
                elem = driver.find_element_by_xpath("/html/body/div[1]/div/a")
                elem = elem.get_attribute("href")
                if elem == "http://unofall2020isqagroup2.pythonanywhere.com/accounts/logout/":
                    assert True
                else:
                    self.fail(
                        "Login was not complete successfully - login page may not be working or user may not exist")
                    assert False

            except NoSuchElementException:
                self.fail("Login Failed - user may not exist")
                assert False

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
