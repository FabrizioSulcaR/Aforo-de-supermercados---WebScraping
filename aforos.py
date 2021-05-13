# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Usuario\\Desktop\\Scrapping\\Practice\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

#Inicializamos el chrome
driver.get('https://visitaresponsable.produce.gob.pe/')

#Busqueda de locales
#Busqueda de Ate
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[2]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]")))\
    .click()

#Seleccionar Bellavista
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[3]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]")))\
    .click()

#Seleccionar Breña
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[4]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[3]")))\
    .click()

#Seleccionar Cajamarca
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[5]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[4]")))\
    .click()

### Notamos que el último div[i] es el # de entrada en el filtrador
### Notamos que el último div[i] e el # de opción en el select -> cambia esto y cambias local

#Seleccionar Callao
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[6]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[5]")))\
    .click()

#Seleccionar Callería
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[7]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[6]")))\
    .click()

#Seleccionar Castilla
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[8]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[7]")))\
    .click()

#Seleccionar Cayma
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[9]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[8]")))\
    .click()

#Seleccionar Cerro Colorado
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[10]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[9]")))\
    .click()

#Seleccionar Chiclayo
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[11]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[10]")))\
    .click()

#Seleccionar Chorrillos
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[12]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[11]")))\
    .click()

#Seleccionar Comas
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[13]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[12]")))\
    .click()

#Seleccionar Cusco
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[14]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[13]")))\
    .click()

#Seleccionar Huacho
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[15]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[14]")))\
    .click()

#Seleccionar Huancayo
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[16]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[15]")))\
    .click()

#Seleccionar Huánuco
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[17]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[16]")))\
    .click()

#Seleccionar Ica
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[18]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[17]")))\
    .click()

#Seleccionar Independencia
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[19]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[18]")))\
    .click()

#Seleccionar Jesús María
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[20]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[19]")))\
    .click()

#Seleccionar Juliaca
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[21]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[20]")))\
    .click()

#Seleccionar Lima
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[22]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[21]")))\
    .click()

#Seleccionar Paucarpata
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[23]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[22]")))\
    .click()

#Seleccionar Piura
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[24]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[23]")))\
    .click()

#Seleccionar San Borja
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[25]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[24]")))\
    .click()

#Seleccionar San Juan de Miraflores
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[26]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[25]")))\
    .click()

#Seleccionar San Martin de Porres
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[27]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[26]")))\
    .click()

#Seleccionar San Miguel
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[28]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[27]")))\
    .click()

#Seleccionar Santa Anita
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[29]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[28]")))\
    .click()

#Seleccionar Santiago de Surco
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[30]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[29]")))\
    .click()

#Seleccionar Surquillo
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[31]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[30]")))\
    .click()

#Seleccionar Trujillo
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[32]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[31]")))\
    .click()

#Seleccionar Villa Maria del Triunfo
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[33]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[32]")))\
    .click()

#Seleccionar Yarinacocha
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/div/div/div[34]/input')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/app-root[1]/app-home/div[3]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[33]")))\
    .click()

time.sleep(20)
#Distritos
distritos = driver.find_elements_by_xpath("//div[@class = 'col-sm-12 cuadro-region no-gutters' or @class='col-sm-12 cuadro-region-rojo no-gutters']")
time.sleep(2)

list_distritos = []
for distrito in distritos:
    list_distritos.append(distrito.text)

#Malls
malls = driver.find_elements_by_xpath("//div[@class = 'col-sm-12 cuadro-nombrecc' or @class='col-sm-12 cuadro-nombrecc-rojo']")
time.sleep(2)

list_malls = []
for mall in malls:
    list_malls.append(mall.text)

#Dirección
direccion = driver.find_elements_by_xpath("//div[@class='col-sm-12 cuadro-direccion' or @class='col-sm-12 cuadro-direccion-rojo']")
time.sleep(2)

list_directions = []
for direction in direccion:
    list_directions.append(direction.text)

#Porcentaje limite
porcentaje_limite = driver.find_elements_by_xpath('//h3[@class="texto-datos-verde2" or @class="texto-datos-rojo2"]')
time.sleep(2)

list_limits = []
for limit in porcentaje_limite:
    list_limits.append(limit.text)

#Porcentaje actual
porcentaje_actual = driver.find_elements_by_xpath('//h3[@class="texto-datosn"]')
time.sleep(2)

list_porcentaje_actual = []
for p_actual in porcentaje_actual:
    list_porcentaje_actual.append(p_actual.text)

#Aforo actual
aforos_actuales = driver.find_elements_by_xpath('//p[@class="texto-aforoactual"]')
time.sleep(2)

list_aforo_actual = []
for aforo_actual in aforos_actuales:
    list_aforo_actual.append(((aforo_actual).text).replace(" personas aforo actual"," "))

#Aforo total
aforos_totales = driver.find_elements_by_xpath('//h3[@class="texto-datosn2"]')
time.sleep(2)

list_aforo_total = []
for aforo_total in aforos_totales:
    list_aforo_total.append(aforo_total.text)

#Ultima Actualizacion
actualizaciones = driver.find_elements_by_xpath('//p[@class="texto-comentario"]/span')
time.sleep(2)

list_actualizacion = []
for actualizacion in actualizaciones:
    list_actualizacion.append(actualizacion.text)
driver.quit()
#Guardado de datos
df = pd.DataFrame({'Distritos':list_distritos, 'Malls':list_malls, 'Direccion':list_directions, 'Limite':list_limits, 'Porcentaje actual':list_porcentaje_actual, 'Aforo actual':list_aforo_actual, 'Aforo total':list_aforo_total, 'Actualizacion':list_actualizacion})

print(df)

df.to_csv('data.csv', index=False, encoding='utf-8')
