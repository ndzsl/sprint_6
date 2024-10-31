from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы для вопросов и ответов с параметризацией
    QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]'  # Локатор для вопроса
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]'      # Локатор для ответа

    # Локатор последнего вопроса
    LAST_QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-7"]'

    # Кнопка для согласия с куками
    ACCEPT_COOKIES_BUTTON = By.XPATH, '//button[text()="да все привыкли"]'

    # Кнопки "Заказать" в шапке и подвале
    HEADER_ORDER_BUTTON = By.XPATH, '//button[contains(@class, "order_header")][text()="Заказать"]'
    FOOTER_ORDER_BUTTON = By.XPATH, '//button[contains(@class, "order_footer")][text()="Заказать"]'

    # Логотипы
    YANDEX_LOGO_LOCATOR = By.XPATH, '//*[@href="//yandex.ru"]'  # Логотип Яндекс
    SCOOTER_LOGO_LOCATOR = By.XPATH, '//*[@href="/"]'            # Логотип Самоката