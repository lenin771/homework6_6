# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N

num = int(input('Введите число '))
print ((lambda b: (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1,b))(num))