import csv
import statistics
import math

headers = ["customer","order","total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]
variable = input()
values= []

X = headers.index(variable)

with open('ulabox_orders_with_categories_partials_2017.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if(row != headers):
            values.append(float(row[X]))
        
#Cantidad
cantidad = len(values)
#Minimo
minimo = min(values)
#Maximo
maximo = max(values)

#se calcula el promedio
media= statistics.mean(values)
#se calcula la mediana
mediana= statistics.median(values)
#se calcula la moda
moda = statistics.mode(values)

#desviacion standar
sumatoria = 0
for x in values:
    sumatoria += pow(x - media, 2)
s = math.sqrt((1/(cantidad -1)) * sumatoria)

#posicion
porcentaje25 = cantidad // 4
porcentaje50 = cantidad // 2
porcentaje75 = porcentaje50 + porcentaje25
porcentaje100 = porcentaje50 * 2

q1 = values[porcentaje25 -1]
q2 = values[porcentaje50 -1]
q3 = values[porcentaje75 -1]
q4 = values[porcentaje100 -1]


print("Variable: %s \t cantida: %d" %(variable, cantidad))
#print("Variable: %s" %variable)
print("Minimo: %d, maximo: %d" %(minimo, maximo) )
print("Media: %d" %media)
print("Mediana: %d" %mediana)
print("Moda: %d" %moda)
print("Desviacion estandar: %d" %s)
print("Q1: %d \t")