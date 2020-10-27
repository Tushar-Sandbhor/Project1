from ..BasePage import BasePage
from .DashboardLocators import DashboardLocators as Locators
import os
import time
from pathlib import Path
class DashboardPage(BasePage):
    """
        This class includes the functions required to validate the details
        regarding the product to be search.
    """

    def logintosite(self, url):
        self.open_url(url)
        
    def filterdata(self,searchtext):
        self.session.click_element(Locators.popup)
        time.sleep(10)
        self.session.input_text(Locators.searchfield_locator, searchtext)
        self.session.press_keys(Locators.searchfield_locator,'ENTER')

    def getlabel(self):
        self.session.get_text(Locators.selectsortby)

    def getproductinfo(self,label):
        self.session.select_element_by_label(Locators.selectsortby,label)
        self.session.click_element(Locators.selectproduct)
        self.session.switch_window(Locators.switchwindow)
        name=self.session.get_text(Locators.getname)
        price=self.session.get_text(Locators.getprice)
        productdetails=self.session(Locators.getproductdescription)
        return[name,price,productdetails]

    
