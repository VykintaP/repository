# # # # # # # # # # # # # # # # print("a")
# # # # # # # # # # # # # # # # name = "10000000"
# # # # # # # # # # # # # # # # print(int(name))
# # # # # # # # # # # # # # # # name = input("Enter your name:")
# # # # # # # # # # # # # # # # age = input("Enter your age:")
# # # # # # # # # # # # # # # # print(f"Your name is {name} age {age}")
# # # # # # # # # # # # # # # # exercise no1
# # # # # # # # # # # # # # # # first_number = int (input ("Enter the first number:"))
# # # # # # # # # # # # # # # # second_number = int (input ("Enter the second number:"))
# # # # # # # # # # # # # # # # result = first_number + second_number
# # # # # # # # # # # # # # # # print(f"And the result is {result}")
# # # # # # # # # # # # # # # first_number = (input ("Enter the first number:"))
# # # # # # # # # # # # # # # second_number = (input ("Enter the second number:"))
# # # # # # # # # # # # # # # result = first_number + second_number
# # # # # # # # # # # # # # # print(f"And the result is {result}")
# # # # # # # # # # # # # # a = 15
# # # # # # # # # # # # # # b = 15
# # # # # # # # # # # # # # if a > b:
# # # # # # # # # # # # # #     print("whoah")
# # # # # # # # # # # # # #     print("a is less than b?")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("a is not less than b")
# # # # # # # # # # # # # # if a==b:
# # # # # # # # # # # # # # #     print("a is equals b")
# # # # # # # # # # # # # name1 = "Bob"
# # # # # # # # # # # # # name2 = "Alice"
# # # # # # # # # # # # # name3 = "Bob"
# # # # # # # # # # # # #
# # # # # # # # # # # # # if name1 == name3:
# # # # # # # # # # # # #     print ("name1 equals name3")
# # # # # # # # # # # # temp_fahrenheit = int(input("Enter temperature in Fahrenheit:"))
# # # # # # # # # # # # temp_celcius = int (temp_fahrenheit - 32) * 5/9
# # # # # # # # # # # # print(f"Temperature in Celcius {temp_celcius}")
# # # # # # # # # # # word = input("Enter the word: ")
# # # # # # # # # # # reversed = word[::-1]
# # # # # # # # # # # print("Reversed word", reversed)
# # # # # # # # # # # Using [::-1]:
# # # # # # # # # #         #
# # # # # # # # # #         # In name[::-1]:
# # # # # # # # # #         # start and stop are left blank, so it includes the entire string.
# # # # # # # # # #         # step is -1, which means to move backward through the string.
# # # # # # # # # #         # The -1 step essentially instructs Python to start from the end of the string and move backward to the beginning, effectively reversing the string.
# # # # # # # # # #         #
# # # # # # # # # # name = input("Enter your name: ")
# # # # # # # # # # surname = input ("Enter your last name: ")
# # # # # # # # # # print(
# # # # # # # # # #     f"Formatted name: {surname} { name}"
# # # # # # # # # # )
# # # # # # # # # principal_amount = input("Enter the principal amount:")
# # # # # # # # # principal_interest = input("Enter the interest rate:")
# # # # # # # # # time_period = input("Enter the time (years):")
# # # # # # # # # simple_interest = (float(principal_amount) * float(principal_interest) * float(time_period)) / 100
# # # # # # # # # print(
# # # # # # # # #     f"Simple interest is {simple_interest}")
# # # # # # # # from ntpath import split
# # # # # # # #
# # # # # # # # name = input("Enter your full name: ")
# # # # # # # # name_up = name.upper()
# # # # # # # # name_split = name_up.split()
# # # # # # # # greeting = "Hello"
# # # # # # # # complete_greeting = f"{greeting} {name_split[0]}"
# # # # # # # # print(complete_greeting)
# # # # # # # #
# # # # # # # first_number = float(input("Enter the first number: "))
# # # # # # # second_number = float(input("Enter the second number: "))
# # # # # # #
# # # # # # # if first_number > second_number:
# # # # # # #     print("The greater number is", first_number)
# # # # # # # elif first_number < second_number:
# # # # # # #     print("The greater number is", second_number)
# # # # # # # else:
# # # # # # #     print("Both numbers are equal.")
# # # # # # a = 6.897213
# # # # # # b = 231.3218
# # # # # #
# # # # # # # Suma
# # # # # # print(a + b)  # Rezultatas: 30
# # # # # #
# # # # # # # Skirtumas
# # # # # # print(a - b)  # Rezultatas: -20
# # # # # #
# # # # # # # Sandauga
# # # # # # print(a * b)  # Rezultatas: 125
# # # # # #
# # # # # # # Dalmuo
# # # # # # print(b / a)  # Rezultatas: 5.0 (float tipo, nes dalyba sukuria dešimtainę reikšmę)
# # # # # #  # Rezultatas: 1,234,567.89
# # # # # #
# # # # # # # Dalmuo be liekanos
# # # # # # print(b // a)  # Rezultatas: 5 (integer tipo)
# # # # # #
# # # # # # # Liekana
# # # # # # print(b % a)  # Rezultatas: 0
# # # # # #
# # # # # # # Laipsnis
# # # # # # print(a ** 2)  # Rezultatas: 25
# # # # # # large_number = a * b
# # # # # # print(f"{large_number:,.2f}")
# # # # # #
# # # # # # small_number = 0.632194240981-9814
# # # # # # print(f"{small_number:.2e}")  # Rezultatas: 1.23e-04
# # # # # name = "Code Academy"
# # # # #
# # # # # # Simbolių pasirinkimas
# # # # # print(name[0])  # Rezultatas: C
# # # # # print(name[5:12])  # Rezultatas: Academy
# # # # # #
# # # # # # # Teksto keitimas į didžiąsias raides
# # # # # print(name.upper())  # Rezultatas: CODE ACADEMY
# # # # # #
# # # # # # # Žodžių dalinimas
# # # # # print(name.split())  # Rezultatas: ['Code', 'Academy']
# # # # # #
# # # # # # # Teksto apjungimas
# # # # # greeting = "Sveiki, mano vardas yra"
# # # # # name = "Tomas"
# # # # # completed_greeting = f"{greeting} {name}"
# # # # # print(completed_greeting)  # Rezultatas: Sveiki, mano vardas yra Toamas
# # # # a = 7663.1 % 213.323
# # # # print (a)
# # # a = "Pabandykime ismokti, belenlka jojojo:::: kaip Ąččęčę1221 3242 3.2321 ,,,,,,,, !!!!!!!!!!! :::::"
# # # b = ()
# #
# # # # print (b)
# #
# #
# # name = "ona"
# # city = "gagai"
# #
# # b = f'ji yra {name}, gyv. {city}'
# # print(b)
# #
# # balance = 1234.56
# # balance1 = f"{balance:,.2f}"
# # print(balance1)
# #
# # sk = 218721.21972398321
# # sk1 = f"{sk:,.6e}"
# # print(sk1)
# # sk3 = 68213.821980921
# # sk2 = f"{sk3:,.3f}"
# # print(sk2)
# def keisti_tvarkarasti():
#     pamoka = "Matematika"
#
#     def keisti_pamoka():
#         nonlocal pamoka  # Leidžiame vidinei funkcijai keisti išorinės funkcijos kintamąjį
#         pamoka = "Istorija"
#
#     keisti_pamoka()
#     print(pamoka)  # Rezultatas: "Istorija"
#
#
# keisti_tvarkarasti()


# komentaras naujas
# kitas naujas komentaras
