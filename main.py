import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Tarefa 4: Verifica se o servidor Urban Routes está ativo antes de executar os testes
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Tarefa 3: Define a rota de origem e destino
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Tarefa 3: Seleciona a tarifa desejada (ex: Comfort)
        # Adicionar em S8
        print("função criada para selecionar a tarifa")
        pass

    def test_fill_phone_number(self):
        # Tarefa 3: Preenche o número de telefone e confirma o código
        # Adicionar em S8
        print("função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # Tarefa 3: Adiciona as informações do cartão de crédito
        # Adicionar em S8
        print("função criada para preencher o cartão de pagamento")
        pass

    def test_comment_for_driver(self):
        # Tarefa 3: Escreve a mensagem direcionada ao motorista
        # Adicionar em S8
        print("função criada para adicionar comentário ao motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Tarefa 3: Solicita os cobertores e lenços nos itens adicionais
        # Adicionar em S8
        print("função criada para pedir cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        # Tarefa 5: Estrutura o laço para pedir 2 sorvetes
        numbers_of_ice_creams = 2
        print("função criada para adicionar a quantidade de sorvetes")
        for count in range(numbers_of_ice_creams):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Tarefa 3: Valida se o modal de busca do veículo é exibido
        # Adicionar em S8
        print("função criada para verificar a exibição do modal de busca do carro")
        pass