import matplotlib.pyplot as plt
import pandas as pd
import math

from collections import Counter
from decimal import *


getcontext().prec = 20

def _gradient(x_1, x_2, y_1, y_2):
   return (Decimal(y_2)-Decimal(y_1))/(Decimal(x_2)-Decimal(x_1))

excel_data = pd.read_excel("C:\\Program Files\\Automation Anywhere\\Bot Agent\\tensile test\\stress_strain1.xlsx")
strain_list = excel_data['strain'].tolist()
stress_list = excel_data['stress'].tolist()

n_samples = len(strain_list)
g_list = []

for i in range(n_samples):
   if strain_list[i] > 0.02:
      break
   else:
      g_sample = _gradient(strain_list[i], strain_list[i+5], stress_list[i], stress_list[i+5])
      if g_sample <= 0:
         continue
      else: 
         g_list.append(g_sample)

n_g_samples = len(g_list)
longest_digit = 0
for i in range(n_g_samples):
   digit = int(math.log10(int(g_list[i]))+1)
   if longest_digit < digit:
      longest_digit = digit

# int_g_list = [int(x) for x in g_list]
str_g_list = [format(x, '.7f') for x in g_list]
processed_list = []
for i in range(n_g_samples):
   if '.' in str_g_list[i][:longest_digit]:
      continue
   elif '.' not in str_g_list[i][:longest_digit]:
      processed_list.append(str_g_list[i])

standard = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
n_p_samples = len(processed_list)
sorted_list_1 = []
sorted_list_2 = []
most_number = [0,0]
first_num = []
second_num = []
for i in range(n_p_samples):
   first_num.append(processed_list[i][0])
first_num = Counter(first_num).most_common()[0][0]

for i in range(n_p_samples):
   if processed_list[i][0] == first_num:
      sorted_list_1.append(processed_list[i])

for i in range(len(sorted_list_1)):
   second_num.append(sorted_list_1[i][1])
second_num = Counter(second_num).most_common()[0][0]

for i in range(len(sorted_list_1)):
   if sorted_list_1[i][1] == second_num:
      sorted_list_2.append(sorted_list_1[i])

sorted_list_2 = [float(x) for x in sorted_list_2]

final_gradient = sum([float(x) for x in sorted_list_2])/len(sorted_list_2)

coordinates = [strain_list, stress_list]
distance = []
for x,y in zip(strain_list, stress_list):
   distance.append(abs(final_gradient*x+(-1)*y+(-1)*final_gradient*0.002)/math.sqrt(final_gradient**2 + 1))

intersection = [coordinates[0][distance.index(min(distance))], coordinates[1][distance.index(min(distance))],]
TS = [coordinates[0][stress_list.index(max(stress_list))], max(stress_list)]
elongation_point = [max(strain_list), coordinates[1][strain_list.index(max(strain_list))]]

def gradient():
   return final_gradient

def _intersection():
   return intersection

if __name__ == '__main__':
   # print(_intersection())
   # print(distance)
   print("Young's Modulus: " + str("%.1f" %(final_gradient/1000)) + 'GPa')
   print("Yield Strength: " + str(intersection[1]) + 'MPa')
   print("Tensile Strength: " + str(TS[1]) + 'MPa')
   print("Elongation: " + str(elongation_point[0]))
   start = [0, 0.01]
   end = [0, final_gradient*0.01]
   g_start = [0.002, 0.012]
   g_end = [0, final_gradient*0.01]
   plt.plot(strain_list, stress_list)
   plt.plot(start, end)
   plt.plot(g_start, g_end)
   plt.plot(intersection[0], intersection[1], marker='o', markersize=4, label='Yield Strength: ' + str("%.1f" %intersection[1]) + ' MPa')
   plt.plot(TS[0], TS[1], marker='o', markersize=4, label='Tensile Strength: ' + str("%.1f" %TS[1]) + ' MPa')
   plt.plot(elongation_point[0], elongation_point[1], marker='o', markersize=4, label='Elongation Point: ' + str(elongation_point[0]))
   plt.legend()
   plt.savefig('Stress Strain.png', dpi=600)
   plt.show()
   print("Done!")