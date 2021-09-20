
import math
lat1 = float(input())
lon1 = float(input())
lat2 = float(input())
lon2 = float(input())

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

R = 6371.0
dlon = lon2 - lon1
dlat = lat2 - lat1

a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
print(a)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
print(c)

distance = R * c
print(f"{round(distance, 2)} Kilometer")