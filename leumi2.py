from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select


import os
import leumi.constants as const

class Luemi2(webdriver.Chrome):
    def __init__(self, driver_path=r"/usr/local/bin", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Luemi2, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.CACL_URL)


    def fill_dates(self):
        hurt_date = self.find_element_by_id("ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_DynDatePicker_PguiaDate_Date")
        brth_date = self.find_element_by_id("ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_DynDatePicker_BirthDate_Date")

        hurt_date.send_keys("25/1/2000")
        brth_date.send_keys("18/7/1990")

        self.find_element_by_id("ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_StartNavigationTemplateContainerID_StartNextButton").click()


    def click_continue_btn(self):
        continue_btn = self.find_element_by_id("ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_StartNavigationTemplateContainerID_StartNextButton")
        # self.implicitly_wait(15)
        # WebDriverWait(self, 10).until(expected_conditions.element_to_be_selected(continue_btn))
        continue_btn.click()


    def drop_down_percent(self):
        percent = self.find_element_by_id("ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_Percent")
        percent.send_keys("50")
        drop_down_element = self.find_element_by_id("ctl00_ctl49_g_0339dd53_9d84_4774_b0c6_a578bf46ed47_ctl00_WorkDisabilityWizard_ddl_Type")
        drp = Select(drop_down_element)
        drp.select_by_value("1")

