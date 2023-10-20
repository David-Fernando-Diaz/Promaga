import pandas as pd

# Carga el archivo CSV con los datos de los estudiantes (asegúrate de proporcionar la ruta correcta)
estudiantes_data = pd.read_csv('estudiantes.csv')

# Calcula el promedio de edad de los estudiantes
promedio_edad = estudiantes_data['Edad'].mean()

# Calcula el promedio de calificaciones de los estudiantes
promedio_calificaciones = estudiantes_data['Calificaciones'].mean()

# Selecciona a los estudiantes que perdieron la asignatura (por ejemplo, calificación menor a 5)
perdieron_asignatura = estudiantes_data[estudiantes_data['Calificaciones'] < 5]

# Calcula la cantidad de estudiantes que están entre el 10% mejor (por ejemplo, los que tienen las calificaciones más altas)
porcentaje_mejor = 10
cantidad_estudiantes = len(estudiantes_data)
cantidad_mejor = int(cantidad_estudiantes * porcentaje_mejor / 100)
mejores_estudiantes = estudiantes_data.nlargest(cantidad_mejor, 'Calificaciones')

# Imprime los resultados
print("Promedio de edad de los estudiantes:", promedio_edad)
print("Promedio de calificaciones de los estudiantes:", promedio_calificaciones)
print("\nEstudiantes que perdieron la asignatura:")
print(perdieron_asignatura)
print("\nEstudiantes entre el 10% mejor:")
print(mejores_estudiantes)
