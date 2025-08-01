import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas para hacer la línea de la ruta (Si quieres ver los puntos en el mapa quita el "#" al final del primer for)
paradas = [
    (-0.957333, -80.764332

), #1
    (-0.962560, -80.674425), #2
    (-0.969399, -80.681265), #3
    (-0.973499, -80.680949), #4
    (-0.984558, -80.686665), #5
    (-0.988050, -80.699335), #6
    (-0.984310, -80.700983), #7
    (-0.984812, -80.702536), #8
    (-0.989661, -80.705175), #9
    (-0.988665, -80.706885), #10
    (-0.994178, -80.707342), #11
    (-0.998269, -80.706999), #12
    (-0.972785, -80.730446), #13
    (-0.963889, -80.735236), #14
    (-0.950715, -80.720240), #15
    (-0.943468, -80.724330), #16
    (-0.947090, -80.728710), #17
    (-0.950147, -80.726481), #18
    (-0.952361, -80.729120), #19
    (-0.944848, -80.734670), #20
    (-0.945222, -80.737205), #21
    (-0.955697, -80.744402), #22
    (-0.957605, -80.747498), #23
    (-0.956606, -80.772938), #24
    (-0.959713, -80.807146), #25
]

# Coordenadas de las paradas (Se muestran los puntos en el mapa)
marcadores_individuales = [
    
    (-0.958994, -80.687447),
    (-0.959767, -80.683976),
    (-0.959847, -80.680505),
    (-0.961338, -80.677298),
    (-0.962712, -80.674420),
    (-0.965372, -80.677023),
    (-0.967821, -80.679648),
    (-0.970663, -80.681476),
    (-0.977538, -80.682687),
    (-0.980618, -80.684393),
    (-0.983929, -80.686231),
    (-0.983986, -80.689003),
    (-0.986424, -80.695500),
    (-0.984732, -80.700751),
    (-0.985502, -80.702827),
    (-0.988641, -80.704653),
    (-0.989004, -80.706944),
    (-0.992665, -80.707192),
    (-0.995717, -80.707167),
    (-0.997856, -80.707390),
    (-0.994604, -80.709571),
    (-0.991949, -80.711393),
    (-0.990054, -80.714896),
    (-0.986986, -80.716189),
    (-0.983934, -80.715261),
    (-0.981145, -80.717970),
    (-0.979659, -80.721049),
    (-0.976253, -80.722750),
    (-0.974582, -80.725672),
    (-0.973176, -80.728908),
    (-0.971615, -80.732250),
    (-0.968151, -80.733290),
    (-0.965040, -80.733950),
    (-0.962846, -80.734116),
    (-0.960373, -80.731922),
    (-0.957611, -80.729272),
    (-0.955052, -80.725919),
    (-0.953642, -80.722770),
    (-0.951228, -80.721081),
    (-0.948450, -80.720866),
    (-0.945629, -80.721853),
    (-0.943283, -80.724428),
    (-0.945842, -80.727141),
    (-0.948251, -80.727795),
    (-0.951115, -80.727520),
    (-0.951191, -80.729911),
    (-0.948201, -80.732157),
    (-0.945080, -80.734462),
    (-0.945373, -80.737227),
    (-0.948417, -80.739790),
    (-0.950790, -80.742149),
    (-0.954278, -80.743791),
    (-0.956799, -80.745969),
    (-0.957596, -80.749049),
    (-0.957254, -80.752751),
    (-0.957376, -80.755562),
    (-0.958558, -80.759497),
    (-0.957472, -80.763056),
    (-0.956491, -80.766415),
    (-0.955514, -80.770039),
    (-0.956490, -80.773049),
    (-0.954356, -80.776423),
    (-0.954940, -80.778907),
    (-0.956549, -80.782431),
    (-0.958840, -80.785028),
    (-0.959387, -80.787930),
    (-0.959365, -80.792420),
    (-0.960320, -80.798492),
    (-0.960949, -80.802054),
    (-0.960445, -80.805729),


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
mapa.save("mapar1.html")
webbrowser.open("mapar1.html")