import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas para hacer la línea de la ruta (Si quieres ver los puntos en el mapa quita el "#" al final del primer for)
paradas = [
    (-0.971595, -80.642485), #1
    (-0.959585, -80.680928

), #2
    (-0.957752, -80.698086

), #3
    (-0.951253, -80.700520), #4
    (-0.952294, -80.710145), #5
    (-0.951122, -80.710397

), #6
    (-0.951912, -80.716826

), #7
    (-0.953771, -80.717496

), #8
    (-0.952147, -80.721638

), #9
    (-0.950756, -80.720694

), #10
    (-0.944821, -80.722606

), #11
    (-0.942476, -80.725994

), #12
    (-0.944750, -80.727588

), #13
    (-0.944970, -80.727371

), #14
    (-0.946399, -80.728908

), #15
    (-0.949312, -80.726513

), #16
    (-0.951792, -80.729544

), #17
    (-0.953354, -80.728370), #18
    (-0.955304, -80.730857

), #19
    (-0.953030, -80.732067

), #20
    (-0.957576, -80.747195

), #21

]

# Coordenadas de las paradas (Se muestran los puntos en el mapa)
marcadores_individuales = [
    
    (-0.971595, -80.642485),
    (-0.971203, -80.645707),
    (-0.970695, -80.649250),
    (-0.971135, -80.653195),
    (-0.970300, -80.656359),
    (-0.968836, -80.659772),
    (-0.967334, -80.663148),
    (-0.965840, -80.666502),
    (-0.964479, -80.669669),
    (-0.963080, -80.672910),
    (-0.961610, -80.676207),
    (-0.960124, -80.679388),
    (-0.959995, -80.682763),
    (-0.960515, -80.686319),
    (-0.961095, -80.689779),
    (-0.960301, -80.693170),
    (-0.958509, -80.696453),
    (-0.956841, -80.699666),
    (-0.953182, -80.700179),
    (-0.951376, -80.702031),
    (-0.951789, -80.705240),
    (-0.952139, -80.708837),
    (-0.951380, -80.711606),
    (-0.951824, -80.715016),
    (-0.953295, -80.717285),
    (-0.952594, -80.720293),
    (-0.950045, -80.720960),
    (-0.946624, -80.721385),
    (-0.943698, -80.723853),
    (-0.942966, -80.726421),
    (-0.945788, -80.728340),
    (-0.948571, -80.727043),
    (-0.951003, -80.728492),
    (-0.953544, -80.728515),
    (-0.954545, -80.731155),
    (-0.953720, -80.733618),
    (-0.955400, -80.736787),
    (-0.955082, -80.740324),
    (-0.955440, -80.744266)

]

# Descargar red de calles
G = ox.graph_from_point(paradas[0], dist=20000, network_type='drive', simplify=False)
G = G.to_undirected()

# Crear el mapa
mapa = folium.Map(location=paradas[0], zoom_start=14)

# Dibujar líneas entre paradas sin mostrar marcadores
for i in range(len(paradas) - 1):
    nodo_origen = ox.distance.nearest_nodes(G, paradas[i][1], paradas[i][0])
    nodo_destino = ox.distance.nearest_nodes(G, paradas[i + 1][1], paradas[i + 1][0])
    
    if nx.has_path(G, nodo_origen, nodo_destino):
        ruta = nx.shortest_path(G, nodo_origen, nodo_destino, weight='length')
        coordenadas_ruta = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
        folium.PolyLine(coordenadas_ruta, color='blue', weight=5).add_to(mapa)
    else:
        print(f"❌ No hay ruta entre Parada {i+1} y Parada {i+2}")

    #folium.Marker(paradas[i], popup=f"Parada {i+1}").add_to(mapa)

# Agregar marcadores individuales (sin conexión)
for idx, punto in enumerate(marcadores_individuales, start=1):
    folium.Marker(punto, popup=f"Parada {idx}",icon=folium.Icon(color='red')).add_to(mapa)

# Guardar y abrir
mapa.save("mapar2.html")
webbrowser.open("mapar2.html")