class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as f:
            products_list = f.read()
        return products_list

    '''
    Первый вариант
    '''
    def add(self, *products):
        for product in products:
            products_list = self.get_products()
            if product.name in products_list:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as new_products:
                    new_products.write(f'{product}\n')

    '''
    Второй вариант
    '''
    # def add(self, *products):
    #     old_products_list = self.get_products()
    #     new_products_list = ''
    #     for product in products:
    #         if product.name in old_products_list + new_products_list:
    #             print(f'Продукт {product.name} уже есть в магазине')
    #         else:
    #             new_products = open(self.__file_name, 'a')
    #             new_products.write(f'{product}\n')
    #             new_products.close()
    #             new_products_list += f'{product}\n'


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())


'''
Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries

Продукт Potato уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries

Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato уже есть в магазине
Продукт Spaghetti уже есть в магазине
Продукт Potato уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
'''