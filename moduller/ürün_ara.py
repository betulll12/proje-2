def ürünleriaramenu():
  DOSYA_ADI = "stok.txt"

    aranan = input("Aranacak ürün adı: ").lower()
    bulundu = False
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        for satir in f:
            ad, adet, fiyat = satir.strip().split(",")
            if aranan in ad.lower():
                print(f"Ürün: {ad} | Adet: {adet} | Fiyat: {fiyat}₺")
                bulundu = True
    if not bulundu:
        print("Ürün bulunamadı.\n")
