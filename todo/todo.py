import json

todo_list = {}
tdf = 'todo/todo_list.json'

def save_values(todo_list, tdf):
    with open(tdf, 'w') as f:
        json.dump(todo_list, f)

def load_values(tdf):
    with open(tdf, 'r') as f:
        todo_list = json.load(f)
    return todo_list

def menu():
    print('[1] Ver tarea')
    print('[2] Añadir nueva tarea')
    print('[3] Marcar tarea como hecha')
    print('[4] Eliminar tarea/s')
    print('[0] Salir')

    option = int(input("¿Qué desea hacer?: "))

    if option == 1:
        see_tdl()
    elif option == 2:
        add_task()
    elif option == 3:
        check_task()
    elif option == 4:
        clear_task()
    elif option == 0:
        exit()
    else:
        print('La opción elegida no existe, inténtelo de nuevo.')
        menu()

def back_to_menu():
    save_values(todo_list, tdf)
    if input("\n¿Quieres hacer algo más? (s/n): ") == 's':
        menu()
    else:
        exit()

def see_tdl():
    print('Lista de tareas: ')
    for name, value in todo_list.items():
        print(f"{name}: {"☑" if value else "☒"}")

    back_to_menu()

def add_task():
    name = input("Introduzca el nombre de la tarea: ")
    todo_list.update({name: False})
    back_to_menu()
    
def check_task():
    i = 0
    print("\nTareas: ")
    for name in todo_list.keys():
        print(f'[{i}] {name}')
        i += 1
    key = int(input("¿Qué tarea desea completar?: "))
    todo_list.update({list(todo_list.keys())[key]: True})
    back_to_menu()
    
def clear_task():
    action = int(input('¿Qué desea hacer?: ' \
    '[1] Eliminar una tarea ' \
    '[2] Eliminar la lista de tareas ' \
    '[0] He cambiado de idea... (volver al menú principal) -> '))

    if action == 1:
        i = 0
        print("\nTareas: ")
        for name in todo_list.keys():
            print(f'[{i}] {name}')
            i += 1
        key = int(input("¿Qué tarea desea eliminar?: "))
        todo_list.pop(list(todo_list.keys())[key])
        back_to_menu()
    elif action == 2:
        todo_list.clear()
        print("Lista de tareas eliminada con éxito.")
        back_to_menu()
    elif action == 0:
        menu()
    else:
        print("Esa opción no existe, inténtelo de nuevo.")
        clear_task()

def exit():
    print("¡Hasta la próxima!")

if __name__ == '__main__':
    todo_list = load_values(tdf)
    menu()