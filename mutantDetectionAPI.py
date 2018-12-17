#!bin/python
from flask import Flask, jsonify , request
from dotenv import find_dotenv, load_dotenv
import os
# Import para el manejo de datos 
import pdb
from flask import Response
import logging
import json
from Controllers import MutantDetectionAPIController

app = Flask(__name__)

# Inicializacion del logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('mutantDetectionAPI.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('comienzo logger')


# --------------------------------------------------------------------------------------------------------------------------------
# ENDPOINTS

# Endpoint para verificar si un dna es de un mutante  por POST
@app.route('/mutant/', methods=['POST'])
def analizeDna():

	logger.info("Entrando a validar dna")

	if not request.json or not 'dna' in request.json:
		logger.info('\n Parametros incorrectos')
		return jsonify({'status': 'Error', 'message': 'Parametros incorrectos'}), 403
	else:
		dna = request.json['dna']
		isMutant = controller.isMutant(dna)
		if isMutant is not None:
			# controller.saveDna(dna,isMutant)
			if isMutant:
				return jsonify({"dna":dna,"isMutant":isMutant}), 200
			else:
				return jsonify({"dna":dna,"isMutant":isMutant}), 403
		else:
			return jsonify({'status': 'Error', 'message': 'DNA No valido para analizar'}), 403

# Endpoint GET para obtener las estadisticas
@app.route('/stats/', methods=['GET'])
def getStats():
	logger.info("Entrando a get stats")
	stats = controller.getStats()
	return jsonify(stats),200
	
@app.route('/clearData/', methods=['GET'])
def clearDataBase():
	controller.clearDataBase()
	logger.info("Entrando a clear data")
	stats = controller.getStats()
	return jsonify(stats),200



@app.route('/')
def index():
	return "Bienvenido al detector de Mutantes!"


# inicializacion de la aplicacion flask
if __name__ == '__main__':
	load_dotenv(find_dotenv())

	controller = MutantDetectionAPIController()
	
	host = str(os.environ.get('host'))
	port = str(os.environ.get('port'))
	logger.info("Arrancando server en host "+host)
	app.run(use_reloader=True,host=host,port=port)
