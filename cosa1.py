print("bien!")

nombre = input("dime tu nombre")

if nombre.lower() == "nadia":
  print("te quiero.")
else:
  print("qué hacés tocando mi computadora!!")

print("fin")



print("hola mundosdfiods")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

total = 0 #luego sumaremos valores a esta variable para poder lograr el objetivo de sumar valroes que uno ingresa.
          #variable, lista. ahora falta otra variable que le indique a la maquina el rango en el que debe contar.

for i in range(5):#este rango es el que me indica las veces que debe realizar determinada cosa que irá después del ":".
    nuevonumero = int(input("introduce un number: ")) #aquí estoy diciendo que la nueva variable "nuevonumero" será igual a el valor entero (por el "int") que introducirá el ser que use este programita (por el "input"), luego de que la máquina le pida que lo haga. Es decir, que le ordenamos a la máquina que se encargue de pedirle, al posible humano, un valor para la nueva variable llamada "nuevonumero".
    total += nuevonumero #esto le pide a la máquina que a la variable total, que era igual a cero, se le sume la variable nuevonumero, esto sucederá 5 veces, tantas veces como numeros de le asigne a nuevonumero ya que se le pedirá al humano esa cantidad de veces.

#una vez que le bucle termine de hacer esa suma de variables, la imprimirá

print("El total es: ", total)
 #en este sensillo programita, tenemos 3 variables en juego. La variable i que me indica la cantidad de veces que se repetirá la acción asignada después del ":". La variable nuevonumero, será la que tendrá el valor que le introduzca el usuarui. y, por último, la variable total que irá cambiando según se vaya ejecutando el bucle; esta variable comenzará siendo igual a 0, luego cuando se ejecute por primera vez el bucle, según las indicaciones que le hemos dado, se le suma el valor que el usuario le da a la variable nuevonumero. Ej.: si nuevonumero = 2 entonces total = 0 + 2 = 2, y este será el primer numero  a sumar. el primero de los otros 4 numeros que se crearán luego de ingresar valores a la variable nuevonumero, según la  máquina nos lo vaya pidiendo. En la proxima ejecución (recordemos que la repetirá 5 veces, o sea, 5 numeros por sumar) tomará el valor que le quedó a la variable en la operación anterior. No es lindo el hecho de que lo haya entendido? total acumulado! 





