# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.

num = int(input("Введите целое число n: "))
my_list = []


for i in range(1,num+1):
    my_list.append((1+1/i)**(i))
    
    

print(*my_list,sep= ', ')  


print(sum(my_list))

 



# for i in range ()
#  sum = 0
#  while (i < len.my_list): 
#     sum = sum + (i)
# print(sum)    
 
