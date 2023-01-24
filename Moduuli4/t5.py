kayttaja = input('Anna käyttäjätunnus ')
salasana = input('Anna salasana ')

if kayttaja == 'python' or salasana == 'rules':
    tulos = 'Tervetuloa'

    print(tulos)

else: tulos = 'Pääsy evätty'

    print(tulos)