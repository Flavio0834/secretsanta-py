import csv


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
                    self.data[self.datas[0][i]].append(self.datas[j][i])
                print(self.data[self.datas[0][i]])

        self.classes = dict()
        for i in range(len(self.data["Nom"])):
            if (
                self.data["Filière"][i] + self.data["Classe"][i]
                not in self.classes.keys()
            ):
                self.classes[self.data["Filière"][i] + self.data["Classe"][i]] = [
                    self.data["Nom"][i] + self.data["Prénom"][i]
                ]
            else:
                self.classes[self.data["Filière"][i] + self.data["Classe"][i]].append(
                    self.data["Nom"][i] + self.data["Prénom"][i]
                )

    def get_classes(self):
        return self.classes.keys()

    def get_students_by_class_number(self, class_number):
        return self.classes[class_number]


if __name__ == "__main__":
    file = Reader("form.csv")
