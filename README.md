# Salida_de_campo
Solución al reto 3, semana 4 del ciclo 1; Universidad El Bosque.

# Ciclo 1: Semana 4 Reto 3
![MisiónTic 2022](https://www.mintic.gov.co/portal/715/articles-160227_foto_marquesina.thumb_principal.jpg)   
MisiónTic 2022 - Reto 3 Semana 4, Universidad El Bosque

**Situación**

El programa de Ingeniería ambiental de la Universidad El Bosque en una de sus salidas de
campo, ha registrado un par de temperaturas diarias (máxima, mínima) para todos los días que
permanecieron en campo. Dadas las condiciones del terreno donde se encontraban, no era
posible tener temperaturas menores de 5 grados ni mayores de 35 grados, que se consideraron
errores, pero igual se registraron para su estudio posterior. La pareja de temperaturas (0,0)
indicará que se han terminado los datos de la salida de campo.
El director del programa le ha solicitado a usted como programador, que le desarrolle un
programa en lenguaje Python que le permita:

* Leer desde el teclado todos los datos registrados en la salida de campo.
* Mostrar en consola el número total de días que duró la salida de campo.
* Mostrar en consola cuantos días en total se tuvieron temperaturas con
error, de los cuales se debe informar cuántos fueron por temperaturas
menores de 5 grados, cuántos fueron por temperaturas mayores de 35
grados y cuántos por ambos errores.
* Mostrar en consola la temperatura media mínima y media máxima, sin tener en
cuenta los días en que se reportaron errores.
* Mostrar en consola el porcentaje de días que se reportaron errores
respecto del total de días reportados.

**Parámetros de Salida (Este Orden)**:  
Contador_Dias   
Dias_Error  
Contador_Min  
Contador_Max  
Contador_Ambos  
Media_Max  
Media_Min  
Porcentaje_Dias_Error  

**DATOS DE PRUEBA**:

**Input**  
1=> 34 | 12  
2=> 38 | 4  
3=> 25 | 22  
4=> 39 | 12  
5=> 30 | 3   
6=> 36 | 9  
7=> 38 | 11  
8=> 29 | 2  
9=> 39 | 14  
0 | 0

**Output**   
9 Contador_Dias  
7 Dias_Error  
2 Contador_Min  
4 Contador_Max  
1 Contador_Ambos (dias con errores en ambas temperaturas)  
29.5 Media_Max  
17.0 Media_Min  
77.77777777777777 Porcentaje_Dias_Er  
