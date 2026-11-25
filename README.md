# Gradebook

Small pure functions for computing grades. No globals, and no input is modified.

## Functions

| Function | Input | Output |
|---|---|---|
| `average(scores)` | list of numbers | mean, or `None` if empty |
| `letter_grade(score)` | number 0 to 100, or `None` | `A`, `B`, `C`, `D`, `F`, or `N/A` |
| `class_report(students)` | list of `{"name", "scores"}` dicts | list of `{"name", "average", "grade"}` dicts |
| `pass_rate(students, pass_mark=40)` | same as `class_report` | percentage who passed |

## Grade bands

A: 70 and above, B: 60 to 69, C: 50 to 59, D: 40 to 49, F: below 40.

## Edge cases

- Empty score list: `average` returns `None`, the grade is `N/A`.
- Scores of exactly 0 or 100 are valid. Anything outside 0 to 100 raises `ValueError`.
- Student with no scores: shown as `N/A` and not counted in the pass rate.
- Duplicate names: each record is reported separately.
- Nobody has scores: `pass_rate` returns `0.0`.

## Usage

```python
from gradebook import class_report, pass_rate

students = [
    {"name": "Amina", "scores": [80, 90]},
    {"name": "Brian", "scores": [30, 40]},
]
print(class_report(students))
print(pass_rate(students))
```

## Running the tests

From the `gradebook` folder:

```
python -m unittest discover -s tests -t .
```
# assignments2
