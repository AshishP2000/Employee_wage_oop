import random


class EmployeeWage:

    def __init__(self):
        self.PRESENT = 0
        self.ABSENT = 1

    def present_absent(self):
        """
        :return: a random number between 0 and 1
        """
        return random.randint(0, 1)

    def check_presence(self):
        """
        check if employee is present or not
        """
        if self.present_absent() == self.PRESENT:
            print("EMPLOYEE IS PRESENT")
        else:
            print("EMPLOYEE IS ABSENT")


if __name__ == '__main__':
    # creating object of an EmployeeWage()
    employee = EmployeeWage()
    employee.check_presence()
