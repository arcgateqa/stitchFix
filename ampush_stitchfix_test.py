__author__ = 'KARUNAKAR'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from po_ampush_stichfix import ObjectAmpStitchFix
import csv
import time
from tqdm import tqdm
class AAUIAmpushStitchFix(unittest.TestCase):

    def setUp(self):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        chrome_options = webdriver.ChromeOptions()
        #todo PROXY disabled
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(desired_capabilities=d, chrome_options=chrome_options)
        self.base_url = 'https://style.stitchfix.com'
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # self.driver.orientation = 'PORTRAIT'
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_variant_displayed()

    def test_function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()

class UIAmpushStitchFixMobileIphone4(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Apple iPhone 4"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('iPhone 4')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class UIAmpushStitchFixMobileIphone5(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Apple iPhone 5"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('iPhone 5')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class UIAmpushStitchFixMobileIphone6(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Apple iPhone 6"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('iPhone 6')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class UIAmpushStitchFixMobileIphone6Plus(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Apple iPhone 6 Plus"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('iPhone 6 plus')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class UIAmpushStitchFixMobileAppleIpad(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Apple iPad"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('iPad')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class UIAmpushStitchFixMobileIpadMini(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Apple iPad Mini"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('iPad Mini')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()

        self.assertEqual([], self.verificationErrors)

class UIAmpushStitchFixMobileSamsungGalaxyNote3(unittest.TestCase):

    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('general.useragent.override', "iPhone")
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        # self.driver = webdriver.Chrome(desired_capabilities=d)
        mobile_emulation = {"deviceName": "Samsung Galaxy Note 3"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # PROXY = "54.167.142.68:3128"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=d)
        # self.driver.orientation = 'landscape'
        # self.driver = webdriver.Firefox(profile)
        self.verificationErrors = []

    def _function_form_variant_displayed(self):
        # self.driver.orientation = 'portrait'
        driver = ObjectAmpStitchFix(self.driver)
        driver.mobile_function_form_variant_displayed('Note 3')

    def _function_all_forms_sign_up(self):
        driver = ObjectAmpStitchFix(self.driver)
        driver.function_form_sign_up()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
