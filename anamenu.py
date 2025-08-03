def anamenu():
    print ("anamenu")

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║STOK TAKİP PROGRAMI  ║")
    print("║                     ║")
    print("║  1-Ürün ekle        ║")
    print("║  2-Ürünleri listele ║")
    print("║  3-Ürünleri ara     ║")
    print("║  4-Ürünleri sil     ║")
    print("║  5-Ürünleri güncelle║")
    print("║  6-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")


    secim = input("Seçiminizi yapınız (1-6):")
    if secim=="1":
        import moduller.ürün_ekle
        moduller.ürün_ekle.ürüneklemenu()  
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
        print("Çıkış")
        exit()

    else:
     print("Geçersiz seçim! Lütfen tekrar deneyin.")    

anamenu()
    
    