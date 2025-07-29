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
    (-0.955796, -80.744454), #6
    (-0.955379, -80.744123), #7
    (-0.952198, -80.742908), #8
    (-0.949955, -80.741566), #9
    (-0.948549, -80.740010), #10
    (-0.945222, -80.737173), #11
    (-0.944781, -80.733925), #12
    (-0.944649, -80.733768), #13
    (-0.942083, -80.733305), #14 
    (-0.941798, -80.732697), #15 
    (-0.941661, -80.730756), #16
    (-0.941504, -80.728557), #17
    (-0.941567, -80.727718), #18 
    (-0.941722, -80.727201), #19
    (-0.943596, -80.724419), #20
    (-0.946196, -80.721868), #21
    (-0.948651, -80.721188), #22
    (-0.950482, -80.720874), #23
    (-0.950683, -80.720288), #24
    (-0.950565, -80.719882), #25
    (-0.950549, -80.718687), #26
    (-0.950672, -80.716904), #27
    (-0.950774, -80.715207), #28
    (-0.950974, -80.710858), #29
    (-0.951010, -80.710273), #30
    (-0.950855, -80.709630), #31
    (-0.950579, -80.707823), #32
    (-0.950041, -80.705439), #33
    (-0.949621, -80.704152), #34
    (-0.948480, -80.699803), #36
    (-0.948896, -80.697947), #37 
    (-0.949882, -80.696554), #38
    (-0.950710, -80.695406), #39 
    (-0.956493, -80.693190), #40
    (-0.958093, -80.690726), #41
    (-0.958677, -80.689881), #42 
]

# Coordenadas de las paradas (Se muestran los puntos en el mapa)
marcadores_individuales = [
    (-0.957592, -80.763628),
    (-0.958691, -80.760043),
    (-0.957529, -80.756058),
    (-0.957398, -80.752181),
    (-0.957810, -80.748519),
    (-0.956406, -80.745475),
    (-0.952852, -80.743208),
    (-0.950204, -80.741864),
    (-0.947776, -80.739326),
    (-0.945295, -80.737273),
    (-0.945072, -80.736096),
    (-0.944896, -80.734922),
    (-0.944195, -80.733628),
    (-0.941829, -80.732446),
    (-0.941526, -80.728761),
    (-0.943303, -80.724891),
    (-0.944405, -80.723332),
    (-0.946106, -80.722014),
    (-0.947433, -80.721431),
    (-0.950489, -80.719158),
    (-0.950766, -80.715448),
    (-0.950869, -80.712962),
    (-0.950824, -80.709303),
    (-0.950167, -80.705683),
    (-0.948661, -80.700785),
    (-0.950235, -80.696040),
    (-0.952900, -80.694119),
    (-0.954819, -80.693913),
    (-0.957175, -80.692584),
    (-0.958618, -80.690252),
]

# Descargar red de calles
G = ox.graph_from_point(paradas[0], dist=20000, network_type='drive', simplify=False)
G = G.to_undirected()

# Crear el mapa
mapa = folium.Map(location=paradas[0], zoom_start=14)

# Iterar sobre las paradas y calcular rutas consecutivas
for i in range(len(paradas) - 1):
    # Encontrar los nodos más cercanos a las paradas
    nodo_origen = ox.distance.nearest_nodes(G, paradas[i][1], paradas[i][0])
    nodo_destino = ox.distance.nearest_nodes(G, paradas[i + 1][1], paradas[i + 1][0])
    
    # Calcular la ruta más corta (en distancia)
    ruta = nx.shortest_path(G, nodo_origen, nodo_destino, weight='length')
    
    # Obtener coordenadas de la ruta
    coordenadas_ruta = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
    
    # Dibujar la ruta en el mapa
    folium.PolyLine(coordenadas_ruta, color='blue', weight=5).add_to(mapa)


# Agregar marcadores individuales (sin conexión)
for idx, punto in enumerate(marcadores_individuales, start=1):
    folium.Marker(punto, popup=f"Parada {idx}", icon=folium.Icon(color='red')).add_to(mapa)

# Guardar y abrir
mapa.save("LINEA17.html")
webbrowser.open("LINEA17.html")
