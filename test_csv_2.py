
import csv
import random
#
with open('new_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:
        print(line)

#
# with open('new_file.csv', 'w', newline='') as new_file:
#     csv_writer = csv.writer(new_file, delimiter=',')
#     for i in range(300):
#         for j in range(300):
#             data = [i, j, random.randint(5, 20)]
#             csv_writer.writerow([i, j, random.randint(5, 20)])

