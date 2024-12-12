import time
kitap,defter,kalem = 0,0,0

while(True):
    print("""\033[033m
            ---ANA MENÜ---
            [0] - ÇIKIŞ YAP
            [1] - ÜRÜNLERE GİT
    \033[0m""")
    
    secim1 = input("\033[034msecim1: \033[0m")
    if(secim1=="0"):
        print("\033[032msistemden cikis yapiliyor",end='')
        for i in range(3):
            print(".",end='',flush=True)
            time.sleep(1)
        print("\033[0m")    
        break
        
    elif(secim1=="1"):
        while(True):
            print("""\033[033m
            ---ÜRÜNLER---
            [1] - KALEM EKLE
            [2] - KİTAP EKLE
            [3] - DEFTER EKLE
                
            [4] - SEPETİ GİT
            [5] - ANA MENÜYE GEL
            \033[0m""")
            
            secim2 = input("\033[034msecim2: \033[0m")
            if(secim2=="1"):
                kalem +=1
                print("\033[032mkalem eklendi..\033[0m")
            elif(secim2=="2"):
                kitap +=1
                print("\033[032mkitap eklendi..\033[0m")
            elif(secim2=="3"):
                defter +=1
                print("\033[032mdefter eklendi..\033[0m")
            elif(secim2=="4"):
                
                while(True):
                    print("""\033[033m
            ---SEPETTEKİ ÜRÜNLER---
            KALEM SAYISI = \033[0m{}\033[033m
            KİTAP SAYISI = \033[0m{}\033[033m
            DEFTER SAYISI = \033[0m{}
                    """.format(kalem,kitap,defter))
                    
                    print("""\033[033m
            ---ÜRÜN KALDIR..?---
            [1] - EVET
            [2] - HAYIR
                    \033[0m""")
                    
                    secim3 = input("\033[034msecim3: \033[0m")
                    if(secim3=="1"): 
                        
                        print("""\033[033m
            ---ÜRÜN..?---
            [1] - KALEM
            [2] - KİTAP
            [3] - DEFTER
                        \033[0m""")
                        
                        secim4 = input("\033[034msecim4: \033[0m")
                        if(secim4=="1"):
                            if(kalem > 0):
                                print("\033[032mkalem kaldırıldı..\033[0m")
                                kalem -=1
                            else:
                                print("\033[031msepette kalem yok.\033[0m")
                        elif(secim4=="2"):
                            if(kitap > 0):
                                print("\033[032mkitap kaldırıldı..\033[0m")
                                kitap -=1
                            else:
                                print("\033[031msepette kitap yok.\033[0m")     
                        elif(secim4=="3"):
                            if(defter > 0):
                                print("\033[032mdefter kaldırıldı..\033[0m")
                                defter -=1
                            else:
                                print("\033[031msepette defter yok.\033[0m")
                        else:
                            print("\033[031myanlis secim yaptiniz..\033[0m")
                            
                    elif(secim3=="2"):
                        break
                    else:
                        print("\033[031myanlis secim yaptiniz..\033[0m")
                        
            elif(secim2=="5"):
                break
            else:
                print("\033[031myanlis secim yaptiniz..\033[0m")
    else:
        print("\033[031myanlis secim yaptiniz..\033[0m")