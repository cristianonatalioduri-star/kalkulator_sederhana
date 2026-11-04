print(20*"=")
print("kalkulator sederhana")
print(20*"="+"\n")

angka_1 = int(input("masukan angka pertama :"))
operator = input("masukan operator : ")

angka_2 = int(input("masukan angka kedua :"))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah : {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah : {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah : {hasil}")
else:
    print("false")

print("========akhir dari program==========")


