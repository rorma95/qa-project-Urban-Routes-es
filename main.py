import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

#------------------------------------------------------------------------------------------------------------------------------

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

#------------------------------------------------------------------------------------------------------------------------------

class UrbanRoutesPage:                                  #localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    logo = (By.CLASS_NAME, "logo")                      # Correccion para espera
    results = (By.CLASS_NAME, "results-text")           # Correccion para espera
    ask_a_taxi = (By.CLASS_NAME, "button.round")
    tariff = (By.CLASS_NAME, "tariff-picker.shown")
    comfort = (By.XPATH, "//div[text()='Comfort'] ")
    add_phone_number = (By.CLASS_NAME, "np-text")
    cellphone_number = (By.ID,"phone")
    next_button = (By.CLASS_NAME, "button.full")
    code = (By.ID,"code")
    confirm_code = (By.XPATH, "//button[text()='Confirmar']")
    payment_method = (By.CLASS_NAME, "pp-text")
    add_card = (By.XPATH, "//img[contains(@src,'/static/media/card.411e0152.svg')]")
    card_number = (By.ID, "number")
    card_code = (By.XPATH, "//input[@placeholder='12']")
    add_button = (By.XPATH, "//button[text()='Agregar']")
    close_payment = (By.XPATH, '//div[@class="payment-picker open"]/div/div[@class="section active"]/button[@class="close-button section-close"]')
    driver_message = (By.ID, "comment")
    blanket_n_scarves = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]') #click derecho/copy/copy XPATH
    two_icecream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    final_ask_taxi = (By.CLASS_NAME, "smart-button-secondary")
    order_summary = (By.CLASS_NAME, "number")
    blanket_prove = (By.XPATH, " //div[text()='Manta y pañuelos']")
    checkbox = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    number_of_icecream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    final_button = (By.CLASS_NAME, "smart-button-main")
    driver_rating = (By.CLASS_NAME, "order-btn-rating")   # Correccion para espera
    cards = (By.CLASS_NAME, "tariff-cards")

# ------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):  # (0)>
        self.set_from(address_from)
        self.set_to(address_to)

    def click_ask_a_taxi(self): # (0)>
        self.driver.find_element(*self.ask_a_taxi).click()

    def select_comfort_tariff(self):    # (0)>
        self.driver.find_element(*self.comfort).click()

    def wait_for_results(self):                          # Correccion para espera
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.results))

    def get_confirmation_taxi(self):
        return self.driver.find_element(*self.cards).is_displayed()

    def get_comfort_tariff_prove(self):
        return self.driver.find_element(*self.blanket_prove).text

    def wait_open_page(self):                           # Correccion para espera
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.logo))

# ---------------------------------------------------------------------------------------------------

    def click_phone_number(self):   # (0)>
        self.driver.find_element(*self.add_phone_number).click()

    def add_number(self,cellphone): # (0)>
        self.driver.find_element(*self.cellphone_number).send_keys(cellphone)

    def click_next_button(self):    # (0)>
        self.driver.find_element(*self.next_button).click()

    def add_sms_code(self, code):    # (0)>
        self.driver.find_element(*self.code).send_keys(code)

    def click_confirm_code(self):   # (0)>
        self.driver.find_element(*self.confirm_code).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.cellphone_number).get_property('value')

# ---------------------------------------------------------------------------------------------------

    def click_payment(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()

    def add_number_card(self, number_card):
        self.driver.find_element(*self.card_number).send_keys(number_card)

    def add_card_code(self, cvv):
        self.driver.find_element(*self.card_code).send_keys(cvv)

    def open_add_button(self):
        self.driver.find_element(*self.card_number).click()

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def close_payment_method(self):
        self.driver.find_element(*self.close_payment).click()

    def set_credit_card(self,number_card,code_card):
        self.click_payment()
        self.click_add_card()
        self.add_number_card(number_card)
        self.add_card_code(code_card)
        self.open_add_button()
        self.click_add_button()
        self.close_payment_method()

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.card_code).get_property('value')

# ------------------------------------------------------------------------------------------------------------------------------

    def add_message_for_driver(self, text):
        self.driver.find_element(*self.driver_message).send_keys(text)

    def get_driver_message(self):
        return self.driver.find_element(*self.driver_message).get_property('value')

    def ask_blanket_n_scarves(self):
        self.driver.find_element(*self.blanket_n_scarves).click()

    def check_blanket_n_scarves_is_selected(self):
        return self.driver.find_element(*self.checkbox).is_selected()

# ------------------------------------------------------------------------------------------------------------------------------

    def ask_one_icecream(self):
        self.driver.find_element(*self.two_icecream).click()

    def ask_two_icecream(self):
        self.driver.find_element(*self.two_icecream).click()

    def set_ice_creams(self):
        self.ask_one_icecream()
        self.ask_two_icecream()

    def check_number_of_icecream(self):
        return self.driver.find_element(*self.number_of_icecream).text

# ------------------------------------------------------------------------------------------------------------------------------

    def click_final_ask_taxi(self):
        self.driver.find_element(*self.final_ask_taxi).click()

    def wait_for(self): # (0)>
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.order_summary)) # (0)>

    def check_final_button(self):
        return self.driver.find_element(*self.final_button).text

    def get_driver_rating(self):
        return self.driver.find_element(*self.driver_rating).is_displayed()


#------------------------------------------------------------------------------------------------------------------------------

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

        """
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
"""

    def test_set_route(self):                                                   # ingresamos las direcciones en el campo Desde y Hasta, Comprobamos si son las direcciones que ingresamos
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_open_page()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_taxi_button(self):                                                 # Hacemos click en el boton de pedir un taxi
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_results()
        routes_page.click_ask_a_taxi()
        assert routes_page.get_confirmation_taxi() == True

    def test_comfort_click(self):                                               # Seleccionamos la tarifa Comfort, comprobamos que se haya seleccionado la tarifa Comfort comprobando uno de los elementos que se pueden agregar
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert routes_page.get_comfort_tariff_prove() == 'Manta y pañuelos'

    def test_phone_number(self):                                                # Se agrega un numero de telefono y el codigo obtenido, se comprueba que ambos campos se han completado con los valores correctos
        routes_page = UrbanRoutesPage(self.driver)
        test_number = data.phone_number
        routes_page.click_phone_number()
        routes_page.add_number(test_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(driver=self.driver)
        routes_page.add_sms_code(code)
        routes_page.click_confirm_code()
        assert routes_page.get_phone_number() == test_number



    def test_payment(self):                                                     # Agregar una TDC como medio de pago, validar que los campos sean los correctos.
        routes_page = UrbanRoutesPage(self.driver)
        number_card = data.card_number
        code_card = data.card_code
        routes_page.set_credit_card(number_card,code_card)
        assert routes_page.get_card_number() == number_card
        assert routes_page.get_card_code() == code_card

    def test_message_to_driver(self):                                           # Agregar un mensaje para el conductor, validar que sea el adecuado
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.add_message_for_driver(message)
        assert routes_page.get_driver_message() == message

    def test_ask_for_blanket_n_scarves(self):                                   # Añadir una manta y pañuelos al pedido, comprobar que el elemento este seleccionado
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.ask_blanket_n_scarves()
        assert routes_page.check_blanket_n_scarves_is_selected() == True


    def test_ask_for_two_icecream(self):                                        # Agregar dos Helados al pedido, comprobar que sse hayan agregado solo 2 ingredientes
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_ice_creams()
        assert routes_page.check_number_of_icecream() == '2'

    def test_final_taxi_button(self):                                           # Hacer click en el boto para realizar la solicitud de un taxi
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_final_ask_taxi()
        assert "Pedir un taxi" in routes_page.check_final_button()

    def test_final_page(self):                                                  # Espera a que se asigne un conductor
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for()
        assert routes_page.get_driver_rating() == True
        time.sleep(2)                                                           # Lo deje solo para  ver que se  realizaron  correctamente las   demas pruebas

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

#------------------------------------------------------------------------------------------------------------------------------