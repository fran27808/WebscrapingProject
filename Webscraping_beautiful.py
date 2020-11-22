import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')  # para entrar en modo incógnito
#options.add_argument('--headless') # para realizar webscraping sin abrir el navegador
driver = webdriver.Chrome(r"C:\Users\franc\archivos_datos/chromedriver.exe", options=options)

driver.implicitly_wait(5)

url = "https://trends.google.es/trends/?geo=ES"
driver.get(url)

# Hacer clic en el icono de la menú
driver.find_element_by_xpath('//*[@id="sidenav-menu-btn"]').click()
time.sleep(6)

# Clic en El año en búsquedas, para acceder a lo más destacado del año anterior
driver.find_element_by_xpath('//*[@id="sidenav-list-group-trends"]/md-item[4]/md-item-content/a').click()
time.sleep(6)

# Queremos que sean visible toda la información posible, por lo que mediante selenium clicamos todos los botones de "Mostrar más"
mostrar_mas = driver.find_elements_by_class_name("show-more")
for i in range(len(mostrar_mas)):
      driver.execute_script("arguments[0].click();", mostrar_mas[i])
      time.sleep(1)
page_source = driver.page_source


#Ahora que se muestra toda la info, recopilamos los datos
page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")
tendencias_2019 = []
categorias = soup.find_all('div', class_='expandable-list-header-text')
#eliminamos los tags del listado de categorias 2019
for categoria in categorias:
    a = str(categoria).replace("""<div bidi="fields.topic.value" class="expandable-list-header-text" dir="ltr" ng-class="{'mobile': ctrl.globals.isMobileMode}"><span ng-bind="bidiText">""", "")
    b = a.replace("""</span></div>""", "")
    tendencias_2019.append(b)
print(tendencias_2019)

tendencias_2019_2 = []
categorias_2 = soup.find_all('a', class_='fe-expandable-item-text')
#eliminamos los tags del listado de categorias 2019
for quitar in categorias_2:
    a = str(quitar).replace("""[<a class="fe-expandable-item-text" href="/trends/explore?date=2019-01-01%202019-12-31&amp;q=Elecciones%20generales&amp;geo=ES" ng-attr-title="{{::ctrl.tpYisService.createExploreStringForTooltip(value)}}" ng-href="/trends/explore?date=2019-01-01%202019-12-31&amp;q=Elecciones%20generales&amp;geo=ES" ng-if="!ctrl.isSmallTouchDevice &amp;&amp; ctrl.tpYisService.shouldDisplayListsExploreLinks()" target="_self" title=""", "")
    b = a.replace("""</a>""", "")
    tendencias_2019_2.append(b)

print(tendencias_2019_2)

