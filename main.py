import math


def add(x, y):
    return math.ceil(x) + math.floor(y)


# import datetime as dt


# def present_value(cash_flow):

#     if not cash_flow:
#         return "Current data structure has has no Cash Flow Info"

#     # Cash Flow Formula for PV is PV = CF/(1+r)^n

#     # formula to give me current year
#     current_year = dt.datetime.now().year()

#     # we start with PV = 0
#     present_value = 0

#     # this is our r in the formula
#     discount_rate = 0.04

#     for year, amount in cash_flow.items():

#         if year < current_year:
#             continue

#         n = year - current_year
#         present_value = present_value + amount / ((1 + discount_rate) ** n)

#         return present_value


# # Test Cases
# cs_1 = {1999: 10193210,  2027: 23450, 2030: 678819} # Test case including date in the past
# cs_2 = {} # Test Case Including Blank
# cs_3  = {2024: 2300, 2025: 91021, 2026: 34599, 2030: 56660} #Normal Test Case
# cs_4 = {2024: 2300, 2025: 91021, 2026: 34599.17} #Test Case Including Decimal
