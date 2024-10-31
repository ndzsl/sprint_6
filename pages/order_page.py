from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
import allure


class BasePage:

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход по URL')
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step('Ожидание и поиск элемента на странице')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Получение текста элемента')
    def fetch_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Ввод текста в элемент')
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    @allure.step('Прокрутка страницы до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локатора')
    def format_locator(self, locator, number):
        method, locator = locator
        formatted_locator = locator.format(number)
        return method, formatted_locator

    @allure.step('Переключение на вторую вкладку')
    def switch_to_second_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получение текущего URL')
    def current_url(self):
        return self.driver.current_url