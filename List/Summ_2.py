# На вход программе подается натуральное число n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел(0 и 1, 1 и 2, и т.д.)

n = int(input())
my_list = []
new_list = []
for i in range(n):
    x = int(input())
    my_list.append(x)
for i in range(n-1):
    new_list.append(my_list[i] + my_list[i+1])
print(new_list)