from reader import Reader
from chooser import Chooser

file = Reader("form.csv")
file.clean_odd_classes()
file.clean_odd_alone_sectors()
chooser = Chooser(file.classes, file.alone_sectors, file.alone_students)
result = chooser.assign_students()
print(result)