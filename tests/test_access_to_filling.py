from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_access_to_filling():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys("class_class@yandex.ru")
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys("1234A!")
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="Начинки"]')))
    driver.find_element(*TestLocators.BUTTON_FILLING).click()
    class1 = driver.find_element(*TestLocators.BUTTON_FILLING_CLASS).get_attribute('class')
    assert class1 == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'