import copy
import unittest

from gradebook import average, class_report, letter_grade, pass_rate


def sample_students():
    return [
        {"name": "Amina", "scores": [80, 90]},
        {"name": "Brian", "scores": [30, 40]},
        {"name": "Cate", "scores": []},
    ]


class TestAverage(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(average([50, 70, 90]), 70)

    def test_empty_returns_none(self):
        self.assertIsNone(average([]))

    def test_single_score(self):
        self.assertEqual(average([55]), 55)

    def test_does_not_mutate(self):
        scores = [3, 1, 2]
        average(scores)
        self.assertEqual(scores, [3, 1, 2])


class TestLetterGrade(unittest.TestCase):
    def test_bands(self):
        self.assertEqual(letter_grade(85), "A")
        self.assertEqual(letter_grade(65), "B")
        self.assertEqual(letter_grade(55), "C")
        self.assertEqual(letter_grade(45), "D")
        self.assertEqual(letter_grade(20), "F")

    def test_lower_edges(self):
        self.assertEqual(letter_grade(70), "A")
        self.assertEqual(letter_grade(60), "B")
        self.assertEqual(letter_grade(50), "C")
        self.assertEqual(letter_grade(40), "D")
        self.assertEqual(letter_grade(39.9), "F")

    def test_zero_and_hundred(self):
        self.assertEqual(letter_grade(0), "F")
        self.assertEqual(letter_grade(100), "A")

    def test_none_gives_na(self):
        self.assertEqual(letter_grade(None), "N/A")

    def test_out_of_range_raises(self):
        with self.assertRaises(ValueError):
            letter_grade(101)
        with self.assertRaises(ValueError):
            letter_grade(-1)


class TestClassReport(unittest.TestCase):
    def test_normal(self):
        report = class_report(sample_students())
        self.assertEqual(report[0], {"name": "Amina", "average": 85, "grade": "A"})
        self.assertEqual(report[1], {"name": "Brian", "average": 35, "grade": "F"})

    def test_student_with_no_scores(self):
        report = class_report(sample_students())
        self.assertEqual(report[2], {"name": "Cate", "average": None, "grade": "N/A"})

    def test_missing_scores_key(self):
        report = class_report([{"name": "Dan"}])
        self.assertEqual(report[0]["grade"], "N/A")

    def test_duplicate_names_kept(self):
        students = [
            {"name": "Sam", "scores": [90]},
            {"name": "Sam", "scores": [20]},
        ]
        report = class_report(students)
        self.assertEqual(len(report), 2)
        self.assertEqual([r["grade"] for r in report], ["A", "F"])

    def test_does_not_mutate_input(self):
        students = sample_students()
        before = copy.deepcopy(students)
        class_report(students)
        self.assertEqual(students, before)

    def test_empty_class(self):
        self.assertEqual(class_report([]), [])


class TestPassRate(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(pass_rate(sample_students()), 50.0)

    def test_everyone_passes(self):
        students = [{"name": "A", "scores": [40]}, {"name": "B", "scores": [100]}]
        self.assertEqual(pass_rate(students), 100.0)

    def test_empty_class(self):
        self.assertEqual(pass_rate([]), 0.0)

    def test_nobody_has_scores(self):
        self.assertEqual(pass_rate([{"name": "A", "scores": []}]), 0.0)

    def test_does_not_mutate_input(self):
        students = sample_students()
        before = copy.deepcopy(students)
        pass_rate(students)
        self.assertEqual(students, before)


if __name__ == "__main__":
    unittest.main()
