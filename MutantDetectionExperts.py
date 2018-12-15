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
		nCols = len(dna[0])
		# arreglo para contar cuantos elementos iguales encontramos en cada columna
		contadoresElmentosIgualesColumnas = []
		for i in range(nCols):
			# lo inicializamos con un 1 para cada columna
			contadoresElmentosIgualesColumnas.append(1)
		# iteramos por fila
		for fila in range(0, len(dna)):
			# para cada nueva fila el contador de elementos iguales por fila se reinicia a 1 
    		elementosIgualesFila = 1
    		# iteramos por columnas (caracteres de la cadena ubicada en la posicion fila)
    		for columna in range(0, len(dna[row])):
    			# obtenemos el elemento actual
        		elementoActual = dna[row][col]

		        # chequear con elementos en la misma fila
		        if col > 0:
		        	# solo si existe un elemento previo
		        	# buscamos el anterior en la misma fila , es decir en la columna anterior
		            elementoPrevio = dna[row][col - 1]
		            if elementoActual == elementoPrevio:
		            	# si el elemento actual es igual al previo en la fila
		            	# sumamos uno al contador
		                elementosIgualesFila += 1
		                if elementosIgualesFila == cantidadIguales:
		                	# cuando llegamos a la cantidad considerada de elementos iguales sumamos uno al contador 
		                	# de secuencias en linea
		                	contadorSecuenciasIguales += 1
		                	if contadorSecuenciasIguales >= secuenciasIgualesMinima:
		                		# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
		                		# para cortar cuanto antes
		                		return True
		                	#TODO: deberiamos reiniciar el contador de elementos iguales por fila?
		                    
		            else:
		            	# si no es igual reiniciamos directamente
		                elementosIgualesFila = 1

		        # verificar  con elementos en la misma columna
		        if row > 0:
		        	# solo si existe una columna previa
		        	# obtenemos ese elmento de la fila anterior para esta columna
		            elementoPrevio = dna[row - 1][col]
		            if elementoActual == elementoPrevio:
		            	# si el actual es igual al previo
		            	# sumamos uno al contador de elementos iguales para esta columna
		                contadoresElmentosIgualesColumnas[col] += 1
		                if contadoresElmentosIgualesColumnas[col] == cantidadIguales:
		                	# cuando llegamos a la cantidad de elementos iguales en esta columna, sumamos uno a la cantidad 
		                	# de secuencias iguales
		                    contadorSecuenciasIguales += 1
		                    if contadorSecuenciasIguales >= secuenciasIgualesMinima:
		                		# apenas encontramos al menos secuenciasIgualesMinima secuencias iguales devolvemos True
		                		# para cortar cuanto antes
		                		return True
		                    #TODO: deberiamos reiniciar el contador de elementos iguales por columna?
		            else:
		            	# si no es igual vamos a reiniciar el contador de elemntos iguales por columna
		            	contadoresElmentosIgualesColumnas[col] = 1

		        # TODO: hacer los mismo para diagonal considerando que los elementos se sacan
		  #       # para el elemento anterior arriba a la izquierda
		  #       dna[row - 1][col - 1]
		  #       # para el elemento anterior arriba a la derecha
				# dna[row - 1][col + 1]



		# TODO manejar el False
