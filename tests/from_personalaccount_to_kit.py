from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_from_personalaccount_to_kit(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.BUTTON_KIT).click()
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/'
