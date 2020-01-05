import json
from geopy.distance import geodesic

with open("./exportOSM.json") as js:
    json_brut = json.load(js)['elements']

musees_coords = { musee['tags']['name'] : (musee['lat'], musee['lon']) for musee in json_brut }

w_c = musees_coords['Wellcome Collection']

distances = [(musee, geodesic(w_c, musees_coords[musee]).km) for musee in musees_coords]

ordre_visites = sorted(distances, key=lambda couple: couple[1])

liste_ord_musees = [visite[0] for visite in ordre_visites]

print(liste_ord_musees)
