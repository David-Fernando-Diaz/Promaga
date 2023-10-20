import pandas as pd
titanic_data = pd.read_csv('titanic.csv')  
sobrevivieron = titanic_data['survived'].sum()
Nosobrevivieron = len(titanic_data) - sobrevivieron
print("Cantidad de pasajeros que sobrevivieron:", sobrevivieron)
print("Cantidad de pasajeros que no sobrevivieron:", Nosobrevivieron)
