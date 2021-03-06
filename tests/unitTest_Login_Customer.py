import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_cms(self):
        user = "jtjar"
        pwd = "jj765432"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://unofall2020isqagroup2.pythonanywhere.com/")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://unofall2020isqagroup2.pythonanywhere.com/")
        time.sleep(3)
        # assert that the login was completed
        try:
            # attempt to find the logout URL
            elem = driver.find_element_by_xpath("/html/body/div[1]/div/a")
            elem = elem.get_attribute("href")
            if elem == "http://unofall2020isqagroup2.pythonanywhere.com/accounts/logout/":
                assert True
            else:
                self.fail("Login was not complete successfully - login page may not be working or user may not exist")
                assert False

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
