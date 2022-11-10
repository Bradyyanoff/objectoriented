class Student:
    def __init__(self, name, number):
        self.name = name
        self.studentID = number
        self.classes_taken = []

    def transfer_classes(self, other_classes):
        self.classes_taken.extend(other_classes)

    def can_graduate(self):

        if len(self.classes_taken) > 40:
            return True
        else:
            return False
