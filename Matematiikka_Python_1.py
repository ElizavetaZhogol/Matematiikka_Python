import numpy as np

# Tehtävät 1.1 a ja b

print("\n Vastaukset tehtävään 1.1 \n")

a = 2.493
b = 0.911

print(np.degrees(a))
print(np.degrees(b))

# Tehtävät 1.2 a ja b

print("\n Vastaukset tehtävään 1.2 \n")

a = 137.7
b = 62.3

print(np.radians(a))
print(np.radians(b))

# Tehtävä 1.3

print("\n Vastaukset tehtävään 1.3 \n")

A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
  print(np.radians(i))

# Tehtävä 2.1

print("\n Vastaus tehtävään 2.1 \n")

a = 1.6
b = 2.3

print(np.hypot(a, b))