from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_1_registration(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.BUTTON_TO_GO_REGISTER).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_NAME).send_keys("Anna")
    driver.find_element(*TestLocators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_REGISTRATION).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/register'


def test_2_registration_wrong_password(driver, email):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*TestLocators.BUTTON_TO_GO_REGISTER).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_NAME).send_keys("Anna")
    driver.find_element(*TestLocators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_REGISTRATION).send_keys("123")
    driver.find_element(*TestLocators.BUTTON_REGISTER).click()
    assert driver.find_element(*TestLocators.FIELD_PASSWORD_REGISTRATION).get_attribute('class') == 'input pr-6 pl-6 input_type_password input_size_default input_status_error'


def test_3_enter_account(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'

def test_4_enter_personal_access(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_enter_restore_password(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.RESTORE_PASSWORD).click()
    WebDriverWait(driver, 10)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    driver.find_element(*TestLocators.FIELD_EMAIL_ENTERFORM).send_keys(email)
    driver.find_element(*TestLocators.FIELD_PASSWORD_ENTERFORM).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTER_ENTERFORM).click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'

