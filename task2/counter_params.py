from data_tests import create_values

XPath_Water = "//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]"
XPath_CO2 = "//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]"
XPath_Energy = "//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]"

#Проверка граничных значений -1, 0, 1
test_1 = create_values(1, 1, 1)
test_2 = create_values(-1, -1, -1)
test_3 = create_values(0, 0, 0)

#Проверка работы граничных значений 999, 1000, 1100
test_4 = create_values(999, 999, 999)
test_5 = create_values(1000, 1000, 1000)
test_6 = create_values(1100, 1100, 1100)

#Проверка работы граничных значений 999999, 1000000, 1100000
test_7 = create_values(999999, 999999, 999999)
test_8 = create_values(1000000, 1000000, 1000000)
test_9 = create_values(1100000, 1100000, 1100000)

#Проверка работы граничных значений 999999999, 1000000000, 110000000
test_10 = create_values(999999999, 999999999, 999999999)
test_11 = create_values(1000000000, 1000000000, 1000000000)
test_12 = create_values(1100000000, 1100000000, 1100000000)


counter_params = [
    (test_1, XPath_Water, "1"),
    (test_1, XPath_CO2, "2"),
    (test_1, XPath_Energy, "3"),

    (test_2, XPath_Water, "4"),
    (test_2, XPath_CO2, "5"),
    (test_2, XPath_Energy, "6"),

    (test_3, XPath_Water, "7"),
    (test_3, XPath_CO2, "8"),
    (test_3, XPath_Energy, "9"),

    (test_4, XPath_Water, "10"),
    (test_4, XPath_CO2, "11"),
    (test_4, XPath_Energy, "12"),

    (test_5, XPath_Water, "13"),
    (test_5, XPath_CO2, "14"),
    (test_5, XPath_Energy, "15"),

    (test_6, XPath_Water, "16"),
    (test_6, XPath_CO2, "17"),
    (test_6, XPath_Energy, "18"),

    (test_7, XPath_Water, "19"),
    (test_7, XPath_CO2, "20"),
    (test_7, XPath_Energy, "21"),

    (test_8, XPath_Water, "22"),
    (test_8, XPath_CO2, "23"),
    (test_8, XPath_Energy, "24"),

    (test_9, XPath_Water, "25"),
    (test_9, XPath_CO2, "26"),
    (test_9, XPath_Energy, "27"),

    (test_10, XPath_Water, "28"),
    (test_10, XPath_CO2, "29"),
    (test_10, XPath_Energy, "30"),

    (test_11, XPath_Water, "31"),
    (test_11, XPath_CO2, "32"),
    (test_11, XPath_Energy, "33"),

    (test_12, XPath_Water, "34"),
    (test_12, XPath_CO2, "35"),
    (test_12, XPath_Energy, "36"),
]