#Diseñar un programa que muestre el producto de los 10 primeros números impares.

#[1,3,5,7,9,11,13,15,17,19]
mult = 1
for i in range(1,20,2):
    mult = mult * i
    print(mult)