values = []
dictionary = {}


c = int(input("Введите значение C: "))
i = int(input("Введите значение I: "))
g = int(input("Введите значение G: "))
ex = int(input("Введите значение Ex: "))
im = int(input("Введите значение Im: "))


values.extend([c, i, g, ex, im])
dictionary['c'] = c
dictionary['i'] = i
dictionary['g'] = g
dictionary['ex'] = ex
dictionary['im'] = im

print("Список значений:", values)
print("Словарь значений:", dictionary)

print('-'*30)

def calculate_GDP(C, I, G, Ex, Im):
    Y = C + I + G + Ex - Im
    return Y

C = int(input("Введите значение C: "))
I = int(input("Введите значение I: "))
G = int(input("Введите значение G: "))
Ex = int(input("Введите значение Ex: "))
Im = int(input("Введите значение Im: "))

GDP = calculate_GDP(C, I, G, Ex, Im)
print("Валовой внутренний продукт (ВВП):", GDP)

print('-'*30)

def calculate_GDP(C, I, G, Ex, Im):
    Y = C + I + G + Ex - Im
    return Y

values = [3, 1, 5, 2, 4]
dictionary = {'C': 3, 'I': 1, 'G': 5, 'Ex': 2, 'Im': 4}

GDP = calculate_GDP(*values)
print("Валовой внутренний продукт (ВВП):", GDP)

GDP = calculate_GDP(**dictionary)
print("Валовой внутренний продукт (ВВП):", GDP)
