import allure
import pytest
from locators.main_page_locators import MainPageLocators

class TestScooterOrder:
    @allure.title('Тест оформления заказа на самокат')
    @pytest.mark.parametrize('button_element, delivery_date',
                             [
                                 [MainPageLocators.HEADER_ORDER_BUTTON, '15.11.2024'],
                                 [MainPageLocators.HEADER_ORDER_BUTTON, '20.11.2024'],
                             ])
    def test_place_scooter_order(self, main_page_page, order_page, button_element, delivery_date):
        home_page.accept_cookies()
        home_page.click_order_button(button_element)
        order_page.fill_order_details()
        order_page.click_next()
        order_page.fill_rental_details(delivery_date)
        order_page.place_order_and_confirm()
        assert order_page.verify_order_success()