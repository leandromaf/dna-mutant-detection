# -*- coding: utf-8 -*-
import pdb
from dotenv import find_dotenv, load_dotenv
#Import para acceder a mongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

# Experto para manejo de base de datos MongoDB
class MongoDataBaseExpert:

	def __init__(self):
		load_dotenv(find_dotenv())
		self.dbuser = str(os.environ.get('dbuser'))
		self.dbpass = str(os.environ.get('dbpass'))
		self.dbname = str(os.environ.get('dbname'))
		self.dbhost = str(os.environ.get('dbhost'))
		self.clientMongo = MongoClient('mongodb://'+self.dbuser+':'+self.dbpass+'@'+self.dbhost+':27017/'+self.dbname+'?authSource=admin')
		# accedemos a la base de datos 
		self.dbMongo = self.clientMongo[self.dbname]

	# funcion que agrega un dna a la base (si no existe) especificando si es mutante o no
	def saveDna(self,dna,isMutant):
		# generar una cadena de todo el dna para identificacion unica
		dnaString = ''.join(dna)
		count = self.dbMongo.dnas.find({'dnaString':dnaString}).count()
		if count == 0 :
			# insertar la clustered location
			d = {'dnaString':dnaString,'dna':dna,'isMutant':isMutant}
			self.dbMongo.dnas.insert_one(d)

	# funcion que  devuelve la cantidad de mutantes
	def getCountMutants(self):
		count = self.dbMongo.dnas.find({'isMutant':True}).count()
		return count

	# funcion que  devuelve la cantidad de humanos
	def getCountHumans(self):
			count = self.dbMongo.dnas.find({'isMutant':False}).count()
			return count

