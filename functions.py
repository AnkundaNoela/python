def greet_student():
    print('Good morning welcome to python class')

greet_student()  # Call the function outside its body

def find_product(a, b):
    return a * b

# Example usage
result = find_product(5, 3)
print("Product:", result)


def get_stats(a,b):
    return a+b, a-b

sum_value, subtract_value = get_stats(20,12)
print(sum_value)
print(subtract_value)

def division(x,y):
    return x/y
print(division(3,4))

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)
