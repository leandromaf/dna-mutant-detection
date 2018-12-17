# -*- coding: utf-8 -*-
import pdb
from MutantDetectionExperts import DNAMutantDetectionExpert
from DataBaseExperts import MongoDataBaseExpert

# Eperto en deteccion de mutantes analizando su DNA
class MutantDetectionAPIController:

	def __init__(self):

		self.mutantDetectionExpert = DNAMutantDetectionExpert()
		self.dataBaseExpert = MongoDataBaseExpert()

	def __validateDna(self,dna):
		# Validar que sea una matriz cuadrada
		dnaString = ''.join(dna)
		if dnaString.__len__() == (dna.__len__()*dna.__len__()):
			return True
		else:
			return False

	def isMutant(self,dna):

		if self.__validateDna(dna):
			# si es un dna valido
			isMutant = self.dataBaseExpert.getDna(dna)
			if isMutant is not None:
				return isMutant
			else:
				isMutant = self.mutantDetectionExpert.isMutant(dna)
				self.dataBaseExpert.saveDna(dna,isMutant)
				return isMutant
		else:
			return None



	def getStats(self):

		count_mutant_dna = self.dataBaseExpert.getCountMutants()
		count_human_dna = self.dataBaseExpert.getCountHumans()
	
		if count_mutant_dna == 0 or count_human_dna == 0 :
			ratio = 0
		else:
			ratio = float(count_mutant_dna / count_human_dna)

		return {"count_mutant_dna":count_mutant_dna, "count_human_dna":count_human_dna,"ratio":ratio}


	def clearDataBase(self):
		self.dataBaseExpert.clearDataBase()


