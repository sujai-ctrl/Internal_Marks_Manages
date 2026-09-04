def calculate_internal(test1, test2, assignment, attendance):
    """
    Prototype calculation.

    Test 1       -> 25%
    Test 2       -> 25%
    Assignment   -> 25%
    Attendance   -> 25%
    """

    internal_mark = (
        test1 * 0.25 +
        test2 * 0.25 +
        assignment * 0.25 +
        attendance * 0.25
    )

    return round(internal_mark, 2)


def get_grade(mark):

    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"