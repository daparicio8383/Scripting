num_user = input("\r\nEscribe tu número decimal:\r\n")
b = []
c = []
hex_list_itC = []
hex_list_itB = []
numeros_dec = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numeros_hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

try: # Se usa para el manejo de errores. try/except.

    if int(num_user) >= 16:  #Comportamiento para aquellos números decimales mayores o iguales a 16.

        def division(n): # Función para dividir un número dado entre 16, sin decimales ni resto.
            if n >= 16:
                a = int(n / 16)
                b.append(a) # Añade a la lista 'b' el resultado de n / 16
                division(a) # Ejecuta la función division de forma recursiva, hasta que n < 16

        def iteracionB(): # Función para iterar sobre los valores de n / 16
            i = b[-1] # i es igual al último valor de la lista 'b'.
            a = numeros_dec.index(i) # se iguala el valor obtenido de i con su equivalente en la lista 'numeros_dec', obteniendo su posición (índice) en ella.
            hex = numeros_hex[a] # Se iguala el valor del índice en la lista de dígitos hexadecimales.
            hex_list_itB.append(hex)
            return hex_list_itB[0]

        def iteracionC(): # Función para iterar sobre los valores de n % 16
            for i in c: # Para todo elemento en la lista 'c'.
                a = numeros_dec.index(i)
                hex = numeros_hex[a]
                hex_list_itC.append(hex)
                hex_num = "".join(hex_list_itC[::-1]) # Une lo números de la lista, empezando por el final.
            return hex_num

        def total():
            res1 = str(iteracionB())
            res2 = str(iteracionC())
            print("\r\n\r\nEl número en hexadecimal es: " + res1 + res2 + "\r\n\r\n")
                
        b.append(int(num_user)) # Añade el input a la lista 'b'.
        division(int(num_user))

        for i in b: # Para cada número en 'b'. Si es mayor o igual a 16, añadir a 'c' el resto de dividir el número entre 16.
            if i >= 16:
                c.append(i % 16)

        total()

    elif int(num_user) < 16: # Supuesto para aquellos números menores a 16. Se comparará el número decimal con su equivalente en la tabla hexadecimal.
        i = b.append(int(num_user))
        a = numeros_dec.index(b[0])
        hex = numeros_hex[a]
        hex_list_itB.append(hex)
        print("\r\n\r\nEl número en hexadecimal es: " + hex_list_itB[0] + "\r\n\r\n")

    elif int(num_user) == 0:
        print("\r\n\r\nEl número en hexadecimal es: 0\r\n\r\n")

except ValueError as ve: # Tratamiento del tipo ValueError, para inputs que no sean números naturales.
    print("\r\n\r\nSe ha producido un error. Introduce un número natural (0, 1, 2, etc)\r\n\r\n")
