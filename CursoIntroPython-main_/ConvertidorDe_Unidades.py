from datetime import date

parsec = input("Ingresa la cantidad de Parsec: ")
lightyears = 3.26156 * int(parsec)               # 1 parsec es 3.26156 años luz. 


print("In "+ str(parsec) + " parsec, is " + str(lightyears) + " lightyears")
print("Today's date is: " + str(date.today()))