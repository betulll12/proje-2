def anamenu():
    print ("anamenu")
    print("\033[1;32;40m")
    print("╔═════════════════════╗")
    print("║STOK TAKİP PROGRAMI  ║")
    print("║                     ║")
    print("║  1-Ürün ekle        ║")
    print("║  2-Ürünleri listele ║")
    print("║  3-Ürünleri ara     ║")
    print("║  4-Ürünleri sil     ║")
    print("║  5-Ürünleri güncelle║")
    print("║  6-Stok kontrol     ║")
    print("║  7-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")


    secim = input("Seçiminizi girin (1-7): ")
    if secim=="1":
        import moduller.ürün_ekle
        moduller.ürün_ekle.ürünlerieklemenu()  
    if secim=="2":
        import moduller.ürünleri_listele
        moduller.ürünleri_listele.ürünlerilistelemenu()  
    if secim == "3":
        import moduller.ürün_ara
        moduller.ürün_ara.ürünleriaramenu()
    if secim == "4":
        import moduller.ürün_sil
        moduller.ürün_sil.ürünlerisilmenu()
    if secim == "5":
        import moduller.ürün_güncelle
        moduller.ürün_güncelle.ürünlerigüncellemenu()
    if secim == "6":
        import moduller.kontrol_stok
        moduller.kontrol_stok.stokkontrolmenu()    
    if secim == "7":
        print("Çıkış")
        exit()

    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")    

anamenu()
    
    