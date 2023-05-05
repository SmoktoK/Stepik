# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x
# выводит значение функции f(x)=x**2+2*x+1, каждое на отдельной строке.

n = int(input())
my_list = []
for _ in range(n):
    my_list.append(int(input()))
print(*my_list, sep='\n')
print()
for i in range(n):
    print(my_list[i]**2 + 2 * my_list[i] + 1)