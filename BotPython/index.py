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

service = Service("D:\BotPython\Driver\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
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

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[4]/div/div[4]/div/div[2]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del primer paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del segundo paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del tercero paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del cuarto paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del quinto paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del sexto paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del septimo paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del octavo paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del noveno paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del decimo paquete es {textPrecio}")

Precio = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
textPrecio = Precio.text
print(f"el precio del undecimo paquete es {textPrecio}")


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
time.sleep(15)


plano = bot.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div")
textPlano = plano.text

# Guarda el texto en un archivo TXT
nombre_archivo = 'InfoAeroSelected.txt'
with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write(textPlano)

print(f'Se ha guardado la información en {nombre_archivo}')

bot.save_screenshot('ScreenShotAvianca.png')

print(f'Se ha tomado el ScreenShot')

bot.quit()

