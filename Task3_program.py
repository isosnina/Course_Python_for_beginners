from Task3_module_compare import compare

cities = ['Москва','Пермь', 'Пенза', 'Тверь']
y = 'Пермь'

if __name__ == '__main__':
    for x in cities:
        print(x, y, compare(x, y))
