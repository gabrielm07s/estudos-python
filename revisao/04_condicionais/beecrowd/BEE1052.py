"""
beecrowd 1052 - Mês
https://www.beecrowd.com.br/judge/pt/problems/view/1052
"""

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

MONTH = int(input())

if MONTH in MONTHS:
    print(MONTHS[MONTH])
