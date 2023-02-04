# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

print('Enter the ticket number: ')
tiket = int(input())
summa1 = 0
summa2 = 0

while tiket:
    if tiket > 999:
        n = tiket % 10
        summa1 += n
        tiket = tiket // 10
    else:
        n = tiket % 10
        summa2 += n
        tiket = tiket // 10
if summa1 == summa2:
    print("Ticket lucky")
else:
    print("Ticket not lucky")
