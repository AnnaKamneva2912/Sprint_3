from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_access_to_sauce(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_SOUCE)))
    driver.find_element(*TestLocators.BUTTON_SOUCE).click()
    element = driver.find_element(*TestLocators.DISPLAYED_SOUCE)
    assert element.is_displayed()