from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_1_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.NAME, "name").send_keys("Anna")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[3]/div/div/input').send_keys("1234A!")
    driver.find_element(By.XPATH, '//form/button').click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/register'
    driver.quit()

def test_2_registration_wrong_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.NAME, "name").send_keys("Anna")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[3]/div/div/input').send_keys("123")
    driver.find_element(By.XPATH, '//form/button').click()

    assert driver.find_element(By.XPATH, '//fieldset[3]/div/div').get_attribute('class') == 'input pr-6 pl-6 input_type_password input_size_default input_status_error'


def test_3_enter_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, '//section[2]/div/button').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, '//fieldset[1]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("1234A!")
    driver.find_element(By.XPATH, '//form/button').click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_4_enter_personal_access():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, 'html/body/div/div/header/nav/a').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, '//fieldset[1]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("1234A!")
    driver.find_element(By.XPATH, '//form/button').click()
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_enter_restore_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, '//section[2]/div/button').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.LINK_TEXT, "Войти").click()
    driver.find_element(By.XPATH, '//fieldset[1]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("1234A!")
    driver.find_element(By.XPATH, '//form/button').click()
    WebDriverWait(driver, 10)
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()