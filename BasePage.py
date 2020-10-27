from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.DateTime import datetime
from SeleniumLibrary import SeleniumLibrary
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .BaseLocators import BaseLocators as Locators
import os


class BasePage():
    def __init__(self):
        self.session = SeleniumLibrary(run_on_failure='Nothing')
        self.builtin = BuiltIn()
        self.datetime = datetime
        self.set_browser_settings()

    def screenshot(self):

        self.session.capture_page_screenshot()

    def set_browser_settings(self, browser='gc', timeout=30, implicit_wait=30,speed=0.1, run_on_failure='screenshot',
                             screenshot_root_directory=None):
        self.browser = browser
        self.selenium_timeout = timeout
        self.implicit_wait = implicit_wait
        self.selenium_speed = speed
        self.run_on_failure = run_on_failure
        self.screenshot_directory = screenshot_root_directory

    def close_browser_window(self):
        self.session.close_browser()

    def close_browser_all_windows(self):
        self.session.close_all_browsers()

    def open_url(self, url, alias=None):
        self.session.open_browser(url,browser=self.browser)
        self.session.open_browser(url, browser=self.browser, alias=alias,
                                 desired_capabilities={'acceptInsecureCerts': True})
        self.session.maximize_browser_window()
        self._browser_settings()

    def _browser_settings(self):
        self.session.set_selenium_timeout(self.selenium_timeout)
        self.session.set_browser_implicit_wait(self.implicit_wait)
        self.session.set_selenium_speed(self.selenium_speed)
        self.session.register_keyword_to_run_on_failure(self.run_on_failure)
        # self.session.set_screenshot_directory(self.screenshot_directory)

    def _open_browser_window(self, server, protocol='https', port=443, alias=None):
        url = "%s://%s:%s" % (protocol, server, port)
        self.session.open_browser(url, browser=self.browser, alias=alias,
                                  desired_capabilities={'acceptInsecureCerts': True})
        self.session.maximize_browser_window()
        self._browser_settings()

    def click_element(self, locator, action_chain=False):
        """
            Click element identified by `locator`.

            Key attributes for arbitrary elements are `id` and `name`. See
            `introduction` for details about locating elements.

            @param locator: identifier to the elements along with locator
                            strategy to be used
            @type locator: String
            @param action_chain: True/False -It is used to click element by performing action

        """
        for i in range(3):
            try:
                self.session.scroll_element_into_view(locator)
                self.session.wait_until_element_is_visible(locator)
                if action_chain is True:
                    self._click_element_with_action_chain(locator)
                else:
                    self.session.click_element(locator)
                break
            except:
                if i in range(2):
                    self.builtin.sleep(2)
                else:
                    self.screenshot()
                    raise
    def input_text(self, locator, text):
        for i in range(3):
            try:
                self.session.scroll_element_into_view(locator)
                self.session.wait_until_element_is_visible(locator)
                self.session.input_text(locator, text)
                break

            except:
                if i in range(2):
                    self.builtin.sleep(2)
                else:
                    self.screenshot()
                    raise

    def get_text(self, locator):
        for i in range(3):
            try:
                self.session.wait_until_element_is_visible(locator)
                value = self.session.get_text(locator)
                break
            except:
                if i in range(2):
                    self.builtin.sleep(2)
                else:
                    self.screenshot()
                    raise
        return value


    def click_button(self, locator, action_chain=False):
        """
            Click button identified by `locator`.

            Key attributes for arbitrary elements are `id` and `name`. See
            `introduction` for details about locating elements.

            @param locator: identifier to the elements along with locator
                            strategy to be used
            @type locator: String
            @param action_chain: True/False -It is used to click element by performing action

        """
        for i in range(3):
            try:
                self.session.scroll_element_into_view(locator)
                self.session.wait_until_element_is_visible(locator)
                if action_chain is True:
                    self._click_element_with_action_chain(locator)
                else:
                    self.session.click_button(locator)
                break
            except:
                if i in range(2):
                    self.builtin.sleep(2)
                else:
                    self.screenshot()
                    raise

    def select_element_by_label(self, locator, label, action_chain=False):
        """
            select element with given 'label' as identified by `locator`.

            Key attributes for arbitrary elements are `id` and `name`. See
            `introduction` for details about locating elements.

            @param locator: identifier to the elements along with locator
                            strategy to be used
            @type locator: String
            @param action_chain: True/False -It is used to click element by performing action

        """
        for i in range(3):
            try:
                self.session.wait_until_element_is_visible(locator)
                if action_chain is True:
                    self._click_element_with_action_chain(locator)
                else:
                    self.session.select_from_list_by_label(locator,label)
                break
            except:
                if i in range(2):
                    self.builtin.sleep(2)
                else:
                    self.screenshot()
                    raise
 
