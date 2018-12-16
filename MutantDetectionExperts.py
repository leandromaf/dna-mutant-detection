# -*- coding: utf-8 -*-
import pdb


# Eperto en deteccion de mutantes analizando su DNA
class DNAMutantDetectionExpert:

	# funcion que debe decir si el arreglo de cadenas pasado en dna corresponde a un mutante
	def isMutant(self,dna,cantidadIguales = 4,secuenciasIgualesMinima = 2):
		#IN PROGRESS
		# para decidir debe verificar si hay  más de una secuencia de cantidadIguales letras iguales​, de forma oblicua, horizontal o vertical
		'''
		TODO
		idealmente deberiamos poder transformar el arreglo de cadenas a una matriz numpy para chequear de antemano ante
		un elemento puntual si efectivamente existen al menos en toda la matriz una cantidad igual a la considerada
		para ser mutante
		'''	
		# Variable para contar cuantas secuencias iguales llevamos encontradas
		contadorSecuenciasIguales = 0
		
		# asumimos que todas las cadenas del arreglo dna tienen la misma longitud en caracteres
		ncolumnas = len(dna[0])
		# arreglo para contar cuantos elementos iguales encontramos en cada columnaumna
		contadoresElmentosIgualescolumnaumnas = []
		for i in range(ncolumnas):
			# lo inicializamos con un 1 para cada columnaumna
			contadoresElmentosIgualescolumnaumnas.append(1)

		
		# matriz para llevar la cuenta de elementos iguales en las diagonales 
		# tiene una cantidad de filas igua la la (cantidad de columnas de la matriz * 2 ) - 1 (cantidad de diagonales posibles
		# y dos columnas, una para cada direccion posible de la diagonal
		# desde la izquieda o desde la derecha
		contadorElementosIgualesDiagonal = []
		for i in range((2*ncolumnas)-1):
			# lo inicializamos con una lista de dos 1 para cada direccion
			contadorElementosIgualesDiagonal.append([1,1])

		
		# iteramos por fila
		for fila in range(0, len(dna)):
			# para cada nueva fila el contador de elementos iguales por fila se reinicia a 1 
			elementosIgualesFila = 1
			# iteramos por columnaumnas (caracteres de la cadena ubicada en la posicion fila)
			for columna in range(0, len(dna[fila])):
				# obtenemos el elemento actual
				elementoActual = dna[fila][columna]

				# chequear con elementos en la misma fila
				if columna > 0:
					# solo si existe un elemento previo
					# buscamos el anterior en la misma fila , es decir en la columnaumna anterior
					elementoPrevio = dna[fila][columna - 1]
					if elementoActual == elementoPrevio:
						# si el elemento actual es igual al previo en la fila
						# sumamos uno al contador
						elementosIgualesFila += 1
						if elementosIgualesFila == cantidadIguales:
							# cuando llegamos a la cantidad considerada de elementos iguales sumamos uno al contador 
							# de secuencias en linea
							print("Encontramos "+str(elementosIgualesFila)+ " elementos iguales en una misma fila")
							# reinicio del contador de elemntos iguales por fila
							elementosIgualesFila = 1
							contadorSecuenciasIguales += 1
							if contadorSecuenciasIguales >= secuenciasIgualesMinima:
								# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
								# para cortar cuanto antes
								return True
								

					else:
						# si no es igual reiniciamos directamente
						elementosIgualesFila = 1

				# verificar  con elementos en la misma columnaumna
				if fila > 0:		
					# solo si existe una columnaumna previa
					# obtenemos ese elmento de la fila anterior para esta columnaumna
					elementoPrevio = dna[fila - 1][columna]
					if elementoActual == elementoPrevio:
						# si el actual es igual al previo
						# sumamos uno al contador de elementos iguales para esta columnaumna
						contadoresElmentosIgualescolumnaumnas[columna] += 1
						if contadoresElmentosIgualescolumnaumnas[columna] == cantidadIguales:
							# cuando llegamos a la cantidad de elementos iguales en esta columnaumna, sumamos uno a la cantidad 
							# de secuencias iguales
							print("Encontramos "+str(contadoresElmentosIgualescolumnaumnas[columna])+ " elementos iguales en una misma columna")
							# reinicio del contador de elementos iguales por columna
							contadoresElmentosIgualescolumnaumnas[columna] = 1
							contadorSecuenciasIguales += 1
							if contadorSecuenciasIguales >= secuenciasIgualesMinima:
								# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
								# para cortar cuanto antes
								return True
							
					else:
						# si no es igual vamos a reiniciar el contador de elemntos iguales por columnaumna
						contadoresElmentosIgualescolumnaumnas[columna] = 1

				# analisis de las diagonales
				for direccionDiagonal in range(2):
					# variable para indicar si se puede o no analizar este caso
					analizando = False
					# si estamos trabajando en la direccion diagonal desde arriba a la izquierda
					if direccionDiagonal == 0:
						# indicamos el indice a buscar en la matriz contadora de elemntos iguales que para este caso se 
						# calcula como:
						indiceMatriz = columna - fila + ncolumnas - 1 
						if fila > 0 and columna > 0 :
							# y ademas es posible extraer ese elemento (validacion)	
							# analizando el elemento anterior arriba a la izquierda
							elementoPrevio = dna[fila - 1][columna - 1]
							analizando = True
					elif direccionDiagonal == 1:
						# indicamos el indice a buscar en la matriz contadora de elemntos iguales que para este caso se 
						# calcula como:
						indiceMatriz = columna + fila
						if fila > 0 and columna + 1 < ncolumnas :
							# hacer los mismo para diagonal analizando el elemento anterior arriba a la derecha
							elementoPrevio = dna[fila - 1][columna + 1]
							analizando = True

					if analizando and elementoActual == elementoPrevio:
						# si el actual es igual al previo

						contadorElementosIgualesDiagonal[indiceMatriz][direccionDiagonal] +=1

						if contadorElementosIgualesDiagonal[indiceMatriz][direccionDiagonal] == cantidadIguales:
							print("Encontramos "+str(contadorElementosIgualesDiagonal[indiceMatriz][direccionDiagonal])+ " elementos iguales en la diagonal")
							# reinicio del contador de elementos iguales de la diagonal principal
							contadorElementosIgualesDiagonal[indiceMatriz][direccionDiagonal] = 1
							contadorSecuenciasIguales += 1
							if contadorSecuenciasIguales >= secuenciasIgualesMinima:
								# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
								# para cortar cuanto antes
								return True

					else:
						contadorElementosIgualesDiagonal[indiceMatriz][direccionDiagonal] = 1
						

		# si no se ha salido antes por True, sale False por defecto
		return False