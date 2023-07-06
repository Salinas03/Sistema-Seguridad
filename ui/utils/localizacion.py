import geocoder
import folium

class Location:
    ip = '177.249.10.8'
    g = geocoder.ip(ip)

    myAddress = g.latlng
    print(myAddress)
        
    if myAddress is not None:
        my_napi = folium.Map(location=myAddress,zoom_start=12)

        folium.CircleMarker(location=myAddress,radius=50, popup="Equipo de computo").add_to(my_napi)

        folium.Marker(myAddress,popup="Equipo de computo").add_to(my_napi)
        my_napi.save("ui/html/mapa.html")
        result = True
    else:
        result = False
    
    print(result)