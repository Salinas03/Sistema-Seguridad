import geocoder

g = geocoder.ip('me')

myaddress = g.latlng

if myaddress:
    latitude = myaddress[0]
    longitude = myaddress[1]

    print(f'Latitud: {latitude}')
    print(f'Longitud: {longitude}')
else:
    print('No se pudo obtener la ubicación.')