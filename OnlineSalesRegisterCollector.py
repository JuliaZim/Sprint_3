import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            "чипсы": 50,
            "кола": 100,
            "печенье": 45,
            "молоко": 55,
            "кефир": 70,
        }
        self.__tax_rate = {
            "чипсы": 20,
            "кола": 20,
            "печенье": 20,
            "молоко": 10,
            "кефир": 10,
        }

    # 1. Геттер и сеттер для item_price
    @property
    def item_price(self):
        return self.__item_price

    @item_price.setter
    def item_price(self, new_item_price):
        self.__item_price = new_item_price

    # 1.Геттер и сеттер для number_items
    @property
    def number_items(self):
        return self.__number_items

    @number_items.setter
    def number_items(self, new_number_items):
        self.__number_items = new_number_items

    # 2. Метод добавления товара в чек
    def add_item_to_cheque(self, name):
        if not 0 < len(name) <= 40:
            raise ValueError(
                "Нельзя добавить товар, если в его названии нет символов или их больше 40"
            )
        if name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        self.__name_items.append(name)
        new_number_items = self.number_items + 1
        self.number_items = new_number_items

    # 3. Удалить товар из чека
    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError("Позиция отсутствует в чеке")
            self.__name_items.remove(name)
            new_number_items = self.number_items - 1
            self.number_items = new_number_items
        except Exception as e:
            print(e)

    # 4. Посчитать общую стоимость товара
    def check_amount(self):
        total = []
        try:
            for el in self.__name_items:
                total.append(self.item_price.get(el))

            if len(total) > 10:
                return sum(total) * 0.9
            else:
                return sum(total)
        except Exception as e:
            print(e)

    # 5. Вычислить НДС товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        try:
            for name in self.__name_items:
                if self.__tax_rate[name] == 20:
                    twenty_percent_tax.append(name)
                    total.append(self.item_price.get(name))
            if len(self.__name_items) > 10:
                return sum(total) * 0.2 * 0.9
            else:
                return sum(total) * 0.2
        except Exception as e:
            print(e)

    # 6. Вычислить НДС товаров со ставкой 10%:
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        try:
            for name in self.__name_items:
                if self.__tax_rate[name] == 10:
                    ten_percent_tax.append(name)
                    total.append(self.item_price.get(name))
            if len(self.__name_items) > 10:
                return sum(total) * 0.1 * 0.9
            else:
                return sum(total) * 0.1
        except Exception as e:
            print(e)

    # 7. Общая сумма налогов
    def total_tax(self):
        return (
            self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        )

    # 8. Метод, который возвращает номер телефона
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if len(telephone_number) < 10:
                raise ValueError("Необходимо ввести цифры")
            if len(telephone_number) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            return f"+7{telephone_number}"
        except Exception as e:
            print(e)

    # 9. Преобразование даты
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ["часы", lambda x: x.hour],
            ["минуты", lambda x: x.minute],
            ["день", lambda x: x.day],
            ["месяц", lambda x: x.month],
            ["год", lambda x: x.year],
        ]
        for el in date:
            date_and_time.append(f"{el[0]}: {el[1](now)}")
        return date_and_time


check = OnlineSalesRegisterCollector()
check.add_item_to_cheque("чипсы")
check.add_item_to_cheque("молоко")
check.add_item_to_cheque("молоко")
check.delete_item_from_check("молоко")
print(check.number_items)
print(check.check_amount())
print(check.twenty_percent_tax_calculation())
print(check.ten_percent_tax_calculation())
print(check.total_tax())
print(OnlineSalesRegisterCollector.get_telephone_number("9999999999"))
print(OnlineSalesRegisterCollector.get_date_and_time())
