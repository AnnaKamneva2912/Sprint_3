import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture()
def password():
    password = "1234A!"
    return password
@pytest.fixture()
def email():
    email = "class_class@yandex.ru"
    return email



