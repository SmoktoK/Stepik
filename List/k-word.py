# На вход программе подается натуральное число n и n строк,
# а затем число k. Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
my_list = []

x = ''
for _ in range(n):
    my_list.append(input())
k = int(input())
for i in range(n):
    if (len(my_list[i])) >= k:
        new_list = []
        new_list.extend(my_list[i])
        x += new_list[k-1]
print(x)