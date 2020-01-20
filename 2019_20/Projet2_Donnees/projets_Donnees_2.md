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
2.  Qui  est  *Palantir*  ?  Quel  est  son  rôle  ?  Qu'est-ce  que  *Cambridge
   Analytica* ?  Quelle différence entre l'utilisation  des données personnelles
   par l'équipe de campagne d'Obama en 2012 et celle de Trump en 2016 ? Qu'en pensez-**vous**?
3. Analysez l'[article suivant](https://qz.com/213900/the-nine-companies-that-know-more-about-you-than-google-or-facebook/)
   (en anglais...). Qu'en pensez-**vous** ?
4.   Qu'est-ce  que   le   site   [peekYou](https://www.peekyou.com/)  ?   Qu'en
   pensez-**vous** ? Est-ce juste un annuaire genre 118-218 ?
5. Les données doivent-elles être accessibles à tout le monde ? Lire par exemple
   cet [article](https://fr.wikipedia.org/wiki/Rien_%C3%A0_cacher_(argument)) de
   Wikipedia et pourquoi pas ce [film](https://www.youtube.com/watch?v=djbwzEIv7gE).
6. Les données personnelles sont-elles traitées de la même façon en Europe ? Aux
   EUA ? En Chine ? Quelles différences ? Qu'en pensez-**vous** ?


Nous n'allons pas travailler à présent sur des données personnelles mais sur les
données accessibles diffusées par des organismes publics comme
[data.gouv.fr](https://www.data.gouv.fr/fr/)       ou      le       site      de
l'[Insee](https://insee.fr/fr/).




## Format csv

### Qu'est-ce ?

Qu'est-ce que le format `csv` ? Dans quelle situation le rencontre-t-on ? Quelle
est son histoire ? Quel est son lien avec les *Big Data* ?



### Utilisation d'un tableur

1. Voici par exemple des données sur 
[le temps de parole des femmes](https://www.data.gouv.fr/fr/datasets/temps-de-parole-des-hommes-et-des-femmes-a-la-television-et-a-la-radio/#_)
à  la  radio  et  à  la  télévision.   Lisez  les  explications  de  ce  jeu  de
données. Plusieurs fichiers sont ensuite mis à disposition au format CSV.

Voici le premier [fichier au format`csv`](./ParoleFemmes_fr.csv)
 
Voici  le  même  fichier, également  au  format  CSV,  mais  on a  remplacé  les
points-virgules par des virgules, et les virgules par des points : [fichier au format`csv`](./ParoleFemmes.csv)
 
Sur les  pages de  ces deux fichiers,  cliquez sur l'onglet  `Raw` qui  donne le
fichier brut ? Que constatez-vous ? Comment l'expliquez-vous ? 

Enregistrez ces deux fichiers sous forme brute.

Nous voulons maintenant les ouvrir avec `Microsoft Excel`.
Pour cela  on ouvre  `Excel`, on  va sur l'onglet  `Données`, puis  sur `Données
externes` puis sur `À partir du texte` et naviguez ensuite vers le répertoire où
se situent les fichiers. Par  exemple choisissons `ParolesFemmes`. On clique sur
`Importer`. Un menu apparaît  et on voit un aperçu du fichier  décodé en bas. On
peut choisir `UTF-8`  pour l'encodage des caractères et on  voit que les accents
de `Chérie` apparaissent maintenant correctement. Il faut ensuite choisir le bon
séparateur sur  la page suivante. On  choisit la virgule et  maintenant l'aperçu
change et tout apparaît par colonne. On clique ensuite sur `Terminer`.







Que faire avec ces fichiers ? Peut-on répondre à ce genre de questions ? Comment ?

* Quelle est la station de radio qui donne le plus la parole aux femmes ?

* Quelle est la  station dont le temps de parole des femmes  a le plus progressé
  depuis 2012 ?
  
* Est-ce que les femmes ont plus la parole à la télévision ou à la radio ?

* Imaginez vos propres questions et répondez-y.


2. Créez à présent vous-même un petit fichier `csv` et ouvrez-le avec un tableur.

3.  Voici à présent un nouveau fichier de travail au 
[format français](./titanic.csv) et au [format anglo-saxon](./titanic_gb.csv). Enregistrez-les. 
Ouvrez-les avec `Microsoft Excel`.

	* Quels sont les **descripteurs** de ce fichier ? Quels sont les *types* des
	**valeurs** associés à chaque descripteur ? 

	* À quoi correspondent les valeurs des différents descripteurs ?


	* Rédigez une phrase décrivant les informations données par la ligne numéro 37.

	* Quel était le prix moyen d'un billet ?

	* Quelle était la probabilité de survie en première classe ? Seconde classe
		Troisième classe ?

	* Quelle était la proportion d'enfants (de moins de 18 ans) dans chaque classe ?

### Avec Python (Deuxième séance)


Il est un peu pénible de traiter des  données avec un tableur, surtout s'il y en
a  beaucoup. Heureusement,  l'utilisation d'un  langage de  programmation adapté
peut largement nous aider comme par exemple Python.

Vous allez ouvrir `Anaconda` puis `Jupyter`. 

Voux  allez  enregistrer  [ce   fichier](https://raw.githubusercontent.com/Informathix/2nde/master/2019_20/Projet2_Donnees/ManipCSV.ipynb)  et  l'ouvrir  depuis
`Jupyter`.

Vous devez obtenir quelque chose qui ressemble à [ça](./ManipCSV.ipynb) 

Vous répondrez aux questions posées dans ce document et inclurez ce fichier dans
votre envoi. Attention ! Il faut renommer le fichier avec votre nom : `ManipCSV_p_nom_classe.ipynb`.

<!--

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


-->
