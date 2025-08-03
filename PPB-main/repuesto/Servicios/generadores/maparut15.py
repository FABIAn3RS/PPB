import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas de las paradas
paradas = [
   (-0.978732, -80.723489), #1 
   (-0.978593, -80.721755), #2
   (-0.977692, -80.721753), #3
   (-0.975889, -80.719747), #4
   (-0.973393, -80.718557), #5 
   (-0.972357, -80.717440), #6
   (-0.972261, -80.716639), #7
   (-0.971459, -80.716828), #8
   (-0.970682, -80.715616), #9
   (-0.969634, -80.714621), #10
   (-0.969203, -80.714251), #11
   (-0.968645, -80.714594), #12
   (-0.967708, -80.713743), #13
   (-0.967135, -80.714473), #14
   (-0.964969, -80.712862), #15
   (-0.963243, -80.715283), #16
   (-0.960566, -80.717046), #17
   (-0.958684, -80.714229), #18
   (-0.957717, -80.713913), #19
   (-0.955351, -80.715742), #20
   (-0.953755, -80.717569), #21
   (-0.952113, -80.721730), #22
   (-0.955356, -80.726843), #23
   (-0.957364, -80.729056), #24
   (-0.962620, -80.726571), #25
   (-0.963987, -80.729299), #26
   (-0.964075, -80.732869), #27
   (-0.970287, -80.739547), #28
   (-0.972475, -80.740938), #29
   (-0.973338, -80.742415), #30 
   (-0.985416, -80.749108), #31
   (-0.993376, -80.755186), #32
   (-0.995252, -80.759805), #33 
   (-0.999786, -80.761264), #34
   (-1.003129, -80.759601), #35 
]

# Marcadores individuales (sin conexión)
marcadores_individuales = [
    (-0.974341, -80.719047),
    (-0.999572, -80.761210),
    (-0.996969, -80.760348),
    (-0.993946, -80.756792),
    (-0.993217, -80.755114),
    (-0.989559, -80.753848),
    (-0.987224, -80.751373),
    (-0.984982, -80.748685),
    (-0.979882, -80.746154),
    (-0.974743, -80.743596),
    (-0.952393, -80.721892), 
    (-0.969426, -80.738331),
    (-0.967109, -80.735350),
    (-0.965841, -80.733801),
    (-0.964266, -80.731332),
    (-0.963778, -80.728826),
    (-0.961714, -80.726668),
    (-0.9608273246781378, -80.72696684329328),
    (-0.958578, -80.728209),
    (-0.956511, -80.727965),
    (-0.954077, -80.724305),
    (-0.9543022272505353, -80.72531097467116),
    (-0.952711, -80.721869),
    (-0.954963, -80.715926),
    (-0.959342, -80.715266),
    (-0.962735, -80.715597),
    (-0.964878, -80.712980),
    (-0.967467, -80.714041),
    (-0.969589, -80.714686),
    (-0.972095, -80.716696),
    (-0.974535, -80.719083),
    (-0.979039, -80.724054),
]

# Índices de tramos a forzar como línea recta:
# 11 corresponde al tramo 12→13
tramos_rectos = [11]

# Descargar red de calles
G = ox.graph_from_point(paradas[0], dist=20000, network_type='drive', simplify=False)
G = G.to_undirected()

# Crear el mapa
mapa = folium.Map(location=paradas[0], zoom_start=14)

for i in range(len(paradas) - 1):
    origen = paradas[i]
    destino = paradas[i + 1]

    # Si es uno de los tramos "forzados", dibujamos la recta;
    # en caso contrario, calculamos la ruta por la red
    if i in tramos_rectos:
        coordenadas = [origen, destino]
    else:
        nodo_origen  = ox.distance.nearest_nodes(G, origen[1], origen[0])
        nodo_destino = ox.distance.nearest_nodes(G, destino[1], destino[0])
        if nx.has_path(G, nodo_origen, nodo_destino):
            ruta = nx.shortest_path(G, nodo_origen, nodo_destino, weight='length')
            coordenadas = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
        else:
            print(f"❌ No hay ruta entre Parada {i+1} y Parada {i+2}")
            continue

    folium.PolyLine(coordenadas, color='blue', weight=5, opacity=0.8).add_to(mapa)
    
# Agregar marcadores individuales en rojo
for idx, punto in enumerate(marcadores_individuales, start=1):
    folium.Marker(punto, popup=f"Marcador {idx}", icon=folium.Icon(color='red')).add_to(mapa)

# Guardar y abrir el mapa
mapa.save("mapar15.html")
webbrowser.open("mapar15.html")
# Función para abrir un mapa específico