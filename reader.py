import csv
import random


class Reader:
    def __init__(self, sheet):
        with open(sheet, newline="") as form:
            datas = csv.reader(form, delimiter=";")

            self.datas = []
            for row in datas:
                self.datas.append(row)

            self.data = dict()
            l2 = len(self.datas[0])
            l1 = len(self.datas)
            for i in range(l2):
                self.data[self.datas[0][i]] = []
                for j in range(1, l1):
                    self.data[self.datas[0][i]].append(self.datas[j][i].strip())

            self.alone_sectors = dict()
            self.alone_students = []

        self.classes = dict()
        for i in range(len(self.data["Nom"])):
            if (
                self.data["Filière"][i] + self.data["Classe"][i]
                not in self.classes.keys()
            ):
                self.classes[self.data["Filière"][i] + self.data["Classe"][i]] = [
                    self.data["Nom"][i] + " " + self.data["Prénom"][i]
                ]
            else:
                self.classes[self.data["Filière"][i] + self.data["Classe"][i]].append(
                    self.data["Nom"][i] + " " + self.data["Prénom"][i]
                )

    def get_classes(self):
        return self.classes.keys()

    def get_students_by_class_number(self, class_number):
        return self.classes[class_number]

    def clean_odd_classes(self):
        for class_number in self.classes.keys():
            if len(self.classes[class_number]) % 2 == 1:
                k = random.randint(0, len(self.classes[class_number]) - 1)
                if class_number[:-1] not in self.alone_sectors.keys():
                    self.alone_sectors[class_number[:-1]] = [
                        self.classes[class_number].pop(k)
                    ]
                else:
                    self.alone_sectors[class_number[:-1]].append(
                        self.classes[class_number].pop(k)
                    )

    def clean_odd_alone_sectors(self):
        for sector in self.alone_sectors.keys():
            if len(self.alone_sectors[sector]) % 2 == 1:
                k = random.randint(0, len(self.alone_sectors[sector]) - 1)
                self.alone_students.append(self.alone_sectors[sector].pop(k))

    def get_alone_students(self):
        return self.alone_students


if __name__ == "__main__":
    file = Reader("form.csv")
