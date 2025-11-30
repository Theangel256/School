Total = 0
print("           CHOOSE A DRINK")
print ("1.Capuccino $3.00   2.Espresso $2.50")
print ("3.Macchiato $2.50   4.Americano $3.00")
print ("5.Mocha $3.50       6.Latte $2.50")
print ("7.Flat White $2.50")

opcion = int(input ("         ENTER THE NUMBER: "))

while opcion < 1 or opcion >7 :
   print("ERROR: Select something from the menu")
   opcion = int(input("choose a coffee:")) 

if opcion == 1:
    Total += 3.00

if opcion == 2:
    Total += 2.50
    
if opcion == 3:
    Total += 2.50

if opcion == 4:
    Total += 3.00

if opcion == 5:
    Total += 3.50

if opcion == 6:
    Total += 2.50

if opcion == 7:
    Total += 2.50


print("PICK A SIZE")
print("1. Medium $0.00")
print("2. Large +$1.00")
print("3. XL +$1.50")

opcion2 = int(input ("         ENTER THE NUMBER: "))

while opcion2 < 1 or opcion2 >3 :
   print("ERROR: Select something from the menu")
   opcion2 = int(input("choose a size:")) 
     
if opcion2 == 1:
    Total += 0.00

if opcion2 == 2:
    Total += 1.00

if opcion2 == 3:
    Total += 1.50


print("Eat in or take away? ")
print("1. Eat-in $0.00")
print("2. take away +$1.00")

opcion3 = int(input ("         ENTER THE NUMBER: "))

while opcion3 < 1 or opcion3 >2 :
   print(f"ERROR: Select something from the menu")
   opcion3 = int(input("choose the place where you will consume:"))

if opcion3 == 1:
    Total += 0.00
if opcion3 == 2:
    Total += 1.00
else:
 print("invalid option")

print(f"Total to pay: ${Total}")
print ("Have a nice day :)")

#¿Cuál versión crees que es más eficiente y por qué?
#siento que la version con for es mas eficiente porque reduce las lineas de codigo y lo optimiza
#¿Cuál o cuáles son las ventajas/desventajas de cada versión?
#con for, haces menos lineas de codigo y lo optimiza mas pero es un poco mas dificil de utilizar 
#el con puro if es mas sencillo pero ocupas mas lineas de codigo 