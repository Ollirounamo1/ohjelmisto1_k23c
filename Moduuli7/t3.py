toiminto = input('uusi / haku / enter = lopeta:')

airports = {}

airports['EFHK'] = 'Helsinki vantaa'
airports['EFVA'] = 'Vaasan lentokenttä'

print(airports['EFVA'])
#toista jos toiminto ei ole ''
    #Jos toiminto on uusi
        #Kysy icao
        #kysy nimi
        #lisää kenttä airports sanakirjaan
    #jos toiminto on haku
        #kysy icao
        #tulosta airports sanakirjasto alkio icao
    #kysy toiminto