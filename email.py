import re


class EmailExtractor:

    def __init__(self, emailD):
        self.email = emailD

    def is_student(self) -> bool:
        regex = r"(?P<imie>[a-z]+)\.(?P<nazwisko>[a-z]+)[0-9]*@(?P<student>student\.)?wat\.edu\.pl"
        x = re.compile(regex)
        if x.match(self.email).group(3) == "student.":
            return True
        else:
            return False

    def is_male(self) -> bool:
        regex = r"(?P<imie>[a-z]+)\.(?P<nazwisko>[a-z]+)[0-9]*@(?P<student>student\.)?wat\.edu\.pl"
        x = re.compile(regex)
        if x.match(self.email).group(1).endswith("a"):
            return False
        else:
            return True

    def get_name(self) -> str:
        regex = r"(?P<imie>[a-z]+)\.(?P<nazwisko>[a-z]+)[0-9]*@(?P<student>student\.)?wat\.edu\.pl"
        x = re.compile(regex)
        return x.match(self.email).group(1).capitalize()

    def get_surname(self) -> str:
        regex = r"(?P<imie>[a-z]+)\.(?P<nazwisko>[a-z]+)[0-9]*@(?P<student>student\.)?wat\.edu\.pl"
        x = re.compile(regex)
        return x.match(self.email).group(2).capitalize()