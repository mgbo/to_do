
import csv
import math

lat = float(input("Enter a latitude : "))
lon = float(input("Enter a longitude :"))

f_p = 6373
s_p = 6373

ans_1 = 0
ans_2 = 0


def length(lat, lon, n_lat, n_lon):
	return math.sqrt((n_lat - lat)**2 + (n_lon - lon)**2)


with open('location_1.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		n_lat = float(row[0])
		n_lon = float(row[1])
		d = length(lat, lon, n_lat, n_lon)
		print(d)

		if f_p > d:
			# s_p = f_p
			# ans_2 = ans_1
			f_p = d
			ans_1 = row
			print("ans 1 : ", ans_1)
			print("ans 2 : ", ans_2)
		# else:
		# 	if s_p > d:
		# 		s_p = d

print(f"first near : {ans_1}")
print(f"second near : {ans_2}")


# f = open("near_pos.txt", 'w')
# f.write(ans_1.split())
# f.close()

