import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas de la ruta
paradas = [
    (-0.956938, -80.765765), #1
    (-0.959060, -80.758438), #2
    (-0.958411, -80.758006), #3 
    (-0.957846, -80.748158), #4
    (-0.957664, -80.747308), #5
    (-0.955636, -80.743957), #6
    (-0.955166, -80.741348), #7
    (-0.955042, -80.741249), #8 
    (-0.951341, -80.735282), #9 
    (-0.952095, -80.734789), #10
    (-0.949355, -80.731417), #11
    (-0.946215, -80.733791), #12
    (-0.946598, -80.734316), #13
    (-0.944975, -80.735488), #14
    (-0.944591, -80.733699), #15
    (-0.941911, -80.733103), #16
    (-0.941595, -80.729896), #17
    (-0.941804, -80.727027), #18
    (-0.949283, -80.721191), #19
    (-0.951978, -80.722134), #20
    (-0.953724, -80.717819), #21
    (-0.957114, -80.715186), #22
    (-0.959325, -80.718540), #23
    (-0.960890, -80.717517), #24
    (-0.959927, -80.716080), #25
    (-0.962619, -80.714331), #26
    (-0.960977, -80.711878), #27
    (-0.974569, -80.700153), #28
    (-0.981029, -80.704272), #29
    (-0.980638, -80.705259), #30
    (-0.988055, -80.707824), #31
    (-0.990034, -80.704566), #32 
    (-0.994090, -80.706010), #33
    (-0.994185, -80.707364), #34
    (-1.000293, -80.707098), #35
    (-1.003055, -80.710142), #36
    (-1.002334, -80.712486), #37
    (-1.005835, -80.714280), #38
    (-1.010836, -80.718371), #39


]

# Coordenadas para marcadores individuales (en rojo)
marcadores_individuales = [
    (-0.957592, -80.763628),
    (-0.958691, -80.760043),
    (-0.957529, -80.756058),
    (-0.957398, -80.752181),
    (-0.957810, -80.748519),
    (-0.957810, -80.748519),
    (-0.955532, -80.742723),
    (-0.953271, -80.738409),
    (-0.951184, -80.733587),
    (-0.949429, -80.731325),
    (-0.946320, -80.733749),
    (-0.944955, -80.734998),
    (-0.944155, -80.733586),
    (-0.9418279335529652, -80.732355137707379),
    (-0.9417132898392765, -80.73076927697498),
    (-0.942431, -80.726168),
    (-0.946335, -80.721880),
    (-0.952870, -80.719884),
    (-0.953751, -80.717807),
    (-0.956151, -80.715797),
    (-0.958636, -80.717543),
    (-0.959962, -80.716191),
    (-0.961112, -80.711202),
    (-0.963641, -80.708797),
    (-0.970070, -80.703735),
    (-0.974494, -80.700253),
    (-0.977156, -80.702065),
    (-0.980811, -80.704091),
    (-0.985677, -80.706927),
    (-0.988734, -80.706626),
    (-0.990901, -80.704881),
    (-0.994018, -80.705962),
    (-0.995690, -80.707182),
    (-0.999615, -80.707060),
    (-1.002390, -80.712247),
    (-1.005155, -80.713896),
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
    
# Agregar marcadores individuales
for idx, punto in enumerate(marcadores_individuales, start=1):
    folium.Marker(punto, popup=f"Parada {idx}", icon=folium.Icon(color='red')).add_to(mapa)

#Guardar y abrir SOLO mapar10.html
mapa.save("mapar10.html")
webbrowser.open("mapar10.html")
