from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Принимаем куки')
    def click_on_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step('Скролл страницы до последнего вопроса')
    def scroll_page_to_last_question(self):
        self.scroll_page(MainPageLocators.QUESTION_LAST)

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, number):
        question_loc = self.reformate_locator(MainPageLocators.QUESTION, number)
        self.click_on_element(question_loc)

    @allure.step('Получаем текст ответа')
    def get_text_from_answer(self, number):
        answer_loc = self.reformate_locator(MainPageLocators.ANSWER, number)
        return self.get_text_from_element(answer_loc)

    @allure.step('Клик на вопрос и получение текста ответа')
    def click_to_question_get_answer(self, number):
        self.click_on_question(number)
        return self.get_text_from_answer(number)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button(self, button):
        self.click_on_element(button)

    @allure.step('Клик на лого Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Поиск кнопки "Найти" на странице Дзена')
    def search_find_button(self):
        self.switch_to_second_browser_window()
        self.find_element_and_wait(MainPageLocators.BUTTON_FIND)