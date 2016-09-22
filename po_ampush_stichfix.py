__author__ = 'KARUNAKAR'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import csv
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
class ObjectAmpStitchFix():

    def __init__(self, driver):
        self.driver = driver

    def write_header_form_sign_up(self):
        header_lines = ['Test Name', 'Web/Mobile?', 'Resolution', 'Form A% ?', 'Form B% ?', 'Form C% ?',
                        'Form D% ?', 'Form E% ?', 'Form F% ?', 'No of Iterations of URL', 'Pass/Fail?']
        with open("Amp_UI_Form_Sign_Up_RESULTS.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows([header_lines])

    def write_header_form_variant(self):
        header_lines = ['Test Name', 'Web/Mobile?', 'Resolution', 'Form A% ?', 'Form B% ?', 'Form C% ?',
                        'Form D% ?', 'Form E% ?', 'Form F% ?', 'No of Iterations of URL', 'Pass/Fail?']
        with open("Amp_UI_Form_variant_RESULTS.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows([header_lines])

    def write_location_info(self, write_me):
        time.sleep(1)
        with open("Amp_UI_Form_variant_RESULTS.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerows([[unicode(s).encode("utf-8") for s in write_me]])

    def write_form_sign_up(self, write_me):
        time.sleep(1)
        with open("Amp_UI_Form_Sign_Up_RESULTS.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerows([[unicode(s).encode("utf-8") for s in write_me]])

    def write_header_for_sign_up(self):
        header_lines = ['Test Name', 'Web/Mobile?', 'Resolution', 'Form A Sign Up ?', 'Form B Sign Up?', 'Form C Sign Up ?',
                        'Form D Sign Up ?', 'Form E Sign Up ?', 'Form F Sign Up ?', 'Pass/Fail?']
        with open("Amp_UI_Sign_Up_RESULTS.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows([header_lines])

    def mobile_function_form_variant_displayed(self, device_name):
        driver = self.driver
        # self.write_header_form_variant()
        csv_content = []
        with open('url.csv') as f:
            content = f.readlines()
            for single_column in csv.reader(content, delimiter=","):
                csv_content.append(single_column)
        # save_result = []
        for each in csv_content:
            if each[0] == '1':
                change = each[2]
                try:
                    form_percent = self.form_variant_calculator(each[1], change, False)
                    form_a, form_b, form_c, form_d, form_e, form_f = form_percent
                    status = ['Form variant', 'Mobile', 'Browser Iphone4', form_a, form_b, form_c,
                              form_d, form_e, form_f, each[2], 'Test Passed']
                    self.write_location_info(status)
                    try:
                        driver.get_screenshot_as_file('Device_NAME_%s.png'%device_name)
                    except:
                        pass
                except Exception as e:
                    status = ['Form variant', 'Web', 'Browser Iphone4', '_Failed_',
                              '_Failed_', '_Failed_', '_Failed_', '_Failed_', '_Failed_', 'Test Failed']
                    self.write_location_info(status)
                    try:
                        driver.get_screenshot_as_file('Device_NAME_%s.png'%device_name)
                    except:
                        pass
                    print 'Failure due to:', e
            else:
                print 'No urls found in urls.csv to run the test'

    def function_form_variant_displayed(self):
        driver = self.driver
        self.write_header_form_variant()
        csv_content = []
        with open('url.csv') as f:
            content = f.readlines()
            for single_column in csv.reader(content, delimiter=","):
                csv_content.append(single_column)
        # save_result = []
        for each in csv_content:
            if each[0] == '1':
                change = each[2]
                # status = 'Unable to run the test'
                if each[3] == 'Yes':
                    resol_variant = [(360, 640), (412, 732), (768, 1024), (1024, 768),
                                     (320, 480), (320, 568), (375, 667), (414, 736)]
                else:
                    resol_variant = [(1024, 768)]
                for x in resol_variant:
                    res_x, res_y = x
                    try:
                        form_percent = self.form_variant_calculator(each[1], change, res_x, res_y, True)
                        form_a, form_b, form_c, form_d, form_e, form_f = form_percent
                        status = ['Form variant', 'Web', (res_x, res_y), form_a, form_b, form_c,
                                  form_d, form_e, form_f, each[2], 'Test Passed']
                        self.write_location_info(status)
                        try:
                            driver.get_screenshot_as_file('web.png')
                        except:
                            pass
                    except Exception as e:
                        status = ['Form variant', 'Web', (res_x, res_y), '_Failed_',
                                  '_Failed_', '_Failed_', '_Failed_', '_Failed_', '_Failed_', 'Test Failed']
                        self.write_location_info(status)
                        try:
                            driver.get_screenshot_as_file('web.png')
                        except:
                            pass
                        print 'Failure due to:', e
                    # finally:
                    #     # write_status = save_result
                    #     self.write_location_info(save_result)
            else:
                print 'No urls found in urls.csv to run the test'
                # self.write_location_info('No urls found in urls.csv to run the test')
        driver.get('https://www.whatismyip.com')
        print 'Getting location'

        # for i in tqdm(range(100)):
        #     time.sleep(0.1)
        time.sleep(3)
        area_name = driver.find_element_by_xpath('//tr/td[contains(text(), "Country:")]').find_element_by_xpath(
            "following-sibling::*").text
        print '\n\n\n\nForm variant Completed'
        print '\n\n\n\n\n'
        print 'Proxy enabled for the Country: %s'%area_name
        print 'Proxy enabled for the Country: %s'%area_name
        print 'Proxy enabled for the Country: %s'%area_name
        print 'Proxy enabled for the Country: %s'%area_name
        print 'Proxy enabled for the Country: %s'%area_name

    def clickon_sign_up_and_verify_client_page(self):
        new_driver = self.driver
        import ipdb
        ipdb.set_trace()

        new_driver.find_element_by_name('commit').click()
        assert 'My fix' == self.driver.find_element_by_class_name('my-fix')

    def click_on_get_started(self):
        self.driver.find_element_by_class_name('copy').find_element_by_link_text('GET STARTED').click()

    def form_a(self):
        new_driver = self.driver
        tn = time.strftime("%Y%m%d-%H%M%S")
        new_name = tn+'test@gmail.com'
        self.click_on_get_started()
        fname = new_driver.find_element_by_id('user_first_name')
        fname.clear()
        fname.send_keys('testamp')
        lname = new_driver.find_element_by_id('user_last_name')
        lname.clear()
        lname.send_keys('test')
        uemail = new_driver.find_element_by_id('user_email')
        uemail.clear()
        uemail.send_keys(new_name)
        zipcode = new_driver.find_element_by_id('user_client_attributes_shipping_postcode')
        zipcode.clear()
        zipcode.send_keys('10001')
        new_driver.find_elements_by_class_name('btn-group')[1].find_elements_by_class_name('btn')[1].click()
        new_driver.find_element_by_css_selector('div.form-group.submission').find_element_by_tag_name('input').click()

    def form_b(self):
        new_driver = self.driver
        self.click_on_get_started()
        fname = new_driver.find_element_by_css_selector('#new_user_pop > div.form-group > #user_first_name')
        fname.clear()
        tn = time.strftime("%Y%m%d-%H%M%S")
        new_name = tn+'test@gmail.com'
        fname.send_keys('test12')
        last_name = new_driver.find_element_by_css_selector('#new_user_pop > div.form-group > #user_last_name')
        last_name.clear()
        last_name.send_keys('test')
        emailname = new_driver.find_element_by_css_selector('#new_user_pop > div.form-group > #user_email')
        emailname.clear()
        emailname.send_keys(new_name)
        zipme = new_driver.find_element_by_css_selector('#new_user_pop > div.form-group > #user_client_attributes_shipping_postcode')
        zipme.clear()
        zipme.send_keys('10001')
        new_driver.find_element_by_css_selector('#new_user_pop > div.form-group.submission > input[name="commit"]').click()

    def form_c(self):
        new_driver = self.driver
        tn = time.strftime("%Y%m%d-%H%M%S")
        new_name = tn+'test@gmail.com'
        self.click_on_get_started()
        new_driver.find_element_by_link_text('SIGN UP WITH FACEBOOK')
        self.fb_login_form()
        f_name = new_driver.find_element_by_id('user_first_name')
        f_name.clear()
        f_name.send_keys('testamp')
        l_name =  new_driver.find_element_by_id('user_last_name')
        l_name.clear()
        l_name.send_keys('test')
        u_email = new_driver.find_element_by_id('user_email')
        u_email.clear()
        u_email.send_keys(new_name)
        new_driver.find_elements_by_class_name('btn-group')[1].find_elements_by_class_name('btn')[1].click()
        new_driver.find_element_by_css_selector('div.form-group.submission').find_element_by_tag_name('input').click()

    def form_d(self):
        new_driver = self.driver
        self.click_on_get_started()
        new_driver.find_element_by_link_text('Continue with Facebook').click()
        self.fb_login_form()
        tn = time.strftime("%Y%m%d-%H%M%S")
        new_name = tn+'test@gmail.com'
        f_name = new_driver.find_element_by_id('user_first_name')
        f_name.clear()
        f_name.send_keys('testamp')
        l_name =  new_driver.find_element_by_id('user_last_name')
        l_name.clear()
        l_name.send_keys('test')
        u_email = new_driver.find_element_by_id('user_email')
        u_email.clear()
        u_email.send_keys(new_name)
        new_driver.find_elements_by_class_name('btn-group')[1].find_elements_by_class_name('btn')[1].click()
        new_driver.find_element_by_css_selector('div.form-group.submission').find_element_by_tag_name('input').click()

    def form_e(self):
        new_driver = self.driver
        self.click_on_get_started()
        fb_sign_up_button = new_driver.find_element_by_css_selector('#new_user_pop > div.sign-in-form.fb-login-c > div > ul > li > div > #fb-button > #facebook_signup')
        # assert True == self.is_element_present('id', 'facebook_signup')
        fb_sign_up_button.click()
        self.fb_login_form()
        new_driver.find_element_by_css_selector('#new_user_pop > div.form-group > #user_email').clear()
        tn = time.strftime("%Y%m%d-%H%M%S")
        new_name = tn+'test@gmail.com'
        new_driver.find_element_by_css_selector('#new_user_pop > div.form-group > #user_email').send_keys(new_name)
        new_driver.find_element_by_css_selector('#new_user_pop > div.form-group.submission > input[name="commit"]').click()

    def form_f(self):
        new_driver = self.driver
        self.click_on_get_started()
        new_driver.find_element_by_css_selector('#new_user_pop > div.sign-in-form.fb-login-d > div.form-group > ul > li > a.linkFB > span').click()
        self.fb_login_form()
        f_name = new_driver.find_element_by_id('user_first_name')
        f_name.clear()
        f_name.send_keys('testamp')
        l_name = new_driver.find_element_by_id('user_last_name')
        l_name.clear()
        l_name.send_keys('test')
        u_email = new_driver.find_element_by_id('user_email')
        u_email.clear()
        tn = time.strftime("%Y%m%d-%H%M%S")
        new_name = tn+'test@gmail.com'
        u_email.send_keys(new_name)
        self.clickon_sign_up_and_verify_client_page()

    def fb_login_form(self):
        new_driver = self.driver
        new_driver.switch_to.window(new_driver.window_handles[-1])
        new_driver.find_element_by_id('email').send_keys('arcgateqa@gmail.com')
        new_driver.find_element_by_id('pass').send_keys('ArcGate1!')
        new_driver.find_element_by_id('loginbutton').click()
        new_driver.switch_to.window(new_driver.window_handles[-1])

    def random_num(self):
        import random
        return random.randint(0, 50)

    def form_detector(self):
        new_driver = self.driver
        time.sleep(1)
        new_driver.delete_all_cookies()
        browser_log = []
        try:
            for log_value in new_driver.get_log('browser'):
                browser_log.append(log_value)
            req_form_data = browser_log[1]
            # print req_form_data
            form_name = req_form_data.get('message')[-1]
            browser_log[:] = []
            new_driver.delete_all_cookies()
        except:
            form_name = ''
            pass
        return form_name

    def domain_detector(self, find_domain_name):
        import tldextract
        domain_name = tldextract.extract(find_domain_name)
        return domain_name.subdomain, domain_name.domain

    def get_domain_name(self):
        new_driver = self.driver
        domain_name = self.domain_detector(new_driver.current_url)
        return domain_name

    def calculate_each_form_occurence(self, forms, x):
        a_form = forms.count('a')
        b_form = forms.count('b')
        c_form = forms.count('c')
        d_form = forms.count('d')
        e_form = forms.count('e')
        f_form = forms.count('f')
        aa_form = (a_form*1.0)*100/x
        bb_form = (b_form*1.0)*100/x
        cc_form = (c_form*1.0)*100/x
        dd_form = (d_form*1.0)*100/x
        ee_form = (e_form*1.0)*100/x
        ff_form = (f_form*1.0)*100/x
        return [aa_form, bb_form, cc_form, dd_form, ee_form, ff_form]

    def form_variant_calculator(self, url, change, _resolution_x_=None, _resolution_y_=None, flag=None):
        new_driver = self.driver
        nchange = int(change)
        if flag == True:
            try:
                new_driver.set_window_size(_resolution_x_, _resolution_y_)
            except:
                pass
        form_names = []
        for each in xrange(0, nchange):
            new_driver.get(url)
            form_name = self.form_detector()
            form_names.append(form_name)
            print 'count', each
        form_per = self.calculate_each_form_occurence(form_names, nchange)
        return form_per

    def get_particular_form(self, req_form, url):
        new_driver = self.driver
        new_driver.get(url)
        current_present_form = self.form_detector()
        if req_form != current_present_form:
            while True:
                new_driver.refresh()
                time.sleep(2)
                form_new_value = self.form_detector()
                # import ipdb
                # ipdb.set_trace()
                if req_form == form_new_value:
                    break

    def all_forms_sign_up(self, url, res_x, res_y):
        new_driver = self.driver
        # import ipdb
        # ipdb.set_trace()
        #get form name to sign up
        new_driver.set_window_size(res_x, res_y)
        self.get_particular_form('a', url)
        self.form_a()
        new_driver.delete_all_cookies()

        self.get_particular_form('b', url)
        self.form_b()
        new_driver.delete_all_cookies()

        self.get_particular_form('c', url)
        self.form_c()
        new_driver.delete_all_cookies()

        self.get_particular_form('d', url)
        self.form_d()
        new_driver.delete_all_cookies()

        self.get_particular_form('e', url)
        self.form_e()
        new_driver.delete_all_cookies()

        self.get_particular_form('f', url)
        self.form_f()
        new_driver.delete_all_cookies()


    def function_form_sign_up(self):
        driver = self.driver
        self.write_header_form_sign_up()
        csv_content = []
        with open('url.csv') as f:
            content = f.readlines()
            for single_column in csv.reader(content, delimiter=","):
                csv_content.append(single_column)
        # save_result = []
        for each in csv_content:
            if each[0] == '1':
                resol_variant = [(1024, 768)]
                for x in resol_variant:
                    res_x, res_y = x
                    try:
                        self.all_forms_sign_up(each[1], res_x, res_y)
                        status = ['Form Sign Up', 'Web', (res_x, res_y), 'Passed', 'Passed', 'Passed',
                                  'Passed', 'Passed', 'Passed', each[2], 'Test Passed']
                        self.write_form_sign_up(status)
                    except Exception as e:
                        status = ['Form Sign Up', 'Web', (res_x, res_y), '_Failed_',
                                  '_Failed_', '_Failed_', '_Failed_', '_Failed_', '_Failed_', 'Test Failed']
                        self.write_form_sign_up(status)
                        print 'Failure due to:', e

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
