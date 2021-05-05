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
        
values.sort()

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

indexq1 = cantidad // 4
indexq3 = ((3 * cantidad) + 2) // 4

q1 = values[indexq1]
q2 = mediana
q3 = values[indexq3]
q4 = values[cantidad -1]
iqr = q3 - q1 

print("Variable: %s \t cantida: %d" %(variable, cantidad))
#print("Variable: %s" %variable)
print("Minimo: %f, maximo: %f" %(minimo, maximo) )
print("Media: %f" %media)
print("Mediana: %f" %mediana)
print("Moda: %f" %moda)
print("Desviacion estandar: %f" %s)
print("Q1: %f \t Q2: %f \t Q3: %f \t Q4: %f \t" %(q1, q2, q3, q4))
print("IQR: %f" %iqr)