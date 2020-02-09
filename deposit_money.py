MAXIMUM_DEPOSIT_AMOUNT_PER_TIME = 30000.00


def check_deposit_amount_per_time(deposit_amount):
    return deposit_amount <= MAXIMUM_DEPOSIT_AMOUNT_PER_TIME


def calculate_age(DOB, current_date):
    return current_date.year - DOB.year


def calculate_deposit_fee_from(age):
    return 0.00
