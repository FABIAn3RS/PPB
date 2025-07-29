import osmnx as ox 
import networkx as nx
import folium
import webbrowser

# Coordenadas de las paradas
paradas = [
    (-0.989219, -80.701576), #1
    (-0.988406, -80.707313), #2
    (-0.984884, -80.710893), #3
    (-0.980976, -80.710852), #4
    (-0.977894, -80.709262), #5
    (-0.973090, -80.712351), #6
    (-0.967752, -80.716272), #7
    (-0.969976, -80.719981), #8
    (-0.966910, -80.723704), #9
    (-0.963898, -80.724841), #10
    (-0.961193, -80.726845), #11
    (-0.957227, -80.728759), #12
    (-0.952769, -80.721863), #13
    (-0.950466, -80.720242), #14
    (-0.946152, -80.721608), #15
    (-0.943077, -80.724884), #16
    (-0.941140, -80.727776), #17
    (-0.941558, -80.730632), #18
    (-0.941944, -80.733395), #19
    (-0.944417, -80.733766), #20
    (-0.945222, -80.737244), #21
    (-0.950102, -80.741825), #22
    (-0.955544, -80.744379), #23
    (-0.957743, -80.748280), #24
    (-0.957136, -80.755183), #25
    (-0.958466, -80.759963), #26
    (-0.957008, -80.764967), #27
]

# Marcadores individuales
marcadores_individuales = [
    (-0.954112, -80.724404),
    (-0.952769, -80.721863),
    (-0.946152, -80.721608),
    (-0.941604, -80.731356),
    (-0.943474, -80.733628),
    (-0.946795, -80.738709),
    (-0.952923, -80.743341),
    (-0.956930, -80.746429),
    (-0.957080, -80.764496),
    (-0.956543, -80.727999),
    (-0.958113, -80.757367),
    (-0.958611, -80.728145),
    (-0.960885, -80.726951),
    (-0.962000, -80.726647),
    (-0.967357, -80.723361),
    (-0.969882, -80.720308),
    (-0.968226, -80.717153),
    (-0.968996, -80.715110),
    (-0.971380, -80.713447),
    (-0.973773, -80.711878),
    (-0.978331, -80.709324),
    (-0.980432, -80.710699),
    (-0.984865, -80.710917),
    (-0.987646, -80.708691),
    (-0.990149, -80.704313),
]

# Descargar red de calles
G = ox.graph_from_point(paradas[0], dist=20000, network_type='drive', simplify=False)
G = G.to_undirected()

# Crear el mapa
mapa = folium.Map(location=paradas[0], zoom_start=14)

for i in range(len(paradas) - 1):
    if i == len(paradas) - 2:  # es decir, tramo 26 → 27
        continue  # lo manejaremos manualmente después

    nodo_origen = ox.distance.nearest_nodes(G, paradas[i][1], paradas[i][0])
    nodo_destino = ox.distance.nearest_nodes(G, paradas[i + 1][1], paradas[i + 1][0])
    
    if nx.has_path(G, nodo_origen, nodo_destino):
        ruta = nx.shortest_path(G, nodo_origen, nodo_destino, weight='length')
        coordenadas_ruta = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
        folium.PolyLine(coordenadas_ruta, color='blue', weight=5).add_to(mapa)
    else:
        print(f"❌ No hay ruta entre Parada {i+1} y Parada {i+2}")
        
# Línea recta entre Parada 26 → Parada 27
folium.PolyLine([paradas[-2], paradas[-1]], color='blue', weight=5).add_to(mapa)

# Marcar la última parada
folium.Marker(paradas[-1], popup=f"Parada {len(paradas)}").add_to(mapa)

# Marcadores individuales rojos
for idx, punto in enumerate(marcadores_individuales, start=1):
    folium.Marker(punto, popup=f"Parada {idx}", icon=folium.Icon(color='red')).add_to(mapa)

# Guardar y abrir el mapa
mapa.save("mapar16.html")
webbrowser.open("mapar16.html")
