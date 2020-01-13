import csv
from matplotlib.pyplot import plot

lecteur_paroles = csv.DictReader(open('ParoleFemmes.csv', 'r'))
paroles = [dict(ligne) for ligne in lecteur_paroles]

radios = {
    ligne['channel_name'] 
    for ligne in paroles 
    if ligne['media_type'] == 'radio' 
}

max_2017 = max(
    {
        (ligne['women_expression_rate'], ligne['channel_name']) 
        for ligne in paroles 
        if ligne['media_type'] == 'radio'
    }
)

taux_cheri = [float(ligne['women_expression_rate']) for ligne in paroles if ligne['channel_name'] == 'Chérie FM']

annee_cheri = [ligne['year'] for ligne in paroles if ligne['channel_name'] == 'Chérie FM']


plot(annee_cheri_int, taux_cheri, 'g--o')

