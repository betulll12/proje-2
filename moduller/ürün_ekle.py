def ürünlerieklemenu():
  DOSYA_ADI = "stok.txt"
  ad = input("Ürün adı: ")
  adet = input("Adet: ")
  fiyat = input("Fiyat:")
  with open(DOSYA_ADI, "a", encoding="utf-8") as f:
        f.write(f"{ad},{adet},{fiyat}\n")
  print("✅ Ürün eklendi!\n")
  print(f"ürün adı: {ad}")
 