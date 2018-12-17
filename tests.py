import requests
import json
import pdb


url = "http://ec2-18-231-192-215.sa-east-1.compute.amazonaws.com:8080"



mutantService = "/mutant/"
statsService = "/stats/"

clearDataService = "/clearData/"

print("Testeando clearData")
print("")


payload = ""

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url+clearDataService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 200:
	jsonResult = json.loads(response.text)
	if jsonResult['ratio'] == 0 and jsonResult['count_human_dna'] == 0 and jsonResult['count_mutant_dna'] == 0 :
		print("Pasó el test\n\n")
	else:
		print("NO Pasó el test\n\n")

# una verdadera
payload = "{\"dna\":[\"TTGCTG\",\"CTGTAC\",\"TTTACG\",\"AAATGG\",\"CCCTTG\",\"TCACTG\"]}"

print("Testeando /mutant/ con un mutante: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 200:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")

# una falsa
payload = "{\"dna\":[\"TAGCTG\",\"CTGTAC\",\"TTTACA\",\"AAATGG\",\"CCCTTG\",\"TCACTG\"]}"


print("Testeando /mutant/ con un humano: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 403:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")


# otra verdadera
payload = "{\"dna\":[\"TAGCTG\",\"CTGTAC\",\"TTTACA\",\"TAATGG\",\"TCCTTG\",\"TCACTG\"]}"

print("Testeando /mutant/ con otro mutante: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 200:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")



# la misma verdadera
payload = "{\"dna\":[\"TAGCTG\",\"CTGTAC\",\"TTTACA\",\"TAATGG\",\"TCCTTG\",\"TCACTG\"]}"

print("Testeando /mutant/ con el mismo mutante: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 200:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")




print("Testeando /stats/")


payload = ""

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url+statsService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 200:
	jsonResult = json.loads(response.text)
	if jsonResult['ratio'] == 2.0 and jsonResult['count_human_dna'] == 1 and jsonResult['count_mutant_dna'] == 2 :
		print("Pasó el test\n\n")
	else:
		print("NO Pasó el test\n\n")


# una falsa
payload = "{\"dna\":[\"TAGCTG\",\"CTGTAC\",\"TCTACA\",\"AGATGG\",\"CCCTTG\",\"TCACTA\"]}"


print("Testeando /mutant/ con otro humano: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 403:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")



# una falsa
payload = "{\"dna\":[\"GAGCTG\",\"CTGTAG\",\"ACTACA\",\"AGATCG\",\"CCCTTG\",\"TCACTA\"]}"


print("Testeando /mutant/ con otro humano: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 403:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")


# una falsa
payload = "{\"dna\":[\"GAGCTG\",\"CTGTAG\",\"ACTCCA\",\"AGACCA\",\"CCATTT\",\"TCACGA\"]}"


print("Testeando /mutant/ con otro humano: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 403:
	print("Pasó el test\n\n")
else:
	print("NO Pasó el test\n\n")



print("Testeando /stats/")


payload = ""

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url+statsService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 200:
	jsonResult = json.loads(response.text)
	if jsonResult['ratio'] == 0.5 and jsonResult['count_human_dna'] == 4 and jsonResult['count_mutant_dna'] == 2 :
		print("Pasó el test\n\n")
	else:
		print("NO Pasó el test\n\n")



# una mal formateada
payload = "{\"dna\":[\"GAGCTG\",\"CTGTA\",\"ACTCCA\",\"AGA\",\"CCATTT\",\"TCACGA\"]}"


print("Testeando /mutant/ con un dna que no es matriz cuadrada: "+str(payload))

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url+mutantService, data=payload, headers=headers)

print("Respuesta")
print(response.text+str(" status code = ")+str(response.status_code))

if response.status_code == 403:
	jsonResult = json.loads(response.text)
	if jsonResult["message"] == "DNA No valido para analizar" and jsonResult["status"] == "Error":
		print("Pasó el test\n\n")
	else:
		print("NO Pasó el test\n\n")
