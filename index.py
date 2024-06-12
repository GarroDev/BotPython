from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
OrigenVuelo = "Eldorado"
DetinoVuelo = "punta cana"
AerolineaOpc = "Avianca"
service = Service("Driver\chromedriver.exe")
chrome_options = Options()
bot = webdriver.Chrome(service=service, options=chrome_options)
bot.maximize_window()
time.sleep(3)

bot.get("https://www.viajesexito.com/")
time.sleep(5)

actions = ActionChains(bot)

actions.send_keys(Keys.TAB).pause(2).send_keys(Keys.ENTER).perform()

vueloyhotel = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]/a/p')
time.sleep(2)
vueloyhotel.click()
time.sleep(5)

Origen = bot.find_element(By.XPATH, "//input[@id='CityPredictiveFrom_netactica_airhotel']")
Origen.click()
time.sleep(5)
Origen1 = bot.find_element(By.XPATH, "//input[@id='popUpCityPredictiveFrom_netactica_airhotel']")
Origen1.click()
Origen1.send_keys(OrigenVuelo)
time.sleep(2)
Origen1.send_keys(Keys.ENTER)
time.sleep(2)

Destino = bot.find_element(By.XPATH, "//input[@id='CityPredictiveTo_netactica_airhotel']")
Destino.click()
time.sleep(5)
Destino1 = bot.find_element(By.XPATH, "//input[@id='popUpCityPredictiveTo_netactica_airhotel']")
Destino1.click()
Destino1.send_keys(DetinoVuelo)
Destino1.send_keys(Keys.ENTER)
time.sleep(5)

Fecha_Salida = bot.find_element(By.XPATH, "//input[@id='Date_netactica_air_hotel']")
Fecha_Salida.click()
time.sleep(5)
Fecha_Salida1 = bot.find_element(By.XPATH, "//div[@aria-label='Jueves, Junio 20, 2024']")
Fecha_Salida1.click()
time.sleep(5)

Fecha_Regreso = bot.find_element(By.XPATH, "//div[@aria-label='Jueves, Junio 27, 2024']")
Fecha_Regreso.click()
time.sleep(5)
Aceptar = bot.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
Aceptar.click()
time.sleep(5)

Habitacion = bot.find_element(By.XPATH, "//p[@id='txtNumPassengersPaquetesComplete']")
time.sleep(2)
Habitacion.click()
time.sleep(2)
AgregarHabitacion = bot.find_element(By.XPATH, "//button[@id='btbAddRoomtwopaquetes']")
time.sleep(2)
AgregarHabitacion.click()
time.sleep(2)
AceptarHabitacion = bot.find_element(By.XPATH, "//div[@class='col-12 text-right']//button[@id='btbClosePaxPopup']")
time.sleep(2)
AceptarHabitacion.click()
time.sleep(2)

#indica ventana actual
original_window = bot.current_window_handle

Busqueda = bot.find_element(By.XPATH,"//a[@id='sbm_netactica_airhotel']//p[contains(text(),'Buscar')]")
time.sleep(2)
Busqueda.click()
time.sleep(20)

#indica cambio de ventana
all_windows = bot.window_handles

for window in all_windows:
    if window != original_window:
        bot.switch_to.window(window)
        break

# Precio = bot.find_element(By.XPATH,"//p[@class='totalpackprice small-text-center price-extra money']//span[@class='currencyText'][normalize-space()='$ 19.522.518']")


# print("")
# print("Aeroliena: ")
# print("Precios: "+ Precio)
# print("")
# print("Aeroliena: " )
# print("Precios: " + Precio)


OpcionesAvanzadas = bot.find_element(By.XPATH,"//a[@id='aShowHideAdvanced']")
time.sleep(2)
OpcionesAvanzadas.click()
time.sleep(4)
SeleccionarAeorilinea = bot.find_element(By.XPATH,"//input[@id='txtAirlineCode']")
time.sleep(2)
SeleccionarAeorilinea.click()
time.sleep(3)
SeleccionarAeorilinea.send_keys(AerolineaOpc)
time.sleep(2)
SeleccionarAeorilinea.send_keys(Keys.ENTER)
time.sleep(2)
BuscarNuevo = bot.find_element(By.XPATH,"//input[@value='Buscar']")
time.sleep(2)
BuscarNuevo.click()
time.sleep(20)