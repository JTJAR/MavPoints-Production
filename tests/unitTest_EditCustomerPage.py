# # automated unit test to ensure that the edit client page appears
# when the "edit" button is clicked
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_cms(self):
        # login to website with admin user
        user = "instructor"
        pwd = "Mavericks"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://unofall2020isqagroup2.pythonanywhere.com/admin")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://unofall2020isqagroup2.pythonanywhere.com/")
        time.sleep(3)
        assert "Logged In"
        time.sleep(5)

        # find the ‘Customer List’ and click it
        elem = driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
        time.sleep(5)
        continue_test = False
        try:
            # verify 'edit' button appears next to customers
            elem = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[2]/td[12]/a").click()
            continue_test = True

        except NoSuchElementException:
            self.fail("Client did not appear -- There may be no clients stored")
            assert False
            time.sleep(1)
        except:
            self.fail("Edit post NOT successful - error occurred: ")
            assert False
            time.sleep(1)
        time.sleep(2)

        # see if the 'update' button appears on the edit page
        try:
            elem = driver.find_element_by_xpath("/html/body/form/button")
            assert True

        except NoSuchElementException:
            self.fail("Update button could not be found")
            assert False
        except:
            self.fail("Edit post NOT successful - error occurred: ")
            assert False

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
