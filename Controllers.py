# -*- coding: utf-8 -*-
import pdb
from MutantDetectionExperts import DNAMutantDetectionExpert
from DataBaseExperts import MongoDataBaseExpert

# Eperto en deteccion de mutantes analizando su DNA
class MutantDetectionAPIController:

	def __init__(self):

		self.mutantDetectionExpert = DNAMutantDetectionExpert()
		self.dataBaseExpert = MongoDataBaseExpert()

	def isMutant(self,dna):

		return self.mutantDetectionExpert.isMutant(dna)

	def saveDna(self,dna,isMutant):

		self.dataBaseExpert.saveDna(dna,isMutant)


	def getStats(self):

		count_mutant_dna = self.dataBaseExpert.getCountMutants()
		count_human_dna = self.dataBaseExpert.getCountHumans()
	
		if count_mutant_dna == 0 :
			ratio = 0
		else:
			ratio = float(count_mutant_dna / count_human_dna)

		return {"count_mutant_dna":count_mutant_dna, "count_human_dna":count_human_dna,"ratio":ratio}


	def clearDataBase(self):
		self.dataBaseExpert.clearDataBase()


