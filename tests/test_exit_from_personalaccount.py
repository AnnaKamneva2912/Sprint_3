from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_exit_from_personal_account(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_EXIT)))
    driver.find_element(*TestLocators.BUTTON_EXIT).click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
