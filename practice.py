users = [
    {'username': 'admin', 'password': 'admin', 'role': 'admin'},
    {'username': 'user', 'password': 'user', 'role': 'user', 'history': []}
]

products = [
    {'id': 1, 'name': 'Milk', 'price': 50, 'quantity': 10},
    {'id': 2, 'name': 'Bread', 'price': 30, 'quantity': 20},
    {'id': 3, 'name': 'Eggs', 'price': 70, 'quantity': 5}
]

def authenticate():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Добро пожаловать, {username}!")
            return user
    print("Неверные логин или пароль!")
    return None

def view_products():
    print("\nДоступные товары:")
    for product in products:
        print(f"ID: {product['id']}, Название: {product['name']}, Цена: {product['price']}, Кол-во: {product['quantity']}")

def filter_sort_products():
    global products
    print("\n1. Сортировать по цене")
    print("2. Сортировать по количеству")
    print("3. Фильтровать по минимальной цене")
    choice = input("Выберите действие: ")

    if choice == '1':
        sorted_products = sorted(products, key=lambda x: x['price'])
        for product in sorted_products:
            print(f"{product['name']} - {product['price']} руб.")
    elif choice == '2':
        sorted_products = sorted(products, key=lambda x: x['quantity'])
        for product in sorted_products:
            print(f"{product['name']} - {product['quantity']} шт.")
    elif choice == '3':
        min_price = int(input("Введите минимальную цену: "))
        filtered_products = list(filter(lambda x: x['price'] >= min_price, products))
        for product in filtered_products:
            print(f"{product['name']} - {product['price']} руб.")
    else:
        print("Неверный выбор!")

def manage_products():
    global products
    print("\n1. Добавить товар")
    print("2. Удалить товар")
    print("3. Редактировать товар")
    choice = input("Выберите действие: ")

    if choice == '1':
        name = input("Название товара: ")
        price = int(input("Цена товара: "))
        quantity = int(input("Количество товара: "))
        products.append({'id': len(products) + 1, 'name': name, 'price': price, 'quantity': quantity})
        print(f"Товар {name} добавлен.")
    elif choice == '2':
        view_products()
        product_id = int(input("Введите ID товара для удаления: "))
        products = [p for p in products if p['id'] != product_id]
        print("Товар удален.")
    elif choice == '3':
        view_products()
        product_id = int(input("Введите ID товара для редактирования: "))
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            product['name'] = input("Новое название: ")
            product['price'] = int(input("Новая цена: "))
            product['quantity'] = int(input("Новое количество: "))
            print("Товар обновлен.")
        else:
            print("Товар не найден.")
    else:
        print("Неверный выбор!")

def purchase_products(user):
    global products
    cart = []
    while True:
        view_products()
        product_id = int(input("Введите ID товара для добавления в корзину (0 для выхода): "))
        if product_id == 0:
            break
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            quantity = int(input(f"Введите количество для {product['name']}: "))
            if quantity <= product['quantity']:
                cart.append({'name': product['name'], 'price': product['price'], 'quantity': quantity})
                product['quantity'] -= quantity
                print(f"{quantity} шт. {product['name']} добавлено в корзину.")
            else:
                print("Недостаточно товара на складе!")
        else:
            print("Товар не найден.")
    # Покупка
    total_cost = sum(item['price'] * item['quantity'] for item in cart)
    print(f"Общая стоимость: {total_cost} руб.")
    confirm = input("Подтвердить покупку? (да/нет): ")
    if confirm.lower() == 'да':
        user['history'].extend(cart)
        print("Покупка успешно завершена!")
    else:
        print("Покупка отменена.")

def main():
    user = authenticate()
    if not user:
        return

    while True:
        if user['role'] == 'user':
            print("\n1. Просмотреть товары")
            print("2. Купить товары")
            print("3. История покупок")
            print("4. Сортировка и фильтрация")
            print("5. Выйти")
            choice = input("Выберите действие: ")

            if choice == '1':
                view_products()
            elif choice == '2':
                purchase_products(user)
            elif choice == '3':
                print("\nИстория покупок:")
                for item in user['history']:
                    print(f"{item['name']} - {item['quantity']} шт. - {item['price']} руб.")
            elif choice == '4':
                filter_sort_products()
            elif choice == '5':
                break
            else:
                print("Неверный выбор!")
        elif user['role'] == 'admin':
            print("\n1. Управление товарами")
            print("2. Выйти")
            choice = input("Выберите действие: ")

            if choice == '1':
                manage_products()
            elif choice == '2':
                break
            else:
                print("Неверный выбор!")

if __name__ == "__main__":
    main()
