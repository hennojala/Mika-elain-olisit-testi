# Tämän Ohjelmoinnin perusteet TTC2030 -kurssin harjoitustyön osan on tehnyt Henna Ojala.
# Tämä on oheissivu Harjoitustyölle "Mikä_eläin_olisit_testi", tämän tiedot viedään pääsivulle.

# Tuodaan Eläinlistat sivulta listat eläimistä muuttujien luontia varten.

from Eläinlistat import kasvinsyöjät
from Eläinlistat import lihansyöjät


# MUUTTUJAT:

# Kategorioin eläimet koon mukaan muuttujiin, jotta koodi olisi myöhemmin helppokäyttöistä. 
pienet_ks = kasvinsyöjät[0:5]
keskik_ks = kasvinsyöjät[5:10]
suuret_ks = kasvinsyöjät[10:15]


# Kategorioin eläimet koon mukaan muuttujiin, jotta koodi olisi myöhemmin helppokäyttöistä. Haen tiedot listasta indekseillä.
pienet_ls = lihansyöjät[0:5]
keskik_ls = lihansyöjät[5:10]
suuret_ls = lihansyöjät[10:15]

# Yksilöin jokaiselle eläimelle oman muuttujan koon, ravinnon ja kysymyksen aiheen mukaan, jotta itse testin koodaus olisi sujuvaa.
# Listalta poimin oikean alkion jokaiselle muuttujalle indeksin perusteella käyttäen apuna luomaani Word-tekstitiedostoa. Jos listan eläimiä haluaa muuttaa, riittää vain listan eläimen nimen vaihto ilman että tarvitsee muuttaa muuta koodia. Täytyy vain huomioida että kategoriat täsmää.
# p = pieni, kk = keskikokoinen, s = suuri, sekä ks = kasvinsyöjä ja ls = lihansyöjä. Tiedän heti ulkoa kysymyksien vastauksia koodatessa mikä muuttuja täytyy laittaa mihinkin, jotta eläin varmasti täsmää kysymyksen kanssa.

p_ks_vesi = pienet_ks[3]
kk_ks_vesi = keskik_ks[4]
s_ks_vesi = suuret_ks[1]

p_ls_vesi = pienet_ls[4]
kk_ls_vesi = keskik_ls[3]
s_ls_vesi = suuret_ls[0]

p_ks_siivet = pienet_ks[2]
kk_ks_siivet = keskik_ks[2]
s_ks_siivet = suuret_ks[4]

p_ls_siivet = pienet_ls[2]
kk_ls_siivet = keskik_ls[4]
s_ls_siivet = suuret_ls[4]

p_ks_suomi = pienet_ks[1]
kk_ks_suomi = keskik_ks[0]
s_ks_suomi = suuret_ks[2]

p_ls_suomi = pienet_ls[0]
kk_ls_suomi = keskik_ls[1]
s_ls_suomi = suuret_ls[1]

p_ks_muualla = pienet_ks[4]
kk_ks_muualla = keskik_ks[3]
s_ks_muualla = suuret_ks[0]

p_ls_muualla = pienet_ls[3]
kk_ls_muualla = keskik_ls[2]
s_ls_muualla = suuret_ls[2]

p_ks_lemmikki = pienet_ks[0]
kk_ks_lemmikki = keskik_ks[1]
s_ks_lemmikki = suuret_ks[3]

p_ls_lemmikki = pienet_ls[1]
kk_ls_lemmikki = keskik_ls[0]
s_ls_lemmikki = suuret_ls[3]


# Luon muuttujat, joita käytetään estämästä bugeja, jos käyttäjä asettaa vastauksen vaihtoehtojen ulkopuolelle.
vaarin_ab = "Yritä uudelleen, vastataksesi tähän kysymykseen sinun on kirjoitettava a tai b."
vaarin_abc = "Yritä uudelleen, vastataksesi tähän kysymykseen sinun on kirjoitettava a, b tai c."
# Luon lisäksi muuttujan, jonka teksti tulostetaan testin päätyttyä.
loppu = ("Kiitos vastauksista, toivottavasti sinulla oli hauskaa!")
# Luon muuttujan lyhenne sanasta tulos, joka tulostaa alun vastauksen tulostukseen, jotta sitä ei tarvitse kirjoittaa aina uudelleen.
t = "Olisit:"