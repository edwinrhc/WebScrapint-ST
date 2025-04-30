import requests
from bs4 import BeautifulSoup
import csv
import time
import random

url = "https://www.transparencia.gob.pe/enlaces/pte_transparencia_enlaces.aspx?id_entidad=38934&id_tema=1&ver=D"  # cambia esta URL por la real

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    enlaces = soup.find_all('a')

    variable = "Res. U. A. N"
    variable_norm = variable.casefold()
    # Abrimos archivo CSV
    with open("resoluciones.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter="|",quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Nombre del Enlace", "URL"])  # encabezado

        for enlace in enlaces:
            texto = enlace.get_text(strip=True)
            if texto.lower().startswith(variable_norm):
                href = enlace.get('href')
                # Escribimos fila en CSV
                writer.writerow([texto, href])

                print(f"{texto} - {href}")

    print("\n✅ Enlaces guardados correctamente en 'enlaces.csv'")
    time.sleep(random.uniform(2, 6))
else:
    print(f"❌ Error al acceder a la página: {response.status_code}")
