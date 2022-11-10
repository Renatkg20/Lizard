timur = input()
ruslan = input()


if ruslan == "Спок" and timur == "ножницы":
    print("Руслан")
elif ruslan == "камень" and timur == "ножницы":
    print("Руслан")
elif ruslan == "ножницы" and timur == "бумага":
    print("Руслан")
elif ruslan == "бумага" and timur == "камень":
    print("Руслан")
elif timur == "Спок" and ruslan == "ножницы":
    print("Руслан")
elif ruslan == "камень" and timur == "ящерица":
    print("Руслан")
elif ruslan == "ящерица" and timur == "Спок":
    print("Руслан")
elif ruslan == "Спок" and timur == "камень":
    print("Руслан")
elif ruslan == "ящерица" and timur == "бумага":
    print("Руслан")
elif ruslan == "бумага" and timur == "ножницы":
    print("Руслан")
elif ruslan == timur:
    print("ничья")
else:
    print("Тимур")