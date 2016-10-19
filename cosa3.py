#para sumar todos los valores, del 1 al 100.

sum = 0 #en este caso, la varible comienza a tener un valor que será temporal, debido a que en la ejecución del bucle irá cambiando su valor.

#bucle:

for i in range (1, 101): #en esta parte, la variable i tomará valores que empezarán desde el 1 hasta el 100. 
    sum = sum + i #acá estoy diciendo que cuando el valor de i toma un numero sea sumado a el valor actual de sum, que es cero, y el valor obtenido sea el nuevo valor de la variable sum.
print(sum) #luego de haberse ejecutado todo el bucle, o sea, luego de que la variable sum haya tomado todos los valores que se formaron al tomar valores del 1 al 100 inclusive, se le ordena a la máquina que imprima el valor final que ha adquirido la variable sum.

#me gustaría saber cuales los valores que tiene asignada la variable sum durante la ejecución del bucle. Para ello, modificaremos un poco el código. 

print("ahora, imprimiré los valores que tiene la variable durante la ejecución del bucle. O sea, que quiero que me imprima el valor que tiene sum en todas las veces que esta sentencia se repite.")

for i in range (1, 101):
    sum = sum + i
    print(sum) #con esta nueva linea le digo a la máquina que me imprima el valor de sum en cada una de las repeticiones que este realiza.
print(sum) # y por ultimo, que me imprima el valor final que tiene la variable sum.

#lo he ejecutado y me di cuenta de que para empezar a realizar el bucle, toma el ultimo valor que tiene sum en la ultima vez que fué utilizado en la sentencia anterior. Es decir, en la asentencia anterior, sum ha tenido el valor de 5050 y a partir de él, el valor 5050 fué sumado a los valores que he dicho que tome i. Ver que i empieza a tomar el valor 1, entonces el proximo valor de sum será de 5051, luego i toma el valor de 2, entonces sum será igual a 5053, etc., y así sucesivamente.


#si quiero que empiece, de nuevo con sum igual a cero, 

print("de nuevo, pero con sum igual a cero y la variable i en un rango desde el 1 hasta el 51 (50 veces, incluyendo al 1 y excluyendo al 51)")

sum = 0
 
for i in range(1, 51):
    sum += i
    print(sum)
print(sum)

#veamos si funciona. Sí! funciona.

print("ahora, con i que tenga un rango entre el 1 y el 101 (100 veces) y sum igual a cero")

sum = 0

for i in range (1, 101):
    sum += i
    print(sum)
print("el valor final de sum, es ", sum)

#veamos.



