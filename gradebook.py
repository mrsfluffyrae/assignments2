def average(scores):
    """Return the mean of a list of numbers.

    Input: scores, a list of numbers (not modified).
    Output: a float, or None if the list is empty or None.
    """
    if not scores:
        return None
    return sum(scores) / len(scores)


def letter_grade(score):
    """Convert a score to a letter grade.

    Input: score, a number from 0 to 100, or None.
    Output: "A" (70+), "B" (60+), "C" (50+), "D" (40+), "F" (below 40),
    or "N/A" if score is None.
    Raises ValueError if the score is below 0 or above 100.
    """
    if score is None:
        return "N/A"
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:
        return "C"
    if score >= 40:
        return "D"
    return "F"


def class_report(students):
    """Build a report with one entry per student record.

    Input: students, a list of dicts like {"name": "Amina", "scores": [80, 90]}.
    A missing or empty "scores" is allowed. The input is not modified.
    Output: a new list of dicts with keys "name", "average" (rounded to
    2 decimals, or None) and "grade". Duplicate names are kept as
    separate entries.
    """
    report = []
    for student in students:
        avg = average(student.get("scores"))
        if avg is not None:
            avg = round(avg, 2)
        report.append({
            "name": student["name"],
            "average": avg,
            "grade": letter_grade(avg),
        })
    return report


def pass_rate(students, pass_mark=40):
    """Return the percentage of students who passed.

    Input: students, as for class_report; pass_mark, the lowest passing
    average (default 40).
    Output: a float from 0.0 to 100.0. Students with no scores are not
    counted. Returns 0.0 if nobody has scores.
    """
    graded = [r for r in class_report(students) if r["average"] is not None]
    if not graded:
        return 0.0
    passed = [r for r in graded if r["average"] >= pass_mark]
    return len(passed) / len(graded) * 100
