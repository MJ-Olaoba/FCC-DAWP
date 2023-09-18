import numpy as np

def calculate(list):
  b = np.array(list)
  x = b.reshape(3,3)
  mean_axis1 = x.mean(axis=0)
  mean_axis1l = mean_axis1.tolist()
  mean_axis2 = x.mean(axis=1)
  mean_axis2l = mean_axis2.tolist()
  mean_flat = x.mean()

  var_axis1 = x.var(axis=0)
  var_axis1l = var_axis1.tolist()
  var_axis2 = x.var(axis=1)
  var_axis2l = var_axis2.tolist()
  var_flat = x.var()

  std_axis1 = x.std(axis=0)
  std_axis1l = std_axis1.tolist()
  std_axis2 = x.std(axis=1)
  std_axis2l = std_axis2.tolist()
  std_flat = x.std()

  max_axis1 = x.max(axis=0)
  max_axis1l = max_axis1.tolist()
  max_axis2 = x.max(axis=1)
  max_axis2l = max_axis2.tolist()
  max_flat = x.max()

  min_axis1 = x.min(axis=0)
  min_axis1l = min_axis1.tolist()
  min_axis2 = x.min(axis=1)
  min_axis2l = min_axis2.tolist()
  min_flat = x.min()

  sum_axis1 = x.sum(axis=0)
  sum_axis1l = sum_axis1.tolist()
  sum_axis2 = x.sum(axis=1)
  sum_axis2l = sum_axis2.tolist()
  sum_flat = x.sum()

  calculation = {'mean': [mean_axis1l, mean_axis2l, mean_flat], 
  'variance': [var_axis1l, var_axis2l, var_flat], 
  'standard deviation': [std_axis1l, std_axis2l, std_flat], 
  'max': [max_axis1l, max_axis2l, max_flat], 
  'min': [min_axis1l, min_axis2l, min_flat], 
  'sum': [sum_axis1l, sum_axis2l, sum_flat]}
  print(calculation)
  
  return calculation