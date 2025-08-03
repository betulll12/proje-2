import os

# Bu değişkeni fonksiyonun dışına alıyoruz
DOSYA_ADI = "stok.txt"

def stokkontrolmenu():
    if not os.path.exists(DOSYA_ADI):
        return

    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    uyarı_sayisi = 0

    for satir in satirlar:
        satir = satir.strip()
        if not satir or "," not in satir:
            continue
        try:
            ad, adet, fiyat = satir.split(",")
            adet = int(adet.strip())
            if adet < 5:
                print(f"⚠️  Dikkat! '{ad}' ürününün stoğu azaldı ({adet} adet kaldı).")
                uyarı_sayisi += 1
        except (ValueError, IndexError):
            continue

    if uyarı_sayisi == 0:
        print("✅ Tüm ürünlerin stoğu yeterli seviyede.\n")

