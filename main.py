import unittest

from email import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["adam.mickiewicz@wat.edu.pl", False, True, "Adam", "Mickiewicz"],
            ["juliusz.slowacki@wat.edu.pl", False, True, "Juliusz", "Slowacki"],
            ["izabela.lecka@student.wat.edu.pl", True, False, "Izabela", "Lecka"],
            ["andrzej.duda@student.wat.edu.pl", True, True, "Andrzej", "Duda"],
            ["hanna.mostowiak@student.wat.edu.pl", True, False, "Hanna", "Mostowiak"],
            ["adam.malysz01@student.wat.edu.pl", True, True, "Adam", "Malysz"],
            ["kamil.stoch02@wat.edu.pl", False, True, "Kamil", "Stoch"],
            ["magda.gesler@wat.edu.pl", False, False, "Magda", "Gesler"],
            ["robert.lewandowski@wat.edu.pl", False, True, "Robert", "Lewandowski"],
            ["weronika.sowa@student.wat.edu.pl", True, False, "Weronika", "Sowa"]
        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                email = x[0]
                is_student = x[1]
                extratcor = EmailExtractor(email)
                self.assertEqual(is_student, extratcor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                gender = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(gender, extractor.is_male())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                email = x[0]
                name = x[3]
                extractor = EmailExtractor(email)
                self.assertEqual(name, extractor.get_name())
