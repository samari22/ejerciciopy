

import datetime
import random

puntos = 0

numpreguntas=1

while numpreguntas<=5:
	a= random.randint(1,10)1
	b= random.randint(1,10)

	resp = int (input ("{} +{}= ".format(a,b)))
	if resp ==(a +b):
		puntos=puntos +1

	numpreguntas=numpreguntas +1


print ("resultado={} /{} ".format(puntos,5))






