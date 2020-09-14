name = 'ibrahim'
surname = 'Beylem'
age = 36

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'
length = len(greeting) # greeying değikeninin harf sayısını bulur
""""
print(greeting)
print(greeting[0])
print(greeting[3])
print(greeting[length-1])
print(greeting[-1])    # sonuncu karakteri çeker
print(greeting[3:7])   #3. indexten başla 7. indexe kdar 7 dahil değil
print(greeting[3:])    #3. indexten sonrası
print(greeting[:16])   # baştan 16. karaktere kadar git 16 dahil değil"""

print(greeting[2:40:3])  #2. den başla 40 kadar 3er 3eralS