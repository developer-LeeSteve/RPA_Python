import pandas as pd
import math

from collections import Counter
from decimal import *


getcontext().prec = 20

def _gradient(x_1, x_2, y_1, y_2):
   return (Decimal(y_2)-Decimal(y_1))/(Decimal(x_2)-Decimal(x_1))

def x_intercept(address):
   csv_data = pd.read_csv(address)
   strain_list = csv_data['strain'].tolist()
   stress_list = csv_data['stress'].tolist()

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

   _index = 0

   for i in range(len(strain_list)):
      if strain_list[i] < 0.0035:
         pass
      elif strain_list[i] >= 0.0035:
         _index = i
         break
   b_value = Decimal(stress_list[_index]) - Decimal(final_gradient*strain_list[_index])
   _x_intercept = Decimal(Decimal(-b_value)/Decimal(final_gradient))
   if _x_intercept < 0:
      _x_intercept = float(-_x_intercept)
   else:
      _x_intercept = float(_x_intercept)

   return "%.10f" %(_x_intercept)