from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_click_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, '//section[2]/div/button').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, '//fieldset[1]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("1234A!")
    driver.find_element(By.XPATH, '//form/button').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, 'html/body/div/div/header/nav/a').click()
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/account'
    driver.quit()