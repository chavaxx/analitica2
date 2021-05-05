import csv
import statistics


age= []
bmi = []
with open('insurance.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if(row[0]!= "age" and row[2]!= "bmi"):
            age.append(int(row[0]))
            bmi.append(float(row[2]))
        


#se calcula el promedio
promedioAge= statistics.mean(age)
promedioBmi= statistics.mean(bmi)

#se calcula la moda

modaAge = statistics.mode(age)
modaBmi = statistics.mode(bmi)

print(promedioBmi,promedioAge)
print(modaBmi,modaAge)
