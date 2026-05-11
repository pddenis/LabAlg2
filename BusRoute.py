import base64


# =========================
# Узел списка
# =========================
class Node:
    def __init__(self, name, x, y, time_to_next):
        self.name = name
        self.x = x
        self.y = y
        self.time_to_next = time_to_next
        self.next = None


# =========================
# Класс маршрута
# =========================
class BusRoute:

    def __init__(self):
        self.head = None

    # --------------------------------
    # Добавление остановки
    # --------------------------------
    def add_stop(self, name, x, y, time_to_next):

        new_node = Node(name, x, y, time_to_next)

        # если маршрут пуст
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        # поиск последнего узла
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

        print("Остановка добавлена.")

    # --------------------------------
    # Красивый вывод маршрута
    # --------------------------------
    def print_route(self):

        if self.head is None:
            print("Маршрут пуст.")
            return

        temp = self.head

        print("\nМаршрут:\n")
        print("--> ",end="")
        while True:
            print(f"temp.name --({temp.time_to_next} мин)--> " ,end="")

            temp = temp.next

            if temp == self.head:
                break


    # --------------------------------
    # Общее время маршрута
    # --------------------------------
    def total_time(self):

        if self.head is None:
            print("Маршрут пуст.")
            return

        total = 0

        temp = self.head

        while True:

            total += temp.time_to_next

            temp = temp.next

            if temp == self.head:
                break

        print("Общее время маршрута:", total, "мин")

    # --------------------------------
    # Получить список остановок
    # --------------------------------
    def get_stops(self):

        stops = []

        if self.head is None:
            return stops

        temp = self.head

        while True:

            stops.append(temp)

            temp = temp.next

            if temp == self.head:
                break

        return stops

    # --------------------------------
    # Где автобус через N остановок
    # --------------------------------
    def stop_after_n(self):

        if self.head is None:
            print("Маршрут пуст.")
            return

        stops = self.get_stops()

        print("\nСписок остановок:\n")

        for i in range(len(stops)):
            print(f"{i + 1}. {stops[i].name}")

        start_index = int(
            input("\nНа какой остановке сейчас автобус: ")
        ) - 1

        # проверка границ
        if start_index < 0 or start_index >= len(stops):
            print("Неверный номер остановки.")
            return

        n = int(input("Через сколько остановок: "))

        current = stops[start_index]

        for _ in range(n):
            current = current.next

        print(
            f"\nЧерез {n} остановок автобус будет на: "
            f"{current.name}"
        )

    # --------------------------------
    # Разворот маршрута
    # --------------------------------
    def reverse_route(self):

        if self.head is None:
            print("Маршрут пуст.")
            return

        prev = None
        current = self.head
        first = self.head

        while True:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

            if current == self.head:
                break

        first.next = prev
        self.head = prev

        print("\nМаршрут перевернут.")

        # сразу выводим маршрут
        self.print_route()

    # --------------------------------
    # Сохранение в файл Base64
    # --------------------------------
    def save_to_file(self, filename):

        if self.head is None:
            print("Маршрут пуст.")
            return

        with open(filename, "w", encoding="utf-8") as file:

            temp = self.head

            while True:

                line = (
                    f"{temp.name};"
                    f"{temp.x};"
                    f"{temp.y};"
                    f"{temp.time_to_next}"
                )

                encoded = base64.b64encode(
                    line.encode("utf-8")
                ).decode("utf-8")

                file.write(encoded + "\n")

                temp = temp.next

                if temp == self.head:
                    break

        print("Маршрут сохранен в файл.")


# =========================
# Главное меню
# =========================
route = BusRoute()

while True:

    print("\n========== MENU ==========")
    print("1. Добавить остановку")
    print("2. Показать маршрут")
    print("3. Общее время маршрута")
    print("4. Где будет автобус через N остановок")
    print("5. Развернуть маршрут")
    print("6. Сохранить маршрут в файл")
    print("0. Выход")

    choice = input("\nВыберите команду: ")

    # --------------------------------
    # Добавление остановки
    # --------------------------------
    if choice == "1":

        name = input("Название остановки: ")

        x = float(input("Координата X: "))

        y = float(input("Координата Y: "))

        time_to_next = int(
            input("Время до следующей остановки: ")
        )

        route.add_stop(
            name,
            x,
            y,
            time_to_next
        )

    # --------------------------------
    # Показать маршрут
    # --------------------------------
    elif choice == "2":

        route.print_route()

    # --------------------------------
    # Общее время
    # --------------------------------
    elif choice == "3":

        route.total_time()

    # --------------------------------
    # Через N остановок
    # --------------------------------
    elif choice == "4":

        route.stop_after_n()

    # --------------------------------
    # Разворот маршрута
    # --------------------------------
    elif choice == "5":

        route.reverse_route()

    # --------------------------------
    # Сохранение в файл
    # --------------------------------
    elif choice == "6":

        filename = input("Введите имя файла: ").strip()

        route.save_to_file(filename)

    # --------------------------------
    # Выход
    # --------------------------------
    elif choice == "0":

        print("Выход из программы.")
        break

    else:
        print("Неверная команда.")