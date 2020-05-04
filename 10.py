arr=[100,5,20,3,500]
n = len(arr)

#[0..4]
#вывод элементов массива
for i in range(n):
    print(arr[i])
#сумма всех элементов в массиве
sumi=0
for i in range(n):
    sumi = sumi +arr[i]

print(sumi)
#среднее арифметичское
1,2,3,4,6,10