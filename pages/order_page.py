import allure
import generators
from locators.order_page_locators import OrderPageLocators, Flags
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def set_name(self):
        name = generators.generate_name()
        self.set_text_to_element(OrderPageLocators.INPUT_FIELD_NAME, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_surname(self):
        surname = generators.generate_surname()
        self.set_text_to_element(OrderPageLocators.INPUT_FIELD_SURNAME, surname)

    @allure.step('Заполнение поля "Адрес доставки"')
    def set_address(self):
        address = generators.generate_address()
        self.set_text_to_element(OrderPageLocators.INPUT_FIELD_ADDRESS, address)

    @allure.step('Выбор станции метро')
    def select_metro_station(self):
        metro_station = generators.generate_station()
        self.click_on_element(OrderPageLocators.INPUT_FIELD_METRO_STATION)
        locator = self.reformate_locator(OrderPageLocators.STATION_DROP_DOWN, metro_station)
        self.click_on_element(locator)

    @allure.step('Заполнение поля "Номер телефона"')
    def set_phone(self):
        phone = generators.generate_phone()
        self.set_text_to_element(OrderPageLocators.INPUT_FIELD_PHONE, phone)

    @allure.step('Заполняем поля "Для кого самокат"')
    def set_data_for_whom_scooter(self):
        self.set_name()
        self.set_surname()
        self.set_address()
        self.select_metro_station()
        self.set_phone()

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбираем дату доставки самоката')
    def set_date(self, date):
        self.set_text_to_element(OrderPageLocators.INPUT_FIELD_DATE, date)
        self.click_on_element(OrderPageLocators.TITLE)

    @allure.step('Выбираем срок аренды самоката')
    def select_rental_period(self):
        rental_period = generators.generate_rental_period()
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DD)
        locator = self.reformate_locator(OrderPageLocators.RENTAL_PERIOD_BUTTON_IN_DD, rental_period)
        self.click_on_element(locator)

    @allure.step('Выбор цвета самоката')
    def select_color(self):
        color = generators.generate_color()
        locator = self.reformate_locator(OrderPageLocators.INPUT_FIELD_COLOR, color)
        self.click_on_element(locator)

    @allure.step('Заполнение поля "Комментарий"')
    def set_comment(self):
        comment = generators.generate_comment()
        self.set_text_to_element(OrderPageLocators.INPUT_FIELD_COMMENT, comment)

    @allure.step('Заполняем поля "Про Аренду"')
    def set_data_about_rent(self, date):
        self.set_date(date)
        self.select_rental_period()
        self.select_color()
        self.set_comment()

    @allure.step('Нажатие на кнопку "Заказать" и подтверждение заказа')
    def click_on_order_then_confirm_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def check_order_is_done(self):
        result = self.get_text_from_element(OrderPageLocators.ORDER_STATUS_BUTTON)
        return result == Flags.SUCCESSFUL_ORDER_FLAG

    @allure.step('Клик на логотип Самокат в шапке')
    def click_on_logo_scooter(self):
        self.click_on_element(OrderPageLocators.LOGO_SCOOTER)