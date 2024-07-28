from time import sleep

time_clock = input("Digite o tempo em (Segundos): ")

if time_clock.isdigit():
    time_clock = int(time_clock)
else:
    print("Entrada Invalida!")
    quit()

# 120 / 60 = 2
# 150 / 60 = 2 | 30

while time_clock != 0:
    minutes, seconds = divmod(time_clock, 60)
    time = "{:02d}:{:02d}".format(minutes, seconds)
    print(time, end="\r")
    sleep(1)
    time_clock -= 1

print("O TEMPO ACABOU!!!")