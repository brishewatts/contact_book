class Kontakt():
    def __init__(self, first_name, last_name, email, phone, address):
        self.ime = first_name
        self.priimek = last_name
        self.elenaslov = email
        self.telefon = phone
        self.naslov = address

    def polno_ime(self):
        polno_ime = (self.ime,  self.priimek)
        return polno_ime


    def vsi_podatki(self):
        vsi_podatki = (self.ime, self.priimek, self.elenaslov, self.telefon, self.naslov)
        return vsi_podatki

beleznica_kontaktov = []

da = True

while da:
    odgovor = raw_input("Zelis dodati nov kontakt? da ali ne: ")

    if odgovor == "da":
        ime = raw_input("Vpisi ime: ")
        priimek = raw_input("Vpisi priime: ")
        elenaslov = raw_input("Vpisi email: ")
        telefon = raw_input("Vpisi phone: ")
        naslov = raw_input("Vpisi naslov: ")
        oseba = Kontakt(first_name=ime, last_name=priimek, email=elenaslov, phone=telefon, address=naslov)

        beleznica_kontaktov.append(oseba)

    if odgovor == "ne":
        break

for oseba in beleznica_kontaktov:
    print oseba.ime
    print oseba.priimek
    print oseba.vsi_podatki()
