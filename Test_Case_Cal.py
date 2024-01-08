from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import pytest



class Test_Case_Calendar:
    
    def test_calendar(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        calendarButton=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/section[1]/div[2]/div")
        calendarButton.click()
        headerLogo=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[1]/span")))
        assert headerLogo.text =="Eğitim ve Etkinlik Takvimi"
        educationInput=self.driver.find_element(By.ID,"search-event")
        educationInput.send_keys("Yazılım Kalite ve Test Uzmanı - 1A")
        textLogo=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/a/div/span[2]")))
        assert textLogo.text =="Yazılım Kalite ve Test Uzmanı - 1A"
        sleep(10)

    
    def test_educator(self):
         self.driver=webdriver.Chrome()
         self.driver.get("https://tobeto.com/giris")
         self.driver.set_window_size(1552, 840)
         element = self.driver.find_element(By.XPATH, "//div[@id=\'__next\']/div/section/nav/div/ul/li[4]/a")
         actions = ActionChains(self.driver)
         actions.move_to_element(element).perform()
         self.driver.find_element(By.XPATH, "//div[@id=\'__next\']/div/section/div[2]/div").click()
         self.driver.find_element(By.XPATH, "//div[2]/div/div/div[2]").click()
         self.driver.find_element(By.XPATH, "//div[@id=\'react-select-2-listbox\']/div/div").click()
         assert self.driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/div/div").text =="İrem Balcı"
         self.driver.find_element(By.CSS_SELECTOR, ".css-v7duua > .css-8mmkcg").click()
         sleep(5)
         self.driver.close()

    def test_educato(self):
         self.driver=webdriver.Chrome()
         self.driver.get("https://tobeto.com/giris")
         self.driver.set_window_size(1552, 840)
         self.driver.find_element(By.XPATH, "//div[@id=\'__next\']/div/section/div[2]/div").click()
         self.driver.find_element(By.CSS_SELECTOR, ".css-8mmkcg").click()
         self.driver.find_element(By.XPATH, "//div[@id=\'react-select-2-listbox\']/div/div").click()
         assert self.driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/div/div").text == "İrem Balcı"
         self.driver.find_element(By.CSS_SELECTOR, ".css-v7duua > .css-8mmkcg").click()
         self.driver.close()

        

        
        