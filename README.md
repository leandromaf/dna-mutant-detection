# dna-mutant-detection

## El problema

Se considera mutante si se encuentra **más de una secuencia de cuatro letras
iguales**, de forma oblicua, horizontal o vertical en la matriz resultante de el arreglo de Strings.

Por ejemplo:

**No-Mutante**

| A | T | G | C | G | A |

| C | A | G | T | G | C |

| T | T | A | T | T | T |

| A | G | A | C | G | G |

| G | C | G | T | C | A |

| T | C | A | C | T | G |

**Mutante**

| **A** | T | G | C | **G** | A |

| C | **A** | G | T | **G** | C |

| T | T | **A** | T | **G** | T |

| A | G | A | **A** | **G** | G |

| **C** | **C** | **C** | **C** | T | A |

| T | C | A | C | T | G |

## La solucion

API REST para detectar si alguien es mutante basandose en su ADN.

Esta API recibe como parámetro un array de Strings que representan cada fila de una tabla
de (NxN) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las
cuales representa cada base nitrogenada del ADN.

El servicio “/mutant/” puede detectar si un humano es
mutante enviando la secuencia de ADN mediante un HTTP POST con un Json el cual tenga el
siguiente formato:

{

"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

}

En caso de verificar un mutante, devuelve un HTTP 200-OK, en caso contrario un
403-Forbidden

Se puede usar este servicio en el siguiente URL, usando el método POST y pasando el Json correspondiente:

http://ec2-18-231-192-215.sa-east-1.compute.amazonaws.com:8080/mutant/


El servicio  “/stats/”  devuelve un Json con las estadísticas de las
verificaciones de ADN, por ejemplo: 

{“count_mutant_dna”: 40, “count_human_dna”: 100: “ratio”: 0.4}

Se puede usar este servicio en el siguiente URL, usando el método GET:

http://ec2-18-231-192-215.sa-east-1.compute.amazonaws.com:8080/stats/


De forma accesoria existe un servicio "/clearData" que permite limpiar la base de datos donde se han registrado los resultados de análisis, el cual se puede acceder en el siguiente URL, usando el método GET:

http://ec2-18-231-192-215.sa-east-1.compute.amazonaws.com:8080/clearData/



