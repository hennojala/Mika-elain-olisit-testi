# Tämän Ohjelmoinnin perusteet TTC2030 -kurssin harjoitustyön osan on tehnyt Henna Ojala.

# Tämä on oheissivu Harjoitustyölle "Mikä_eläin_olisit_testi", tämän tiedot viedään pääsivulle.
# Tuodaan Eläinlistat sivulta listat kasvinsyöjät ja lihansyöjät, sekä Muuttujat sivun sisältö käyttöön.
from Eläinlistat import kasvinsyöjät
from Eläinlistat import lihansyöjät
from Muuttujat import *

# Luon testin funktioon, jotta sen sijoittaminen koodikokonaisuuteen on helpompaa ja siistimpää.
def elain_testi():
    
    # Testi alkaa tulostamalla käyttäjälle ohjeita testin suorituksesta.
    print("Selvitetään mikä eläin olisit! Vastaa kirjoittamalla vastauskenttään a, b tai c vastausvaihtoehdoista riippuen.")
    
    # Toistorakenne mahdollistaa testin jatkuvuuden, kunnes sen halutaan päättyvän.
    while True:
        # Koko testin ajan inputeissa käytetään string -muotoa, koska kyse on merkkijonoista.
        # Luodaan muuttuja aloitus, jossa valmistellaan käyttäjää testiin kysymällä valmiutta testiin.
        aloitus = str(input("Oletko valmis, aloitetaanko? a) kyllä b) ei "))
        
        # Estetään bugeja tulostamalla ohjeita käyttäjälle vastauksen ollessa muu kuin vaihtoehdoissa. Continue palauttaa toiston alkuun.
        # Tätä käytetään koko testin ajan jokaisen uuden inputin kohdalla.        
        if aloitus != "a" and aloitus != "b":
            print(vaarin_ab)
            continue
        
        # Kieltävällä vastauksella tulostetaan käyttäjälle "kuittaus", eli jos vastaus on muuta kuin a tai b.
        elif aloitus == "b":
            print("Selvä, voit tehdä testin myöhemminkin!")
            break

        # Myöntävällä vastauksella aloitetaan varsinainen testi ensimmäisellä kysymyksellä ja aletaan toteuttamaan ehtokaavaa, joka toistuu läpi testin, jokaisen kysymyksen kohdalla.
        elif aloitus == "a":

            syoja = str(input("Söisitkö a) kasviperäistä vai b) eläinperäistä ravintoa? "))

            if syoja != "a" and syoja != "b":
                print(vaarin_ab)
                continue

            koko = str(input("Olisitko a) pieni b) keskikokoinen vai c) suuri eläin? "))

            if koko != "a" and koko != "b" and koko != "c":
                print(vaarin_abc)
                continue

            vesi = str(input("Viihdytkö vedessä? a) kyllä b) en "))

            if vesi != "a" and vesi != "b":
                print(vaarin_ab)
                continue
            
            # Vastauksen ollessa myönteinen, tulos vielä on riippuvainen aiemmista kysymyksistä.
            elif syoja == "a":

                # Ehtojen perusteella tulostetaan oikea vastaus. Ensimmäinen vastaus voi siis tulla aloitus+kolmen kategoriakysymyksen jälkeen.
                if koko == "a" and vesi == "a":
                    # Kyseisten ehtojen täyttyessä tulostetaan vastaus.
                    # Tämä toistuu samalla kaavalla koodin loppuun saakka.
                    print(t, p_ks_vesi)
                    # Ja lopetetaan silmukka. 
                    # Tämä toistuu myös samalla kaavalla koodin loppuun saakka.
                    break

                elif koko == "b" and vesi == "a":
                    print(t, kk_ks_vesi)
                    break

                elif koko == "c" and vesi == "a":
                    print(t, s_ks_vesi)
                    break

            elif syoja == "b":

                if koko == "a" and vesi == "a":
                    print(t, p_ls_vesi)
                    break

                elif koko == "b" and vesi == "a":
                    print(t, kk_ls_vesi)
                    break

                elif koko == "c" and vesi == "a":
                    print(t, s_ls_vesi)
                    break

            lemmikki = str(input("Voisiko sinua pitää lemmikkinä? a) kyllä b) ei "))

            if lemmikki != "a" and lemmikki != "b":
                print(vaarin_ab)
                continue

            elif lemmikki == "a":

                if syoja == "a":

                    if koko == "a":
                        print(t, p_ks_lemmikki)
                        break

                    elif koko == "b":
                        print(t, kk_ks_lemmikki)
                        break
                    
                    elif koko == "c":
                        print(t, s_ks_lemmikki)
                        break

                if syoja == "b":

                    if koko == "a":
                        print(t, p_ls_lemmikki)
                        break

                    elif koko == "b":
                        print(t, kk_ls_lemmikki)
                        break
                        
                    elif koko == "c":
                        print(t, s_ls_lemmikki)
                        break

            siivet = str(input("Olisiko sinulla siivet? a) kyllä b) ei "))

            if siivet != "a" and siivet != "b":
                print(vaarin_ab)
                continue
                
            elif siivet == "a":

                if syoja == "a":

                    if koko == "a":
                        print(t, p_ks_siivet)
                        break

                    if koko == "b":
                        print(t, kk_ks_siivet)
                        break
                    
                    elif koko == "c":
                        print(t, s_ks_siivet)
                        break

                if syoja == "b":

                    if koko == "a":
                        print(t, p_ls_siivet)
                        break

                    elif koko == "b":
                        print(t, kk_ls_siivet)
                        break
                    
                    elif koko == "c":
                        print(t, s_ls_siivet)
                        break


            suomi = str(input("Eläisitkö Suomen luonnossa? a) kyllä b) en "))

            if suomi != "a" and suomi != "b":
                print(vaarin_ab)
                continue
            
            elif syoja == "a":

                if suomi == "a":
                    if koko == "a":
                        print(t, p_ks_suomi)
                        break
                    elif koko == "b":
                        print(t, kk_ks_suomi)
                        break
                    elif koko == "c":
                        print(t, s_ks_suomi)
                        break

                if suomi == "b":
                    if koko == "a":
                        print(t, p_ks_muualla)
                        break
                    elif koko == "b":
                        print(t, kk_ks_muualla)
                        break
                    elif koko == "c":
                        print(t, s_ks_muualla)
                        break

            elif syoja == "b":
 
                if suomi == "a":
                    if koko == "a":
                        print(t, p_ls_suomi)
                        break
                    elif koko == "b":
                        print(t, kk_ls_suomi)
                        break
                    elif koko == "c":
                        print(t, s_ls_suomi)
                        break

                if suomi == "b":
                    if koko == "a":
                        print(t, p_ls_muualla)
                        break
                    elif koko == "b":
                        print(t, kk_ls_muualla)
                        break
                    elif koko == "c":
                        print(t, s_ls_muualla)
                        break
                    
    # Tulostetaan lopputeksti.
    print(loppu)                    