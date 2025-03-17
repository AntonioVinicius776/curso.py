import pandas as pd
import matplotlib.pyplot as pit

labels=['a','b','c','d','e']
sizes=[51, 30, 7, 7, 5]

pit.figure(figsize=(8, 8))
pit.pie(labels , sizes=sizes, autopct='%1.1f%%',shadow=True , startangle=90 )

pit.title("faz o L")
pit.legend()
pit.show()