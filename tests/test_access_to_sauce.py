from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_access_to_sauce():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, '//section[2]/div/button').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, '//fieldset[1]/div/div/input').send_keys("class_class@yandex.ru")
    driver.find_element(By.XPATH, '//fieldset[2]/div/div/input').send_keys("1234A!")
    driver.find_element(By.XPATH, '//form/button').click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="Соусы"]')))
    driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()

    class1 = driver.find_element(By.XPATH, '//section/div/div[2]').get_attribute('class')
    assert class1 == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'



