from reader import Reader
from chooser import Chooser
import csv

file = Reader("form.csv")
file.clean_odd_classes()
file.clean_odd_alone_sectors()
chooser = Chooser(file.classes, file.alone_sectors, file.alone_students)
result = chooser.assign_students()
print(result, len(result.keys()))

for sender in result.keys():
    mail = file.data["Mail"][file.data["Nom"].index(sender.split()[0])]
    result[sender] = (result[sender], mail)

with open("result3121354655.csv", "w", newline="") as result_file:
    writer = csv.writer(
        result_file, delimiter=";", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    writer.writerow(["Envoyeur", "Mail envoyeur", "Receveur"])
    for student in result.keys():
        writer.writerow([student, result[student][1], result[student][0]])
