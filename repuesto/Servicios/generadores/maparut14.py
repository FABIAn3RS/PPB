import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas para hacer la línea de la ruta (Si quieres ver los puntos en el mapa quita el "#" al final del primer for)
paradas = [
    (-0.956938, -80.765765), #1
    (-0.959060, -80.758438), #2
    (-0.958411, -80.758006), #3 
    (-0.957846, -80.748158), #4
    (-0.957664, -80.747308), #5
    (-0.955636, -80.743957), #6
    (-0.955345, -80.742024), #7
    (-0.954780, -80.742032), #8
    (-0.954115, -80.740951), #9
    (-0.951951, -80.737425), #10
    (-0.950001, -80.734321), #11
    (-0.951072, -80.733508), #12
    (-0.949405, -80.731403), #13
    (-0.950754, -80.730330), #14
    (-0.949245, -80.728205), #15
    (-0.948516, -80.727178), #16
    (-0.945532, -80.729597), #17 
    (-0.945298, -80.730043), #18
    (-0.944869, -80.731983), #19
    (-0.944790, -80.733696), #20
    (-0.944617, -80.733691), #21   
    (-0.943123, -80.733445), #22
    (-0.941934, -80.733257), #23
    (-0.941690, -80.731073), #24
    (-0.941595, -80.729896), #25
    (-0.948293, -80.721130), #26
    (-0.946677, -80.721589), #27
    (-0.950521, -80.720594), #28
    (-0.951148, -80.720017), #29
    (-0.955038, -80.716709), #30
    (-0.959721, -80.713402), #31 
    (-0.961048, -80.711245), #32 
    (-0.973094, -80.701300), #33
    (-0.994639, -80.690754), #34 
    (-0.993652, -80.688543), #35
] 

# Coordenadas de las paradas (Se muestran los puntos en el mapa)
marcadores_individuales = [
    (-0.957592, -80.763628),
    (-0.958691, -80.760043),
    (-0.957529, -80.756058),
    (-0.957398, -80.752181),
    (-0.957810, -80.748519),
    (-0.956406, -80.745475),
    (-0.955535, -80.742729),
    (-0.954422, -80.741428),
    (-0.952137, -80.737767),
    (-0.950298, -80.732566),
    (-0.946876, -80.728529),
    (-0.945484, -80.729606),
    (-0.944186, -80.733611),
    (-0.941673, -80.730643),
    (-0.942698, -80.725782),
    (-0.944021, -80.723823),
    (-0.946279, -80.721937),
    (-0.956258, -80.715846),
    (-0.959178, -80.713789),
    (-0.961307, -80.710754),
    (-0.962540, -80.709646),
    (-0.964307, -80.708259),
    (-0.967962, -80.705396),
    (-0.970343, -80.703509),
    (-0.972939, -80.701434),
    (-0.974213, -80.700426),
    (-0.978390, -80.697861),
    (-0.981219, -80.696715),
    (-0.983785, -80.695684),
    (-0.987031, -80.694397),
    (-0.991628, -80.692335),
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
    folium.Marker(punto, popup=f"Parada {idx}", icon=folium.Icon(color='red')).add_to(mapa)

# Guardar y abrir
mapa.save("mapar14.html")
webbrowser.open("LINEA14.html")
