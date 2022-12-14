import pytest
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1440, 900)
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()