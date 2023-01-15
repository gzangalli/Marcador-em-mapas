import folium

# Coordenadas para o centro do mapa
latitude = -30.0654
longitude = -51.2358

# Criando o mapa
map = folium.Map(location=[latitude, longitude], zoom_start=13)

# Adicionando um marcador
folium.Marker(
    location=[latitude, longitude],
    popup="Este é um marcador no estádio Beira-Rio",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(map)

# Exibindo o mapa
map.save("beira-rio.html")
