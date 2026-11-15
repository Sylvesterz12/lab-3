import employee_info


def test_get_employees_by_age_range():
    # Ages strictly between 24 and 33: John (30), Jane (25), Mike (32)
    result = employee_info.get_employees_by_age_range(24, 33)

    names = []
    for item in result:
        names.append(item["name"])

    assert (names == ["John", "Jane", "Mike"])


def test_get_employees_by_age_range_exclusive_limits():
    # Limits are exclusive: 25 and 35 themselves are not included
    result = employee_info.get_employees_by_age_range(25, 35)

    names = []
    for item in result:
        names.append(item["name"])

    assert (names == ["John", "Mike"])


def test_get_employees_by_age_range_no_match():
    result = employee_info.get_employees_by_age_range(50, 60)

    assert (result == [])


def test_calculate_average_salary():
    # (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6 = 60166.666...
    result = employee_info.calculate_average_salary()

    assert (result == (361000 / 6))


def test_get_employees_by_dept_sales():
    result = employee_info.get_employees_by_dept("Sales")

    names = []
    for item in result:
        names.append(item["name"])

    assert (names == ["John", "Peter"])


def test_get_employees_by_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")

    names = []
    for item in result:
        names.append(item["name"])

    assert (names == ["Chloe", "Mike"])


def test_get_employees_by_dept_unknown():
    result = employee_info.get_employees_by_dept("HR")

    assert (result == [])