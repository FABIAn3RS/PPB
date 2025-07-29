import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas para hacer la línea de la ruta (Si quieres ver los puntos en el mapa quita el "#" al final del primer for)
paradas = [

    (-0.984230, -80.689719), #1
    (-0.981462, -80.686768), #2
    (-0.977949, -80.691237), #3
    (-0.976243, -80.689856), #4
    (-0.975207, -80.690584), #5
    (-0.968206, -80.693239), #6
    (-0.966477, -80.697385), #7
    (-0.963287, -80.699397), #8
    (-0.964045, -80.700341), #9
    (-0.960544, -80.702692), #10
    (-0.956543, -80.699460), #11
    (-0.956335, -80.703487), #12
    (-0.953871, -80.709844), #13
    (-0.951726, -80.717739), #14
    (-0.950826, -80.721106), #15
    (-0.948509, -80.723195), #16
    (-0.953080, -80.728588), #17
    (-0.953912, -80.727973), #18
    (-0.956010, -80.730432), #19
    (-0.953383, -80.731979), #20
    (-0.955559, -80.744291), #21
    (-0.957158, -80.755152), #22
    (-0.957186, -80.764259), #23

]

# Coordenadas de las paradas (Se muestran los puntos en el mapa)
marcadores_individuales = [
    
    (-0.981652, -80.686835),
    (-0.979529, -80.689248),
    (-0.977068, -80.690554),
    (-0.974629, -80.690525),
    (-0.971207, -80.690207),
    (-0.968728, -80.692297),
    (-0.967979, -80.695664),
    (-0.965525, -80.697621),
    (-0.963330, -80.700542),
    (-0.961416, -80.701587),
    (-0.958652, -80.701256),
    (-0.956367, -80.700175),
    (-0.956258, -80.703568),
    (-0.953644, -80.709968),
    (-0.952689, -80.713795),
    (-0.951911, -80.717022),
    (-0.950360, -80.720662),
    (-0.949209, -80.722477),
    (-0.949897, -80.724893),
    (-0.952198, -80.727641),
    (-0.954678, -80.728952),
    (-0.954547, -80.731196),
    (-0.953454, -80.733082),
    (-0.955409, -80.737341),
    (-0.955113, -80.740848),
    (-0.955464, -80.744317),
    (-0.957469, -80.747259),
    (-0.957342, -80.751791),
    (-0.957099, -80.754959),
    (-0.958379, -80.758209),
    (-0.958231, -80.760632),
    (-0.957172, -80.764177),

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
mapa.save("LINEA4.html")
webbrowser.open("LINEA4.html")