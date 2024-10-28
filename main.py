from database_manager import DatabaseManager


def print_menu():
    print("Dame la opción que quieres \n0) Salir \n1) Insertar producto \n2) Mostrar productos\n")
    return int(input())


opcion = print_menu()
db_manager = DatabaseManager('localhost', 'ecommerce_532', 'root', 'andrestorres')
while opcion != 0:
    if opcion == 1:
        name = input("Dame el nombre: ")
        description = input("Dame la descripción: ")
        price = input("Dame el precio $")
        weight = input("Dame el peso: ")
        db_manager.insert_producto(name, description, price, weight)
    if opcion == 2:
        db_manager.list_products()
    opcion = print_menu()



