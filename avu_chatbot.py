
# AVU-BOT : Assistant de Vie Universitaire
# Universite : IRGIB Africa
# Langues : Francais et Anglais

print("====================================")
print("       BIENVENUE SUR AVU-BOT")
print("       WELCOME TO AVU-BOT")
print("====================================")
if __name__ == "__main__":
    # Choix de la langue
    while True:
        print("\nChoisis ta langue / Choose your language:")
        print("1 - Francais")
        print("2 - English")

        choix = input("Ton choix / Your choice: ")

        if choix == "1":
            langue = "fr"
            print("\nBienvenue sur AVU-BOT !")
            break

        elif choix == "2":
            langue = "en"
            print("\nWelcome to AVU-BOT!")
            break

        else:
            print("Choix incorrect. Reessaie.")
            print("Incorrect choice. Try again.")

    # On demande le nom de l'etudiant
    if langue == "fr":
        nom = input("Comment tu t'appelles ? ")
        print("Bonjour", nom, "! Je suis AVU-BOT. En quoi puis-je t'aider ?")
    else:
        nom = input("What is your name? ")
        print("Hello", nom, "! I am AVU-BOT. How can I help you?")

# Memoire de la derniere intention
derniere_intention = "Aucune"

# Fonction qui analyse les questions
def repondre(question, langue):

    question = question.lower()

    # Salutation
    if ("bonjour" in question or "salut" in question
        or "bonsoir" in question or "hello" in question
        or "hi" in question or "good morning" in question 
        or "coucou" in question or "hey" in question or "slt" in question 
        or "bjr" in question or "cc" in question):

        intention = "Salutation"

        if langue == "fr":
            reponse = "Bonjour😊! Bienvenue à IRGIB AFRICA UNIVERSITY. Je suis AVU-Bot votre assistant universitaire. Comment puis-je vous aider?"
        else:
            reponse = "Hello 😊! Welcome to IRGIB AFRICA UNIVERSITY. I'm AVU-Bot, your university assistant. How can I help you??"

    # Remerciement
    elif ("merci" in question or "thanks" in question
          or "thank you" in question or "azy" in question or "thx" in question
          or "merci beaucoup" in question or "thank you very much" in question
          or "bye" in question or "goodbye" in question or "au revoir" in question
          or "super" in question or "great" in question or "awesome" in question):

        intention = "Remerciement"

        if langue == "fr":
            reponse = "Avec plaisir ! Merci d’avoir utilisé votre assistant de vie universitaire. Je suis toujours disponible pour vous aider.N’hesitez pas à revenir si vous avez besoin d’aide😊."
        else:
            reponse = "You're very welcome! Thank you for using your student life assistant. I'm always available to help you. Don't hesitate to come back if you need help 😊."

    # Localisation
    elif ("adresse" in question or "localisation" in question
          or "ou se trouve l'universite" in question or "where is the university" in question
          or "location" in question or "address" in question 
          or "lieu" in question or "place" in question or "emplacement" in question):

        intention = "Localisation"

        if langue == "fr":
            reponse = """IRGIB AFRICA UNIVERSITY dispose de plusieurs sites et centres d'application au Bénin. 
            Pour Cotonou, le site officiel mentionne. Le siège: rue 1886, derrière l'immeuble Air France, route de l'aéroport. Le campus d'Akpakpa: indiqué comme campus universitaire 
            .L'université  d'akpakpa/Cotonou est situé en face du stade René Pleven, même alignement entre la CNSS et la SOBEBRA. 
            Quant à la localisation des salles et autres bâtiments consultez le plan du campus où rapprochez vous de l'administration.."""
        else:
            reponse = """IRGIB AFRICA UNIVERSITY has several campuses and application centers in Benin. 
            For Cotonou, the official website lists: 
            Headquarters: Rue 1886, behind the Air France building, airport road The Akpakpa campus: indicated as a university campus.
            The university campus in Akpakpa/Cotonou is located opposite the René Pleven Stadium, on the same side of the road as the CNSS and SOBEBRA buildings. For the location of classrooms and other buildings, please consult the map.."""

    # Tenue
    elif ("uniforme" in question or "tenue" in question
          or "dress code" in question or "uniform" in question
          or "clothes" in question or "vetements" in question
          or "dress" in question or "habits" in question or "dress code" in question
          or "style" in question or "dress style" in question or "outfit" in question
          or "shoes" in question or "chaussures" in question):

        intention = "Tenue"

        if langue == "fr":
            reponse = (
                "Les étudiants disposent de 2 uniformes. L'uniforme officiel est porté du lundi au mercredi, "
                "et le polo Lacoste accompagné d'un jean ou d'un pantalon bleu ou noir du jeudi au vendredi, "
                "L'achat de l'uniforme se fait auprès du styliste. Quant aux chaussures, ce sont des ballerines "
                "pour les filles et des chaussures en cuir pour les garçons, toutes de couleurs noires du lundi au mercredi, "
                "et les chaussures que vous voulez du jeudi au vendredi tant qu'elles sont fermées."
            )
        else:
            reponse = (
                "Students have two uniforms available. The official uniform is worn from Monday to Wednesday, "
                "and the Lacoste uniform paired with jeans or blue or black trousers from Thursday to Friday, "
                "Uniforms are purchased from the stylist. As for shoes, it is ballet flats for girls and leather "
                "shoes for boys, all black from Monday to Wednesday, and any shoes you like from Thursday to Friday, "
                "as long as they are closed."
            )

    # Contact humain
    elif ("responsable" in question or "contact" in question
          or "parler a quelqu'un" in question
          or "staff" in question or "contact person" in question
          or "talk to someone" in question or "secretary" in question or "administrateur" in question
          or "human contact" in question or "contact humain" in question or "contactez quelqu'un" in question):

        intention = "Contact humain"

        if langue == "fr":
            reponse = "Vous pouvez joindre l’administration en direct sur le " \
            " +2290196171910 (acceuil français) ou sur le +2290167296464( accueil anglais)," \
            " soit via WhatsApp sur le +22999190085, " \
            "soit via Email : Contact@irgibafrica.university ."
        else:
            reponse = "You can contact the administration directly at" \
            " +2290196171910 (French reception) or +2290167296464 (English reception), " \
            "via WhatsApp at +22999190085, " \
            "or by email: Contact@irgibafrica.university ."

    # Transport
    elif ("bus" in question or "transport" in question
          or "deplacement" in question or "trajet" in question 
          or "bus service" in question or "commute" in question
          or "transportation" in question):

        intention = "Transport"

        if langue == "fr":
            reponse = "Pour les étudiants ne vivant pas à proximité, l'université dispose de bus universitaire. Concernant les tarifs et les éventuels réductions, rapprochez vous de l'administration. ."
        else:
            reponse = "For students who do not live nearby, the university provides a bus service. For fares and any applicable discounts, please contact the administration."

    # Inscription
    elif ("inscription" in question or "inscrire" in question
          or "dossier" in question or "admission" in question
          or "registration" in question or "enroll" in question
          or "documents" in question or "integration" in question
          or "integrer" in question or "enrollment" in question):

        intention = "Inscription"

        if langue == "fr":
            reponse = """Pour vous inscrire, rendez vous sur le portail officiel de l’université (http://irgibafrica.university)
            et suivez les étapes indiquées ou rendez vous sur le site physique de l’établissement.
            Pour connaître la liste complète des pièces et les frais actualisés, contactez l’administration ou consultez le site officiel."""
        else:
            reponse = """To register, go to the official university portal (http://irgibafrica.university) and follow the steps indicated or go to the physical site of the institution.
                    For a complete list of required documents and updated fees, contact the administration or visit the official website."""

    # Bibliotheque
    elif ("bibliotheque" in question or "livre" in question
          or "emprunter" in question or "lecture" in question
          or "library" in question or "book" in question
          or "reading" in question or "lire" in question or "borrow" in question
          or "Emprunter un livre" in question or "Borrow a book" in question):

        intention = "Bibliotheque"

        if langue == "fr":
            reponse = """L’université dispose d’une bibliothèque qui met à votre disposition plus de 50.000 ouvrages (livres documents,..) en français comme en anglais ainsi que des espaces de travail.
            La bibliothèque numérique est également disponible à la direction. Concernant les jours ouvrables, la bibliothèque est ouverte du lundi au vendredi de 8h à 17h. Pour connaître les horaires, les conditions d'accès et les modalités d'emprunt,
            veuillez vous renseigner auprès de l'université.
            Plus d'informations : https://irgibafrica.university/library.html"""
        else:
            reponse = ("The university has a library with over 50,000 items (books, documents, etc.) in both French and English, as well as study spaces. "
                       "The digital library is also available at the administration office. Regarding working days, the library is open Monday to Friday from 8am to 5pm. "
                       "For opening hours, access conditions, and borrowing procedures, please contact the university. "
                       "More information: https://irgibafrica.university/library.html")

    # Wi-Fi
    elif ("wifi" in question or "wi-fi" in question
          or "internet" in question or "connexion" in question
          or "connection" in question or "network" in question or "réseau" in question
          or "WIFI" in question or "Wi-Fi" in question or "connexion internet" in question):

        intention = "Wi-Fi"

        if langue == "fr":
            reponse = "Pour accéder au wifi universitaire, demandez les identifiants de connexion au service informatique. ."
        else:
            reponse = "To access the university wifi, request the login credentials from the IT department."

    # Parking
    elif ("parking" in question or "voiture" in question
          or "moto" in question or "car park" in question
          or "motorbike" in question or "garer" in question or "stationnement" in question):

        intention = "Parking"

        if langue == "fr":
            reponse = "L'université dispose de parking destinée aux stationnements des motos pour les étudiants. Pour obtenir les informations complémentaires concernant son emplacement, les horaires d'accès et les conditions d'utilisation veuillez vous rapprocher de l'administration de l'Université."
        else:
            reponse = "The university has a motorcycle parking area for students. For further information regarding its location, access hours,For terms of use, please contact the University administration."
    # Cantine
    elif ("cantine" in question or "repas" in question
            or "food" in question or "canteen" in question
            or "restaurant" in question or "cafeteria" in question
            or" menu" in question or "plat" in question or "dish" in question
            or "restaurant universitaire" in question or "university restaurant" in question
            or"manger" in question or "eat" in question or "food service" in question):
    
            intention = "Cantine"
    
            if langue == "fr":
                reponse = "RGIB AFRICA dispose d’une cantine offrant une variété de mets afin de satisfaire les étudiants. Pour avoir la liste des plats rendez vous à la cantine. Vous pouvez demander aux étudiants sur place de vous montrer le chemin si vous êtes nouveau."
            else:
                reponse = "RGIB AFRICA has a cafeteria offering a variety of dishes to satisfy students. For the menu, please visit the cafeteria. You can ask students on site to show you the way if you are new."
   
    # Question non reconnue
    else:
        intention = "Inconnue"

        if langue == "fr":
            reponse = ("Désolé, je n'ai pas réussi à comprendre votre demande. 😕 Pourriez-vous reformuler votre question ?\n\n"
                       "Je suis AVU Bot, un assistant spécialisé dans la vie universitaire à IRGIB AFRICA. Je peux vous renseigner sur les formations, les inscriptions, la bibliothèque, les laboratoires, la localisation, la cantine et le transport.\n\n"
                       "Si votre demande nécessite une intervention humaine, contactez l'administration au +229 01 96 17 19 10 ou par e-mail à contact@irgibafrica.university.")
        else:
            reponse = (
                "Sorry, I didn't quite understand your request. 😕 Could you please rephrase your question? "
                "I'm AVU Bot, a student life assistant at IRGIB AFRICA. I can provide you with information on "
                "courses, registration, the library, laboratories, location, the canteen and transportation.\n\n"
                "If your request requires human intervention, please contact the administration at "
                "+229 01 96 17 19 10 or by email at contact@irgibafrica.university."
            )

    return reponse, intention

if __name__ == "__main__":
     # Conversation avec l'etudiant
    while True:

        if langue == "fr":
            question = input("\nToi : ")
        else:
            question = input("\nYou: ")

    # Pour quitter le chatbot
        if question.lower() == "quitter" or question.lower() == "quit" or question.lower() == "exit":

            if langue == "fr":
                print("AVU-BOT : Au revoir", nom, "! A bientot.")
            else:
                print("AVU-BOT: Goodbye", nom, "! See you soon.")

            break

    # Appel de la fonction
        reponse, derniere_intention = repondre(question, langue)

    # Affichage de la reponse
        print("AVU-BOT:", reponse)

        if langue == "fr":
            print("Intention reconnue :", derniere_intention)
        else:
            print("Recognized intent:", derniere_intention)
