from datetime import date
import statistics


def make_health_profile(data):
    def get_name():
        return data[0]

    def get_dob():
        return data[1]

    def get_height():
        return data[2]

    def get_weight():
        return data[3]

    def calculate_bmi():
        return data[3] / ((data[2] / 100) ** 2)

    def get_age():
        return date.today().year - get_dob().year

    def get_target_hr():
        moderate_min = (220 - get_age()) * 0.64
        moderate_max = (200 - get_age()) * 0.76

        return moderate_min, moderate_max

    return {'get_name': get_name, 'get_dob': get_dob,
            'get_height': get_height, 'get_weight': get_weight,
            'get_age': get_age, 'get_bmi': calculate_bmi,
            'get_target_hr': get_target_hr}


def calculate_age_stats(list_of_patients):
    ages = [patient['get_age']() for patient in list_of_patients]
    mean_age = statistics.mean(ages)
    std_dev_age = statistics.stdev(ages)
    return mean_age, std_dev_age


def find_people_at_risk(list_of_patients, pos=None, list_of_patients_at_risk=None):
    if pos is None:
        pos = 0

    if list_of_patients_at_risk is None:
        list_of_patients_at_risk = []

    if pos > len(list_of_patients) - 1:
        return list_of_patients_at_risk
    else:
        if list_of_patients[pos]['get_bmi']() < 18.5 or list_of_patients[pos]['get_bmi']() > 24.9:
            list_of_patients_at_risk.append(list_of_patients[pos]['get_name']())
        return find_people_at_risk(list_of_patients, pos + 1, list_of_patients_at_risk)
