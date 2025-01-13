class Product:
    def __init__(self, name, weight, category):
        self.name = name #название продукта (строка)
        self.weight = weight #общий вес товара (дробное число)
        self.category = category #категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')#считывает информацию из файла __file_name
        products = file.read()  # получение содержимого файла
        file.close()  # закрытие файла
        return products # возвращение единой строки со всеми товарами из файла __file_name.

    def add(self, *products): #принимает неограниченное количество объектов класса Product
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in current_products:
                file.write(str(product) + '\n')
                current_products += str(product) + '\n'
            else:
                print(f'Продукт {product} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())