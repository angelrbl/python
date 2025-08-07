agenda = {
    "Pepi": "661761126",
    "Mamá": "606511406",
    "Papá": "636607214",
    "Yo": "665444949"
}

def commandList():
    print("Bienvenido a su agenda, por favor, seleccione una de las siguientes opciones:")
    print("(1) - Ver agenda")
    print("(2) - Buscar contacto")
    print("(3) - Añadir nuevo contacto")
    print("(4) - Eliminar contacto")
    print("(5) - Editar contacto existente")
    print("(0) - Salir", end='\n\n')
    action = int(input("¿Qué desea hacer?: "))

    if action == 1:
        verAgenda()
    elif action == 2:
        busCon()
    elif action == 3:
        addCon()
    elif action == 4:
        elimCon()
    elif action == 5:
        editCon()
    elif action == 0:
        exit()
    else:
        print('Esa opción no existe, por favor, pruebe de nuevo.', end='\n\n')
        commandList

def verAgenda():
    print('Mostrando los contactos de tu agenda:', end='\n\n')
    for key, value in agenda.items():
        print(f'{key}: {value}')
    print('\n')
    commandList()

def busCon():
    contacto = str(input("Por favor, escriba el nombre del contacto que desea buscar: "))
    if agenda.get(contacto):
        print(f"{contacto} se ha encontrado con éxito, su número es {agenda.get(contacto)}")
    else:
        print('El contacto no se ha podido encontrar en su agenda, por favor, búsquelo de nuevo o añádalo.')
    print('\n')
    commandList()

def addCon():
    nombre = str(input("Por favor, escriba el nombre del contacto a añadir: "))
    numero = str(input("Por favor, escriba el número del contacto a añadir: "))
    agenda.update({nombre: numero})
    print(f"{nombre}, con el número {numero} ha sido añadido con éxito.")
    print('\n')
    commandList()

def elimCon():
    contacto = str(input("Por favor, escriba el nombre del contacto a eliminar: "))
    if agenda.get(contacto):
        agenda.pop(contacto)
        print(f"{contacto} se ha eliminado con éxito de su agenda.")
    else:
        print('El contacto no se ha podido encontrar en su agenda, por favor, búsquelo de nuevo.')
    print('\n')
    commandList()

def editCon():
    nombre = str(input("Por favor, escriba el nombre del contacto a editar: "))
    numero = str(input("Por favor, escriba el nuevo número de teléfono: "))
    agenda.update({nombre: numero})
    print(f"{nombre}, ha sido editado con éxito, su nuevo número es {numero}.")
    print('\n')
    commandList()

def exit():
    print("¡Hasta la próxima!")

commandList()