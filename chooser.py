import random


class Chooser:
    def __init__(self, classes, sectors, alones):
        self.classes = classes
        self.sectors = sectors
        self.alones = alones
        self.assignments = dict()
        self.receivers = []

        if len(self.alones) % 2 == 1:
            print(
                "Warning : Odd number of students, the secret santa can't be done correctly !!!"
            )

    def assign_students(self):
        for class_number in self.classes.keys():
            copy = [stud for stud in self.classes[class_number]]
            for student in self.classes[class_number]:
                student2 = random.choice(copy)
                while student2 == student:
                    student2 = random.choice(copy)
                    print(student, student2, copy)
                self.receivers.append(student2)
                copy.remove(student2)
                self.assignments[student] = student2

        for sector in self.sectors.keys():
            copy = [stud for stud in self.sectors[sector]]
            for student in self.sectors[sector]:
                student2 = random.choice(copy)
                while student2 == student:
                    student2 = random.choice(copy)
                    print(student, student2, copy)
                self.receivers.append(student2)
                copy.remove(student2)
                self.assignments[student] = student2

        copy = [stud for stud in self.alones]
        for student in self.alones:
            student2 = random.choice(copy)
            while student2 == student:
                student2 = random.choice(copy)
                print(student, student2, copy)
            self.receivers.append(student2)
            copy.remove(student2)
            self.assignments[student] = student2

        return self.assignments
