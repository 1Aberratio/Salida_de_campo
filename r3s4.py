Contador_Ambos, Contador_Dias = 0,0
Contador_Min, Contador_Max = 0,0
diasTempMax, diasTempMin = [],[]

while True:
    Temperatura_Max = int(input('Ingrese temperatura máxima: '))    
    Temperatura_Min = int(input('Ingrese temperatura mínima: '))      
    if Temperatura_Max == 0 and Temperatura_Min == 0: break 
    elif Temperatura_Max > 35 and Temperatura_Min < 5: Contador_Ambos += 1 # Si ambos días tiene errores, no se deben tener en cuenta para los otros conteos, solo para este.
    elif Temperatura_Max <= 35 and Temperatura_Min < 5: Contador_Min += 1 # Solo se tiene en cuenta los días con errores menores a 5, no con ambos errores (max 35 y min 5)
    elif Temperatura_Max > 35 and Temperatura_Min >= 5: Contador_Max += 1 # Solo se tiene en cuenta los días con errores mayores a 35, no con ambos errores (max 35 y min 5)
    elif Temperatura_Min <= 35 and Temperatura_Min >= 5: # Solo tiene en cuenta los días sin error en ambas temperaturas.
        diasTempMin.append(Temperatura_Min) # Agrega los días sin error en las temperaturas mínimas.
        diasTempMax.append(Temperatura_Max) # Agrega los días sin error en las temperaturas máximas.   
    Contador_Dias += 1 # Total días de campo.
    
Dias_Error = Contador_Min+Contador_Max+Contador_Ambos
Media_Max = sum(diasTempMax)/len(diasTempMax) # La media(promedio) se calcula sumando todos los números, después divide por cuántos números hay. 
Media_Min = sum(diasTempMin)/len(diasTempMin) # La media(promedio) se calcula sumando todos los números, después divide por cuántos números hay.
Porcentaje_Dias_Error = (Dias_Error*100)/Contador_Dias
#print()
print(Contador_Dias, 'Contador_Dias')
print(Dias_Error, 'Dias_Error')
print(Contador_Min, 'Contador_Min')
print(Contador_Max, 'Contador_Max')
print(Contador_Ambos, 'Contador_Ambos')
print(Media_Max, 'Media_Max')
print(Media_Min, 'Media_Min')
print(Porcentaje_Dias_Error, 'Porcentaje_Dias_Error')
