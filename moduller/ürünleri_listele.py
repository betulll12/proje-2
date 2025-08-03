def ürünlerilistelemenu():
    DOSYA_ADI = "stok.txt"
    if not os.path.exists(DOSYA_ADI):
        print("Henüz ürün yok.\n")
        return
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        print("\n--- ÜRÜNLER ---")
        for i, satir in enumerate(f, 1):
            ad, adet, fiyat = satir.strip().split(",")
            print(f"{i}. Ürün: {ad} | Adet: {adet} | Fiyat: {fiyat}₺")
        print()
