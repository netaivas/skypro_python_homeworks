from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "N13", "79998875541"),
    Smartphone("OnePlus", "15K", "79024567895"),
    Smartphone("Google", "Pixel 5", "79023568965"),
    Smartphone("Apple", "Iphone 14", "79184578965"),
    Smartphone("Xiaomi", "Mi 16", "79256369875")
    ]

for smartphone in catalog:
    print(smartphone.brand, "-",
          smartphone.model + ".", "+" + smartphone.phone_number)