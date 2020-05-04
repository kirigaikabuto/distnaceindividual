
# if a%2==0:
#     print("четное")
# else:
#     print("не четное")
tovar1 = 50
tovar2 = 90
balance = 200
c = tovar1+tovar2
#>100 net deneg
#else oplachena
if c>balance:
    print("oplachen")
else:
    print("net deneg")
    diff = balance-c
    if diff<=50:
        print("не хватает чучуть")