# Tämän Ohjelmoinnin perusteet TTC2030 -kurssin harjoitustyön on tehnyt Henna Ojala.
# PÄÄSIVU

# Tulostetaan päivämäärä ja aika.
from datetime import datetime
print(datetime.now())

# *********************************
# Harjoitustyöni idea:

# Tein testin, jossa testataan mikä eläin olisit.
# Käyttäjä vastaa kysymyksiin, joiden vastausten perusteella testi etenee ja antaa käyttäjälle vastauksen.
# Testin kesto ja kysymysten määrä riippuu käyttäjän vastauksista.

# *********************************
# Pohdintoja harjoitustyöstä:

# Syy työni aiheelle on, että ihmiset tykkäävät suorittaa erilaisia "leikkimielisiä" testejä ja niitä tuleekin jatkuvasti medioissa vastaan. Törmäsin tällaiseen eri aihetta koskevaan testiin somessa ja mielenkiintoni heräsi lähteä toteuttamaan omaa testiä.
# Ajattelin, että kurssin tasoon ja aiheisiin nähden tämä voisi olla sopiva työ. Harjoitustyössä pääsin soveltamaan oppimaani.
# Eläinaihe on minulle sydäntä lähellä aijemman ammattini ja harrastuneisuuden vuoksi, joten käyttämäni tiedot syntyivät päästäni kuin itsestään.
# Tein ensin paperille raakaversion koodista, tehtävän rungosta, sekä mietin eläinlajit ja aihealueet kysymyksille.
# Tämän jälkeen siirsin paperiverison tiedot koneelle tekstinkäsittelyohjelmalle, jossa yksinkertaistin rakennetta ja taulukoin koodiin tulevat tiedot.
# Kerron koodin aikana kommentteja harjoitustyö -näkökulmasta, eli selitän poikkeuksellisen perusteellisesti tekemääni.

# *********************************

# Tuodaan funktio, joka toteuttaa testin ja kutsutaan funktio. 
# Testi alkaa pyörimään konsolissa, ole hyvä!


from Testifunktio import elain_testi

elain_testi()

