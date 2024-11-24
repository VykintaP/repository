# # # # # counter = 2
# # # # #
# # # # # while counter <= 3:
# # # # #     print(counter)
# # # # #     counter += 0.2
# # # #
# # # #
# # # # #  Skaičiuok sekundes iki sprogimo
# # # # # Sukurkite programą, kuri skaičiuoja nuo 10 iki 0 ir atspausdina „BOOM!“ kai
# # # # # pasiekia 0. Kiekvieną kartą laukite 1 sekundę tarp spausdinimų.
# # # #
# # # #
# # # # # import time
# # # # #
# # # # # # Pradinė reikšmė
# # # # # timer = 10
# # # # #
# # # # # # Ciklas, kol pasieksime 0
# # # # # while timer > 0:
# # # # #     print(timer)  # Spausdiname dabartinę sekundę
# # # # #     time.sleep(1)  # Laukiame 1 sekundę
# # # # #     timer -= 1  # Mažiname laikmatį
# # # # #
# # # # # # Kai pasiekiame 0
# # # # # print("BOOM!")
# # # #
# # # #
# # # # # import time
# # # # #
# # # # # for char in "Hello, World!":
# # # # #     print(char, end='', flush=True)  # Spausdiname simbolį po simbolio
# # # # #     time.sleep(1)  # Laukiame 0.2 sekundės po kiekvieno simbolio
# # # #
# # # # n = 1001
# # # #
# # # # while True:
# # # #     n % 6 == 0 and n % 9 == 0 and n % 15 == 0
# # # #     print (n)
# # # #     break
# # # #     n += 1
# # # #
# # # #
# # # # def skaitmenu_suma(n):
# # # #     suma = 0
# # # #     while n > 0:
# # # #         suma += n % 10  # Paimame paskutinį skaitmenį ir pridedame prie sumos
# # # #         n //= 10  # Pašaliname paskutinį skaitmenį
# # # #     return suma
# # # #
# # # #
# # # #
# # # #
# # # # skaitmenu_suma (n)
# # #
# # # while True:
# # #     user_input = input ("Įveskite 'stop', kad baigtumėte:")
# # #     if user_input.lower() == 'stop':
# # #         print("Ciklas baigtas.")
# # #         break
# # #
# # names = ["Albertas", "Ignas", "Kęstas"]
# #
# # for name in names:
# #     print (f'Sveikas, pone {name}')
# #
# #
# x = range (0, 24, 1)
#
# for n in x:
#     n += 0.32
#     print (n)

# for number in range (0, 1000):
#    if number % 3 == 0:
#         number_str = str (number)
#         last = number_str[-1]
#         if last == "3":
#             print (number)
#    else:
#      continue

