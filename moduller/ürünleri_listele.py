import os

def ürünlerilistelemenu():
    DOSYA_ADI = "stok.txt"

    if not os.path.exists(DOSYA_ADI):
        print("Henüz ürün yok.\n")
        return

    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    if not satirlar:
        print("Henüz ürün yok.\n")
        return

    print("\n--- ÜRÜNLER ---")
    for i, satir in enumerate(satirlar, 1):
        satir = satir.strip()
        if not satir or "," not in satir:
            continue
        try:
            ad, adet, fiyat = satir.split(",")
            print(f"{i}. Ürün: {ad} | Adet: {adet} | Fiyat: {fiyat}₺")
        except ValueError:
            # Hatalı formatlı satır varsa atla
            continue
    print()
