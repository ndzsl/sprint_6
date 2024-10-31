import allure
from data import Urls
from locators.main_page_locators import MainPageLocators

class TestPageNavigation:

    @allure.title('Проверка редиректа на страницу Дзена по клику на логотип "Яндекс"')
    def test_yandex_logo_redirects_to_dzen(self, main_page):
        main_page.get_url(Urls.MAIN_PAGE_URL)
        main_page.click_on_logo_yandex()
        main_page.search_find_button()
        assert main_page.get_current_url() == Urls.DZEN_URL

    @allure.title('Проверка возврата на главную страницу Самоката по клику на логотип "Самокат"')
    def test_scooter_logo_navigates_to_home_page(self, main_page, order_page):
        main_page.get_url(Urls.MAIN_PAGE_URL)
        main_page.click_on_order_button(HomePageElements.ORDER_BUTTON_IN_HEADER)
        order_page.click_on_logo_scooter()
        assert main_page.get_current_url() == Urls.MAIN_PAGE_URL