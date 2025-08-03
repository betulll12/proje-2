def ürünlerigüncellemenu():
DOSYA_ADI = "stok.txt"
    urun_adi = input("Güncellenecek ürün adı: ").lower()
    guncellendi = False
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        satirlar = f.readlines()
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        for satir in satirlar:
            ad, adet, fiyat = satir.strip().split(",")
            if urun_adi == ad.lower():
                print(f"Mevcut bilgi -> Ad: {ad} | Adet: {adet} | Fiyat: {fiyat}")
                yeni_ad = input("Yeni ürün adı: ")
                yeni_adet = input("Yeni adet: ")
                yeni_fiyat = input("Yeni fiyat: ")
                f.write(f"{yeni_ad},{yeni_adet},{yeni_fiyat}\n")
                guncellendi = True
            else:
                f.write(satir)
    if guncellendi:
        print("✅ Ürün güncellendi.\n")
    else:
        print("Ürün bulunamadı.\n")
