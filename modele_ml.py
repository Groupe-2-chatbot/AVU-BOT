
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Charger les exemples depuis le fichier JSON
with open("donnees/exemples.json", "r", encoding="utf-8") as fichier:
    donnees = json.load(fichier)

# 2. Préparer les phrases et les intentions
phrases = []
intentions = []

for intention, exemples in donnees.items():
    for phrase in exemples:
        phrases.append(phrase)
        intentions.append(intention)

# 3. Transformer les phrases en données numériques
vectoriseur = TfidfVectorizer()
X = vectoriseur.fit_transform(phrases)

# 4. Entraîner le modèle Machine Learning
modele = LogisticRegression(max_iter=1000)
modele.fit(X, intentions)

# 5. Afficher le résultat de l'entraînement
print("================================")
print(" AVU-BOT : MODELE ML ENTRAINE")
print("================================")
print("Nombre de phrases :", len(phrases))
print("Nombre d'intentions :", len(set(intentions)))
print("Intentions apprises :")

for intention in sorted(set(intentions)):
    print("-", intention)

# 6. Fonction de détection d'intention
def detecter_intention_ml(message, seuil=0.10):
    texte = vectoriseur.transform([message])
    probabilites = modele.predict_proba(texte)[0]
    index_max = probabilites.argmax()
    intention = modele.classes_[index_max]
    confiance = probabilites[index_max]

    if confiance < seuil:
        return "inconnue", confiance

    return intention, confiance


# TEST DES 11 INTENTIONS
if __name__ == "__main__":
    questions_test = [
        ("Salut, je viens demander un renseignement.", "salutation"),
        ("Je tiens à vous exprimer toute ma gratitude.", "remerciement"),
        ("Je suis nouveau, comment puis-je rejoindre votre établissement ?", "localisation"),
        ("Quelles sont les règles concernant les vêtements des étudiants ?", "tenue"),
        ("À qui dois-je m'adresser pour obtenir une assistance administrative ?", "contact_humain"),
        ("Quels moyens de déplacement l'école met-elle à disposition ?", "transport"),
        ("Je souhaite rejoindre IRGIB Africa, quelles démarches dois-je suivre ?", "inscription"),
        ("Les étudiants disposent-ils d'un endroit pour consulter des ouvrages ?", "bibliotheque"),
        ("Comment obtenir l'accès à Internet depuis mon ordinateur sur le campus ?", "wifi"),
        ("Où puis-je déposer mon scooter pendant les cours ?", "parking"),
        ("Est-il possible de déjeuner dans l'établissement ?", "cantine"),  
        ("Bonsoir, pourriez-vous me renseigner ?", "salutation"),
        ("Merci beaucoup pour votre disponibilité.", "remerciement"),
        ("À quelle adresse se trouve votre campus ?", "localisation"),
        ("Est-ce qu'un uniforme est obligatoire pour les étudiants ?", "tenue"),
        ("Puis-je parler directement à un responsable ?", "contact_humain"),
        ("Y a-t-il une navette pour les étudiants ?", "transport"),
        ("Quelles formalités faut-il remplir pour intégrer l'école ?", "inscription"),
        ("Quels sont les horaires de la salle de lecture ?", "bibliotheque"),
        ("Quel est le code pour se connecter au réseau sans fil ?", "wifi"),
        ("Où garer ma moto sur le campus ?", "parking"),
        ("Où puis-je acheter un repas pendant la pause ?", "cantine"),
        ("Je souhaite obtenir des renseignements sur les admissions.", "inscription"),
        ("Comment accéder aux locaux de l'université ?", "localisation"),
        ("Qui peut m'aider pour un problème administratif ?", "contact_humain"),
        ("Les bus passent-ils près du campus ?", "transport"),
        ("Je vous suis reconnaissant pour ces informations.", "remerciement"),
        ("Quel temps fera-t-il demain ?", "inconnue"),
        ("Comment préparer une pizza ?", "inconnue"),
        ("Qui a gagné le dernier match de football ?", "inconnue")
]
    seuils = [0.10, 0.15, 0.20, 0.25, 0.30]
    print("\n================================")
    print("EVALUATION SANS SEUIL")
    print("================================")

    bonnes_predictions = 0

    for question, intention_attendue in questions_test:
        question_vect = vectoriseur.transform([question])
        probabilites = modele.predict_proba(question_vect)[0]

        indice = probabilites.argmax()
        intention_predite = modele.classes_[indice]

        if intention_predite == intention_attendue:
            bonnes_predictions += 1

        print("Question :", question)
        print("Attendu :", intention_attendue)
        print("Prédit :", intention_predite)
        print()

    taux = bonnes_predictions / len(questions_test) * 100

    print("Bonnes prédictions :", bonnes_predictions, "/", len(questions_test))
    print("Taux de bonnes prédictions :", round(taux, 2), "%")
    for seuil in seuils:
        print("\n================================")
        print("TEST AVEC LE SEUIL :", seuil)
        print("================================")

        nombre_reconnues = 0
        bonnes_reponses = 0

        for question, intention_attendue in questions_test:
            question_vect = vectoriseur.transform([question])
            probabilites = modele.predict_proba(question_vect)[0]

            indice = probabilites.argmax()
            intention_candidate = modele.classes_[indice]
            confiance = probabilites[indice]

            if confiance < seuil:
                intention_predite = "inconnue"
            else:
                intention_predite = intention_candidate

            if intention_predite != "inconnue":
                nombre_reconnues += 1

            if intention_predite == intention_attendue:
                bonnes_reponses += 1

            print("\nQuestion :", question)
            print("Attendu :", intention_attendue)
            print("Meilleure intention proposée :", intention_candidate)
            print("Prédit :", intention_predite)
            print("Confiance :", round(confiance * 100, 2), "%")

        total_questions = len(questions_test)

        taux_reconnaissance = nombre_reconnues / total_questions * 100
        taux_exactitude = bonnes_reponses / total_questions * 100

        print("\n--------------------------------")
        print("BILAN DU SEUIL :", seuil)
        print("--------------------------------")
        print("Questions reconnues :", nombre_reconnues, "/", total_questions)
        print("Bonnes prédictions :", bonnes_reponses, "/", total_questions)
        print("Taux de reconnaissance :", round(taux_reconnaissance, 2), "%")
        print("Taux de bonnes prédictions :", round(taux_exactitude, 2), "%")
