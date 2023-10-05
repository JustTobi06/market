menu = {"pizza": 250,
               "burger": 189,
               "hranolky": 80,
               "okurka": 20,
               "mrkev": 15,
               "rajce": 12,
               "voda": 10,
               "dzus": 20,
               "pivo": 30,}
kosik = []
dohromady = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key}: {value:}Kč")
print("------------------------")

while True:
    jidlo = input("Vyber si produkt (pro ukončení napiš konec): ")
    if jidlo == "konec":
        break
    elif menu.get(jidlo) is not None:
        kosik.append(jidlo)

print("------ vaše objednávka ------")
for jidlo in kosik:
    dohromady += menu.get(jidlo)
    print(jidlo, end=" ")

print()
print(f"Musíte zaplatit {dohromady:} Kč")