def ürünlerisilmenu():
    DOSYA_ADI = "stok.txt"
    urun_adi = input("Silinecek ürün adı: ").lower()
    silindi = False
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        satirlar = f.readlines()
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        for satir in satirlar:
            ad, _, _ = satir.strip().split(",")
            if urun_adi != ad.lower():
                f.write(satir)
            else:
                silindi = True
    if silindi:
        print("✅ Ürün silindi.\n")
    else:
        print("Ürün bulunamadı.\n")
