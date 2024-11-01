from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.XPATH, '//div[@id = "accordion__heading-{}"]'  # Локатор Вопроса

    QUESTION_LAST = By.XPATH, '//div[@id = "accordion__heading-7"]'  # Локатор последнего вопроса

    ANSWER = By.XPATH, '//div[@id = "accordion__panel-{}"]'  # Локатор ответа

    COOKIE = By.XPATH, '//button[text() = "да все привыкли"]'  # Кнопка принятия куков

    ORDER_BUTTON_IN_HEADER = By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'  # Кнопка "заказать" в шапке

    ORDER_BUTTON_IN_FOOTER = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'  # Кнопка "Заказать" в подвале

    BUTTON_FIND = By.XPATH, '//*[text() = "Найти"]'  # Кнопка "Найти" на стрнице Дзена

    LOGO_YANDEX = By.XPATH, '//*[@href = "//yandex.ru"]'  # Логотип Яндекс