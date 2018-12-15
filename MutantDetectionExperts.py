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

		# arreglo para llevar la cuenta de elementos iguales por diagonal principal, cunado fila == columna
		# tiene  dos elementos, uno para cada direccion
		# desde la izquieda o hacia la derecha
		contadorElementosIgualesDiagonalPrincipal = [1,1]
		
		# matriz para llevar la cuenta de elementos iguales arriba de la  diagonal principal, cuando la columna > fila
		# tiene una cantidad de filas igua la la cantidad de columnas de la matriz y dos columnas, una para cada direccion
		# desde la izquieda o hacia la derecha
		contadorElementosIgualesDiagonalSuperior = []
		for i in range(ncolumnas-1):
			# lo inicializamos con una lista de dos 1 para cada direccion
			contadorElementosIgualesDiagonalSuperior.append([1,1])

		# matriz para llevar la cuenta de elementos iguales abajo de la  diagonal principal, cuando la  fila > columna
		# tiene una cantidad de filas igua la la cantidad de columnas de la matriz y dos columnas, una para cada direccion
		# desde la izquieda o hacia la derecha
		contadorElementosIgualesDiagonalInferior = []
		for i in range(ncolumnas-1):
			# lo inicializamos con una lista de dos 1 para cada direccion
			contadorElementosIgualesDiagonalInferior.append([1,1])

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
					# y ademas es posible extraer ese elemento (validacion)
					if direccionDiagonal == 0 and fila > 0 and columna > 0 :
						# analizando el elemento anterior arriba a la izquierda
						elementoPrevio = dna[fila - 1][columna - 1]
						analizando = True
					elif direccionDiagonal == 1 and fila > 0 and columna + 1 < ncolumnas :
						# hacer los mismo para diagonal analizando el elemento anterior arriba a la derecha
						elementoPrevio = dna[fila - 1][columna + 1]
						analizando = True

					if analizando and elementoActual == elementoPrevio:
						# si el actual es igual al previo

						if elementoActual == elementoPrevio == 'T':
							pdb.set_trace()
						
						if fila == columna :
							# estamos analizando diagonal principal
							contadorElementosIgualesDiagonalPrincipal[direccionDiagonal] += 1
							if contadorElementosIgualesDiagonalPrincipal[direccionDiagonal] == cantidadIguales:
								# cuando llegamos a la cantidad de elementos iguales  sumamos uno a la cantidad 
								# de secuencias iguales
								print("Encontramos "+str(contadorElementosIgualesDiagonalPrincipal[direccionDiagonal])+ " elementos iguales en la diagonal principal")
								# reinicio del contador de elementos iguales de la diagonal principal
								contadorElementosIgualesDiagonalPrincipal[direccionDiagonal] = 1
								contadorSecuenciasIguales += 1
								if contadorSecuenciasIguales >= secuenciasIgualesMinima:
									# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
									# para cortar cuanto antes
									return True
						elif columna > fila :
							# estamos analizando diagonal superior
							# TODO BUG: aqui no estamos indexando bien, no es una forma univoca la digaonal con esa cuenta
							contadorElementosIgualesDiagonalSuperior[columna-fila-1][direccionDiagonal] += 1
							if contadorElementosIgualesDiagonalSuperior[columna-fila-1][direccionDiagonal] == cantidadIguales:
								# cuando llegamos a la cantidad de elementos iguales  sumamos uno a la cantidad 
								# de secuencias iguales
								print("Encontramos "+str(contadorElementosIgualesDiagonalSuperior[columna-fila-1][direccionDiagonal])+ " elementos iguales en una diagonal superior")
								# reinicio del contador de elementos iguales de la diagonal superior columna - fila
								contadorElementosIgualesDiagonalSuperior[columna-fila-1][direccionDiagonal]= 1
								contadorSecuenciasIguales += 1
								if contadorSecuenciasIguales >= secuenciasIgualesMinima:
									# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
									# para cortar cuanto antes
									return True
						elif fila > columna :
							# estamos analizando diagonal inferior
							contadorElementosIgualesDiagonalInferior[fila-columna-1][direccionDiagonal] += 1
							if contadorElementosIgualesDiagonalInferior[fila-columna-1][direccionDiagonal] == cantidadIguales:
								# cuando llegamos a la cantidad de elementos iguales  sumamos uno a la cantidad 
								# de secuencias iguales
								print("Encontramos "+str(contadorElementosIgualesDiagonalInferior[fila-columna-1][direccionDiagonal])+ " elementos iguales en una diagonal inferior")
								# reinicio del contador de elementos iguales de la diagonal superior columna - fila
								contadorElementosIgualesDiagonalInferior[fila-columna-1][direccionDiagonal]= 1
								contadorSecuenciasIguales += 1
								if contadorSecuenciasIguales >= secuenciasIgualesMinima:
									# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
									# para cortar cuanto antes
									return True
					else:
						if fila == columna :
							# estamos analizando diagonal principal
							contadorElementosIgualesDiagonalPrincipal[direccionDiagonal] = 1
						elif columna > fila :
							# estamos analizando diagonal superior
							contadorElementosIgualesDiagonalSuperior[columna-fila-1][direccionDiagonal] = 1
						elif fila > columna :
							# estamos analizando diagonal inferior
							contadorElementosIgualesDiagonalInferior[fila-columna-1][direccionDiagonal] = 1
				

		# si no se ha salido antes por True, sale False por defecto
		return False