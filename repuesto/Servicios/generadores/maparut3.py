import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas para hacer la línea de la ruta (Si quieres ver los puntos en el mapa quita el "#" al final del primer for)
paradas = [
    (-0.957324, -80.763925), #1
    (-0.954807, -80.742068), #2
    (-0.950010, -80.734305), #3
    (-0.951076, -80.733492), #4
    (-0.949387, -80.731384), #5
    (-0.951783, -80.729531), #6
    (-0.946710, -80.723394), #7
    (-0.949385, -80.721377), #8
    (-0.950467, -80.722194), #9
    (-0.957251, -80.729181), #10
    (-0.954471, -80.725126), #11
    (-0.957024, -80.723781), #12
    (-0.955915, -80.716726), #13
    (-0.959593, -80.713855), #14
    (-0.972485, -80.701769), #15
    (-0.987477, -80.708883), #16
    (-0.988856, -80.706967), #17
    (-0.995303, -80.706887), #18
    (-0.998252, -80.706997), #19
    (-0.997324, -80.720058), #20


]

# Coordenadas de las paradas (Se muestran los puntos en el mapa)
marcadores_individuales = [
    
    (-0.957324, -80.763925),
    (-0.958905, -80.759107),
    (-0.957234, -80.755203),
    (-0.957455, -80.752541),
    (-0.957897, -80.748233),
    (-0.956756, -80.745937),
    (-0.955565, -80.742716),
    (-0.954095, -80.739522),
    (-0.952088, -80.736324),
    (-0.951190, -80.733505),
    (-0.949508, -80.731421),
    (-0.951108, -80.728604),
    (-0.948855, -80.725876),
    (-0.946796, -80.723359),
    (-0.950077, -80.722125),
    (-0.952779, -80.722768),
    (-0.954704, -80.725737),
    (-0.956171, -80.724441),
    (-0.956397, -80.721767),
    (-0.956291, -80.719855),
    (-0.955749, -80.716346),
    (-0.956728, -80.715546),
    (-0.959678, -80.713483),
    (-0.961294, -80.710777),
    (-0.964192, -80.708415),
    (-0.966780, -80.706383),
    (-0.967851, -80.705512),
    (-0.972493, -80.701888),
    (-0.974560, -80.704401),
    (-0.978398, -80.705730),
    (-0.980560, -80.706334),
    (-0.984532, -80.707738),
    (-0.987764, -80.708585),
    (-0.990472, -80.707392),
    (-0.994044, -80.706888),
    (-0.997367, -80.707003),
    (-0.998082, -80.707018),
    (-0.995937, -80.709171),
    (-0.992365, -80.710862),
    (-0.990698, -80.713743),
    (-0.992581, -80.716364),
    (-0.995960, -80.719200),


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
mapa.save("LINEA3.html")
webbrowser.open("LINEA3.html")