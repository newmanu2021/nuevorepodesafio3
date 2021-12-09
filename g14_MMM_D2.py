numeros=[100,2,33,4,5,687,7,8,9,10,11,12,130,14,15]

def promedio (numeros):
    return sum(numeros)/len(numeros)

def programa (numeros):
    print ("Mayor: "+str(max (numeros)))
    print ("Menor: "+ str(min (numeros)))
    print ("Suma: "+str(sum (numeros)))
    print ("Promedio: "+str(promedio(numeros)))