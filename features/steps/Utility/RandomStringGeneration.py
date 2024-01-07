import random
import string


def random_number_generator():
    ph_no = [random.randint(7, 9)]

    for i in range(1, 10):
        ph_no.append(random.randint(0, 9))

    ph_no_value = ''.join(str(i) for i in ph_no)
    return ph_no_value


def random_string_generator():
    result_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    return result_string


