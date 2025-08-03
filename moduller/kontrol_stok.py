def stokkontrolmenu():
    DOSYA_ADI = "stok.txt"
    if not os.path.exists(DOSYA_ADI):
        return
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        for satir in f:
            ad, adet, fiyat = satir.strip().split(",")
            try:
                if int(adet) < 5:
                    print(f"⚠️  Dikkat! '{ad}' ürününün stoğu azaldı ({adet} adet kaldı).")
            except ValueError:
                pass
