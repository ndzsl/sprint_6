import allure
import pytest
from locators.main_page_locators import MainPageLocators


class TestOrderPage:
    @allure.title('Тест заказа самоката')
    @pytest.mark.parametrize('button, date',
                             [
                                 [MainPageLocators.ORDER_BUTTON_IN_HEADER, '27.10.2024'],
                                 [MainPageLocators.ORDER_BUTTON_IN_FOOTER, '07.11.2024']
                             ]
                             )
    def test_order_scooter(self, main_page, order_page, button, date):
        main_page.click_on_cookie()
        main_page.click_on_order_button(button)
        order_page.set_data_for_whom_scooter()
        order_page.click_next_button()
        order_page.set_data_about_rent(date)
        order_page.click_on_order_then_confirm_button()
        assert order_page.check_order_is_done()