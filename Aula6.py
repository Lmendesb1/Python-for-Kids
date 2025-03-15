temp = int(input("Temperatura de hoje: "))
if temp<14:
    print("dia frio")
elif 14<temp<18:
    print("dia fresco")
elif 18<temp<25:
    print("dia ameno")
else:
    print("dia quente")