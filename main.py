from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado.")

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.routes_page = UrbanRoutesPage(self.driver)

    def _prepare_comfort_order(self):
        self.routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.routes_page.select_supportive_plan()

    def test_set_route(self):
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_plan(self):
        self.routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.routes_page.select_supportive_plan()
        assert self.routes_page.get_current_selected_plan() == 'Comfort'

    def test_fill_phone_number(self):
        self._prepare_comfort_order()
        phone_number = data.PHONE_NUMBER
        self.routes_page.set_phone(phone_number)
        assert self.routes_page.get_phone() == phone_number

    def test_fill_card(self):
        self._prepare_comfort_order()
        self.routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.routes_page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        self._prepare_comfort_order()
        message = data.MESSAGE_FOR_DRIVER
        self.routes_page.set_message_for_driver(message)
        assert self.routes_page.get_message_for_driver() == message

    def test_order_blanket_and_handkerchiefs(self):
        self._prepare_comfort_order()
        self.routes_page.click_blanket_and_handkerchiefs_option()
        assert self.routes_page.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        self._prepare_comfort_order()
        self.routes_page.add_ice_cream(2)
        assert self.routes_page.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self):
        self._prepare_comfort_order()
        self.routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.wait_order_taxi_popup().is_displayed()
        popup_title = self.routes_page.get_order_popup_title()
        assert len(popup_title) > 0

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()