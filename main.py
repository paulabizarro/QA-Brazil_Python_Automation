from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Validação do servidor adicionada no Sprint anterior
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado.")

        # Configuração com registro de logs de performance
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(5)

    # 1. Definir o endereço
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # 2. Selecionar o plano Comfort
    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_supportive_plan()
        assert routes_page.get_current_selected_plan() == 'Comfort'

    # 3. Preencher o número de telefone
    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.PHONE_NUMBER
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone() == phone_number

    # 4. Adicionar um cartão de crédito
    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_current_payment_method() == 'Cartão'

    # 5. Escrever um comentário para o motorista
    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.MESSAGE_FOR_DRIVER
        routes_page.set_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message

    # 6. Pedir um cobertor e lenços
    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_handkerchiefs_option()
        assert routes_page.get_blanket_and_handkerchiefs_option_checked()

    # 7. Pedir 2 sorvetes
    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream(2)
        assert routes_page.get_amount_of_ice_cream() == 2

    # 8. Pedir o táxi e verificar modal de busca
    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_buton()
        assert routes_page.wait_order_taxi_popup().is_displayed()

    # Teardown da classe
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()