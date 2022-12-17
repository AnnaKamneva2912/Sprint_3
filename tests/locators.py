from selenium.webdriver.common.by import By
class TestLocators:
    # кнопка Зарегистрироваться
    BUTTON_TO_GO_REGISTER = By.LINK_TEXT, "Зарегистрироваться"
    # поле Имя в форме регистрации
    FIELD_NAME = By.NAME, "name"
    # поле Email в форме регистрации
    FIELD_EMAIL = By.XPATH, '//fieldset[2]/div/div/input'
    # поле Пароль в форме регистрации
    FIELD_PASSWORD_REGISTRATION = By.NAME, "Пароль"
#   #кнопка регистрации в форме регистрации
    BUTTON_REGISTER = By.XPATH, '//form/button'
    #кнопка Войти в аккаунт
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]'
    #поле Email в форме входа
    FIELD_EMAIL_ENTERFORM = By.NAME, "name"
    #поле Пароль в форме входа
    FIELD_PASSWORD_ENTERFORM = By.XPATH, '//*[@type="password"]'
    #кнопка Войти в форме входа
    BUTTON_ENTER_ENTERFORM = By.XPATH, '//form/button'
    #кнопка Личный кабинет
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, 'html/body/div/div/header/nav/a'
    #кнопка Начинки
    BUTTON_FILLING = By.XPATH, '//span[text()="Начинки"]'
    #кнопка Соусы
    BUTTON_SOUCE = By.XPATH, '//span[text()="Соусы"]'
    #кнопка Булки
    BUTTON_BUN = By.XPATH, '//span[text()="Булки"]'
    #логотип SB
    SB_LOGO = By.XPATH, '//header/nav/div'
    #кнопка Конструктор
    BUTTON_KIT = By.TAG_NAME, "a"
    #кнопка выход в личном кабинете
    BUTTON_EXIT = By.XPATH, '//button[text()="Выход"]'
    #восстановить пароль
    RESTORE_PASSWORD = By.LINK_TEXT, "Восстановить пароль"
    # кнопка войти в форме восстановления пароля
    ENTER_BUTTON = By.LINK_TEXT, "Войти"
    # переход ко вкладке Булки
    DISPLAYED_BUN = By.XPATH, '//*[@alt="Флюоресцентная булка R2-D3"]'
    # переход ко вкладке Начинки
    DISPLAYED_FILLING = By.XPATH, '//*[@alt="Говяжий метеорит (отбивная)"]'
    # переход ко вкладке соусы
    DISPLAYED_SOUCE = By.XPATH, '//*[@alt="Соус Spicy-X"]'
    # КНОПКА Сохранить
    BUTTON_SAVE = By.XPATH, '//button[text()="Сохранить"]'



