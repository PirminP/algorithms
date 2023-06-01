def study_schedule(permanence_period, target_time):
    studying_students = 0
    for time_period in permanence_period:
        if (
            type(time_period[0]) != int
            or type(time_period[1]) != int
            or type(target_time) != int
        ):
            return None

        if time_period[0] <= target_time <= time_period[1]:
            studying_students += 1

    return studying_students
