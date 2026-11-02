import ET0735_Lab2.lab2 as bmi


def test_bmi_normal_weight():
    # height 1.75 m, weight 70 kg -> BMI about 22.9 (normal)
    result = bmi.calculate_bmi(1.75, 70)

    assert (result == 0)


def test_bmi_over_weight():
    # height 1.75 m, weight 90 kg -> BMI about 29.4 (over weight)
    result = bmi.calculate_bmi(1.75, 90)

    assert (result == 1)


def test_bmi_under_weight():
    # height 1.75 m, weight 50 kg -> BMI about 16.3 (under weight)
    result = bmi.calculate_bmi(1.75, 50)

    assert (result == -1)