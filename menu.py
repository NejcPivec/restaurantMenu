print("Pozdravljen, sem program, ki ti bo dnevni meni prenesel v txt datoteko")

jedilniList = {}

while True:
    hrana = input("Vnesi jed iz dnevnega menija: ")
    hrana = hrana.capitalize()

    cena = input(f"Vnesi ceno {hrana}: ")

    jedilniList[hrana] = cena

    con = input("Bi želeli vnesti novo jed? [y/n]")
    if con.lower() == "n":
        print("Hvala vaš meni je v TXT datoteki")
        break


#print(jedilniList)
with open("Menu.txt", "w") as text_file:
    for hrana, cena in jedilniList.items():
        text_file.write(f"{hrana}: {cena} € \n")
      


