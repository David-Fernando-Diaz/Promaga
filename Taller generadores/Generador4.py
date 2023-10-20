import json

empleados = [
    {
        "nombre": "Empleado 1",
        "salario": 50000,
        "departamento": "Ventas"
    },
    {
        "nombre": "Empleado 2",
        "salario": 80000,
        "departamento": "Tecnología"
    },
    {
        "nombre": "Empleado 3",
        "salario": 45000,
        "departamento": "Recursos Humanos"
    }
]

with open('empleados.json', 'w') as archivo_json:
    json.dump(empleados, archivo_json)

print("Datos de empleados exportados a empleados.json")
