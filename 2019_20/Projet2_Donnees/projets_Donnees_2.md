# Données structurées

## Travail demandé

Tout au  long de  ce document qui  sera étudié  durant les 5  heures de  cours à
venir, des  questions seront posées, des  recherches seront à faire,  du travail
technique sera proposé et des réponses seront attendues. Vous regrouperez toutes
vos réponses  dans un document  `Sway` avec vos  deux noms, votre  classe, votre
groupe (2-1  signifie par exemple  projet vague 2 (Janvier  → Mars) et  groupe 1
(première rotation)).

Il faudra rendre  un travail **beaucoup plus  approfondi** que ce qui a  été fait au
trimestre précédent.

Vous créerez  un répertoire de  travail sur  votre espace personnel  du *Portail
office 365* dans lequel vous enregistrerez vos différents documents.

## Données et autres Big Data

Depuis  quelques  années, les  *données*  (data)  sont  devenues le  nouvel  *or
noir*. Le marché des *data broker* est en expansion exponentielle. 

1. Qu'est-ce que des data brokers ?
2. Qui est *Palantir* ?
3. Analysez l'[articl suivant](https://qz.com/213900/the-nine-companies-that-know-more-about-you-than-google-or-facebook/)
   (en anglais...). Qu'en pensez-vous ?
4.   Qu'est-ce  que   le   site   [peekYou](https://www.peekyou.com/)  ?   Qu'en
   pensez-vous ?
5. Les données doivent-elles être accessibles à tout le monde ? Lire par exemple
   cet [article](https://fr.wikipedia.org/wiki/Rien_%C3%A0_cacher_(argument)) de
   Wikipedia et pourquoi pas ce [film](https://www.youtube.com/watch?v=djbwzEIv7gE).

Nous n'allons pas travailler à présent sur des données personnelles mais sur les
données    accessibles   diffusées    par   des    organismes   publics    comme
[data.gouv.fr](https://www.data.gouv.fr/fr/)       ou      le       site      de
l'[Insee](https://insee.fr/fr/).




## Format csv

### Qu'est-ce ?

Qu'est-ce que le format `csv` ? Dans quelle situation le rencontre-t-on ? Quelle
est son histoire ? Quel est son lien avec les *Big Data* ?



### Utilisation d'un tableur

1. Voici par exemple [la liste des villes sous
vidéosurveillance](https://www.data.gouv.fr/fr/datasets/villes-sous-videosurveillance/#_)

Enregistrez la cible de ce lien [fichier au format
`csv`](https://www.data.gouv.fr/fr/datasets/r/b56c1eda-6b75-468a-b33f-147d37224c9e)
 
 
L'ouvrir avec un éditeur de texte et l'ouvrir avec un tableur.  Remarques ?
Problèmes ? Vous pouvez demander de l'aide...


Que faire avec ce fichier 

2. Créez à présent vous-même un petit fichier `csv` et ouvrez-le avec un tableur.

3.  Voici à présent 
un nouveau [fichier de travail](./titanic.csv). Enregistrez-le. 

Quels  sont les  **descripteurs** de  ce fichier  ? Quels  sont les  *types* des
**valeurs** associés à chaque descripteur ? 

À quoi correspondent les valeurs des différents descripteurs ?


Rédigez une phrase décrivant les informations données par la ligne numéro 37.

Quel était le prix moyen d'un billet ?

Quelle  était la  probabilité  de survie  en première  classe  ? Seconde  classe
Troisième classe ?

Quelle était la proportion d'enfants (de moins de 18 ans) dans chaque classe ?

### Avec Python (Deuxième séance)


Il est un peu pénible de traiter des  données avec un tableur, surtout s'il y en
a  beaucoup. Heureusement,  l'utilisation d'un  langage de  programmation adapté
peut largement nous aider comme par exemple Python.

C'est ce que nous verrons lors de la prochaine séance

## Format json (Dernière séance)


Nous avons déjà  rencontré le format `json`  lors de la découverte  de OSM. Vous
pouvez reprendre votre formidable et très complet travail de recherche du projet
précédent pour vous rafraîchir la mémoire.

### Exemple de manipulation d'un fichier `json` avec Python

Nous voulons  planifier une visite  de musées  londoniens. Nous savons  que nous
devrons commencer par la Wellcome Collection. Nous choisirons ensuite les musées
selon leur éloignememnt de ce point de  départ. *Nous voulons donc créer la liste
des  musées   londoniens  classés   selon  leur   éloignement  de   la  Wellcome
Collection*.

1. Pour cela, nous allons dans  un premier temps récupérer l'ensemble des musées
   londoniens  grâce à  une  requête effectuée  sur  `overpassTurbo` comme  nous
   l'avons découvert lors du projet précédent. 
   
   **Quelle requete doit-on écrire ? Comment faire ?**
2. Sur la partie droite de l'écran, vous voyez apparaître les musées représentés
   par des cercles  sur une carte. Si vous cliquez  sur l'onglet `Données`, vous
   voyez apparaître un texte qui débute ainsi :
```json
{
  "version": 0.6,
  "generator": "Overpass API 0.7.55.7 8b86ff77",
  "osm3s": {
    "timestamp_osm_base": "2020-01-05T09:57:02Z",
    "timestamp_areas_base": "2020-01-05T09:10:02Z",
    "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL."
  },
  "elements": [
    {
      "type": "node",
      "id": 19085022,
      "lat": 51.669645,
      "lon": -0.0682606,
      "tags": {
        "name": "Forty Hall Museum",
        "toilets:wheelchair": "yes",
        "tourism": "museum",
        "wheelchair": "yes",
        "wikidata": "Q5472972"
      }
    },
    {
      "type": "node",
      "id": 27408513,
      "lat": 51.5108862,
      "lon": -0.307107,
      "tags": {
        "name": "Pitzhanger Manor House and Gallery",
        "tourism": "museum",
        "website": "https://www.pitzhanger.org.uk/",
        "wikidata": "Q2097388"
      }
    },
    {
      "type": "node",
      "id": 29269886,
      "lat": 51.5228224,
      "lon": -0.1547768,
      "tags": {
        "addr:city": "London",
        "addr:housenumber": "8-10",
        "addr:postcode": "NW1 5LR",
        "addr:street": "Marylebone Road",
        "email": "guest.experience@madame-tussauds.com",
        "fhrs:confidence_management": "10",
        "fhrs:hygiene": "5",
        "fhrs:id": "428012",
        "fhrs:local_authority_id": "01066/4000/0/000",
        "fhrs:rating": "4",
        "fhrs:structural": "5",
        "name": "Madame Tussauds",
        "name:ru": "Мадам Тюссо",
        "name:zh": "杜莎夫人蜡像馆",
        "opening_hours": "Mo-Fr 09:30-17:30; Sa-Su 09:00-18:00",
        "phone": "+44 871 894 3000",
        "source:addr": "FSA Food Hygiene Ratings Database",
        "source:postcode": "FSA Food Hygiene Ratings Database",
        "toilets:wheelchair": "yes",
        "tourism": "museum",
        "website": "https://www.madametussauds.co.uk/london",
        "wheelchair": "yes",
        "wheelchair:description": "Bis auf die Bustour am Ende kann man sich alles ansehen. Und wenn man Hilfe braucht um sich mit einer Figur fotografieren zu lassen sind die Mitarbeiter zur Stelle.",
        "wikidata": "Q186309",
        "wikipedia": "en:Madame Tussauds London"
      }
    },
    {
      "type": "node",
      "id": 37124475,
      "lat": 51.36511,
      "lon": -0.1668055,
      "tags": {
        "description": "The water tower is a very unusual early 18th century garden building. As the name suggests, this contained a water-powered pump which supplied water to Carshalton House and the fountains in its garden.",
        "flickr": "https://www.flickr.com/photos/rogersg/3667834465/",
        "name": "Carshalton Water Tower",
        "tourism": "museum",
        "website": "http://www.carshaltonwatertower.co.uk",
        "wikidata": "Q17531582"
      }
    },
    {
      "type": "node",
      "id": 261700004,
      "lat": 51.4736073,
      "lon": -0.1155806,
      "tags": {
        "name": "The Type Museum",
        "tourism": "museum",
        "wikidata": "Q7860886",
        "wikipedia": "en:Type Museum"
      }
    },
	...
```


Un part  très importante des  données disponibles  sur la planète  sont stockées
sous un format similaire, à savoir sous la forme `clé : valeur`.

Par exemple, `"lat":  51.4736073` donne la latitude du lieu,  `"name": "The Type
Museum"` donne son nom, etc.



### À faire : récupération et exploitation d'un fichier `json` en ligne
