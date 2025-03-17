import pandas as pd
import matplotlib.pyplot as pit

pais=['estados unidos','china','alemanha','japao','india']
pibpor=[51, 30, 7, 7, 5]

pit.figure(figsize=(8, 8))
pit.pie(pais ,pibpor=pibpor , autopct='%1.1f%%', shadow=True, startangle=90)

pit.title("faz o L")
pit.show()