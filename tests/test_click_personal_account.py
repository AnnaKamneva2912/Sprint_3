from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_click_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys("class_class@yandex.ru")
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys("1234A!")
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Сохранить"]')))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
