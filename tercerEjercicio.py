'''
Funcion: generarString, la funcion esta hecha para hacer devuelva una cadena que contenga exactamente A letras ' a ' y exactamente B letras ' b ' 
                        sin tres letras consecutivas iguales (en otras palabras, ni " aaa " ni " bbb " puede aparecer en la cadena devuelta).

Parametros: A,B

Retorna:rt
'''
def generarString(A, B):
	rt = ""
	while (0 < A or 0 < B) :

		# More 'b', append "bba"
		if (A < B) :
			if (0 < B):
				rt = rt +'b'
				B -= 1
			if (0 < B):
				rt += 'b'
				B -= 1
			if (0 < A):
				rt += 'a'
				A -= 1

		# More 'a', append "aab"
		elif (B < A):
			if (0 < A):
				rt += 'a'
				A -= 1
			if (0 < A):
				rt += 'a'
				A -= 1
			if (0 < B):
				rt += 'b'
				B -= 1

		# Equal number of 'a' and 'b'
		# append "ab"
		else :
			if (0 < A):
				rt += 'a'
				A -= 1
			if (0 < B):
				rt += 'b'
				B -= 1
	print(rt)

# Driver code
if __name__ == "__main__":
	#ingresamos los valores de la letra A
	A = int(input("Ingrese el número de letras 'a': "))
	#ingresamos los valores de la letra B
	B = int(input("Ingrese el número de letras 'b': "))
	#llamamos a la funcion para generar la cadena de letras segun lo que ingrese el usuario
	generarString(A, B)
