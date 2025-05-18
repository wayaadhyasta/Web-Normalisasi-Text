# Buat dictionary kamus alay ke formal
alay_dict = {
    "gw": "saya",
    "gua": "saya",
    "loe": "kamu",
    "lu": "kamu",
    "lg": "sedang",
    "d": "di",
    "rmh": "rumah",
    "ajh": "saja",
    "kmrn": "kemarin",
    "ga": "tidak",
    "gk": "tidak",
    "td": "barusan",
    "skrg": "sekarang",
    "aja": "saja",
    "udh": "sudah",
    "bgt": "sekali",
    "trs": "terus",
    "krn": "karena",
    "yg": "yang",
    "sm": "sama",
    "blm": "belum",
    "bsk": "besok",
    "pls": "tolong",
    "btw": "omong-omong",
    "wkwk": "wkwk"
}

import csv

# Nama file CSV yang akan dibuat
filename = "alay_dict.csv"

# Tulis dictionary ke file CSV
with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Tulis header
    writer.writerow(["alay", "formal"])
    # Tulis isi kamus
    for key, value in alay_dict.items():
        writer.writerow([key, value])

print(f"File '{filename}' berhasil dibuat di folder saat ini.")
