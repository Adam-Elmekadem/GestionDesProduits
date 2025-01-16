from abc import ABC, abstractmethod

class Produit(ABC):
    def __init__(self, nom, prix, quantite_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_stock = quantite_stock

    @abstractmethod
    def afficher_details(self):
        pass

class Vente(ABC):
    @abstractmethod
    def vendre(self, quantite_vendue: int):
        pass

class ProduitPhysic(Produit, Vente):
    def __init__(self, nom, prix, quantite_stock, poids):
        super().__init__(nom, prix, quantite_stock)
        self.poids = poids

    def vendre(self, quantite_vendue):
        if quantite_vendue <= self.quantite_stock:
            self.quantite_stock -= quantite_vendue
            prix_total = quantite_vendue * self.prix
            print(f"Le prix total : {prix_total}DH\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
        else:
            print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
        poids_total = self.poids * self.quantite_stock
        print(f"\nProduit Physique: {self.nom},\nPrix: {self.prix}DH,\nQuantité en stock: {self.quantite_stock},\nPoids total: {poids_total}kg")

class Pc(ProduitPhysic):
    def __init__(self, nom, prix, quantite_stock, poids, marque, processeur, taille_ecran):
        super().__init__(nom, prix, quantite_stock, poids)
        self.marque = marque
        self.processeur = processeur
        self.taille_ecran = taille_ecran

    def vendre(self, quantite_vendue):
        if quantite_vendue <= self.quantite_stock:
            self.quantite_stock -= quantite_vendue
            prix_total = quantite_vendue * self.prix
            print(f"Le prix total : {prix_total}DH\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
        else:
            print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
        poids_total = self.poids * self.quantite_stock
        print(f"\nPc: {self.nom},\nPrix: {self.prix}DH,\nQuantité en stock: {self.quantite_stock},\nPoids total: {poids_total}kg,\nMarque: {self.marque},\nProcesseur: {self.processeur},\nTaille de l'écran: {self.taille_ecran}Pouce")

class Smartphone(Pc):
    def __init__(self, nom, prix, quantite_stock, poids, marque, processeur, taille_ecran, ram , camera):
        super().__init__(nom, prix, quantite_stock, poids, marque, processeur, taille_ecran)
        self.ram = ram
        self.camera = camera

    def vendre(self, quantite_vendue):
        if quantite_vendue <= self.quantite_stock:
            self.quantite_stock -= quantite_vendue
            prix_total = quantite_vendue * self.prix
            print(f"\nLe prix Total est: {prix_total}DH\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
        else:
            print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

        def afficher_details(self):
            poids_total = self.poids * self.quantite_stock
            print(f"\nSmartphone: {self.nom},\nPrix: {self.prix}DH,\nQuantité en stock: {self.quantite_stock},\nPoids total: {poids_total}kg,\nMarque: {self.marque},\nProcesseur: {self.processeur},\nTaille de l'écran: {self.taille_ecran}Pouce,\nRAM: {self.ram}gb,\nCamera: {self.camera}Mpx")


class ProduitNumerique(Produit, Vente):
    def __init__(self, nom, prix, quantite_stock, version):
        super().__init__(nom, prix, quantite_stock)
        self.version = version

    def vendre(self, quantite_vendue):
        if quantite_vendue <= self.quantite_stock:
            self.quantite_stock -= quantite_vendue
            prix_total = quantite_vendue * self.prix
            print(f"\nLe prix Total est: {prix_total}DH\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
        else:
            print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
        print(f"Produit Numérique: {self.nom}, Prix: {self.prix}€, Quantité en stock: {self.quantite_stock}, Version: {self.version}")

class Logiciel(ProduitNumerique):
    def __init__(self, nom, prix, quantite_stock, version, type_logiciel):
        super().__init__(nom, prix, quantite_stock, version)
        self.type_logiciel = type_logiciel

    def vendre(self, quantite_vendue):
            if quantite_vendue <= self.quantite_stock:
                self.quantite_stock -= quantite_vendue
                prix_total = quantite_vendue * self.prix
                print(f"\nLe prix Total est: {prix_total}DH\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
            else:
                print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
            print(f"Logiciel: {self.nom}, Prix: {self.prix}€, Quantité en stock: {self.quantite_stock}, Version: {self.version}, Type: {self.type_logiciel}")

class JeuxVideo(ProduitNumerique):
    def __init__(self, nom, prix, quantite_stock, version, genre):
        super().__init__(nom, prix, quantite_stock, version)
        self.genre = genre

    def vendre(self, quantite_vendue):
            if quantite_vendue <= self.quantite_stock:
                self.quantite_stock -= quantite_vendue
                prix_total = quantite_vendue * self.prix
                print(f"\nLe prix Total est: {prix_total}DH\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
            else:
                print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
            print(f"Jeux Vidéo: {self.nom}, Prix: {self.prix}€, Quantité en stock: {self.quantite_stock}, Version: {self.version}, Genre: {self.genre}")
class Stock:
    def __init__(self):
        self.produits_en_stock = []

    def ajouter_produit(self, produit):
        if produit not in self.produits_en_stock:
            self.produits_en_stock.append(produit)
            print(f"Le produit {produit.nom} a été ajouté au stock.")
        else:
            print(f"Le produit {produit.nom} est déjà dans le stock.")

    def vendre_produit(self, produit, quantite_vendue):
        if produit in self.produits_en_stock:
            produit.vendre(quantite_vendue)
            if produit.quantite_stock == 0:
                self.produits_en_stock.remove(produit)
                print(f"Le produit {produit.nom} a été retiré du stock car il n'y a plus d'exemplaires en stock.")
        else:
            print(f"Le produit {produit.nom} n'est pas en stock.")

    def afficher_stock(self):
        if not self.produits_en_stock:
            print("Le stock est vide.")
        else:
            print("Contenu du stock :")
            for produit in self.produits_en_stock:
                produit.afficher_details()

def main():
    while True:
        print("\n----Menu:----")
        print("1. Ajouter un produit au stock")
        print("2. Afficher le stock")
        print("3. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            while True:
                print("\n----Ajouter un produit au stock----")
                print("1. Ajouter un produit physique")
                print("2. Ajouter un produit numérique")
                print("3. Retour au menu principal")

                choix_ajout = input("Choisissez une option : ")

                if choix_ajout == "1":
                    ajouter_produit_physique()
                elif choix_ajout == "2":
                    ajouter_produit_numerique() 
                elif choix_ajout == "3":
                    print("Retour au menu principal.")
                    break 
                else:
                    print("Option invalide. Veuillez choisir une option valide.")

        elif choix == "2":
            stock.afficher_stock()

        elif choix == "3":
            print("Au revoir !")
            break 

        else:
            print("Option invalide. Veuillez choisir une option valide.")


def ajouter_produit_physique():
    while True:
        print("\n----Ajouter un produit physique----")
        print("1. Ajouter un PC")
        print("2. Ajouter un smartphone")
        print("3. Retour au menu précédent")

        choix_ajout_produit = input("Choisissez une option : ")
        if choix_ajout_produit == "1":
            # Logic to add a PC
            nom = input("Nom du pc : ")
            prix = float(input("Prix du pc : "))
            quantite_stock = int(input("Quantité en stock : "))
            poids = float(input("Poids du pc en kg: "))
            marque = input("Marque du pc : ")
            processeur = input("Processeur du pc : ")
            taille_ecran = float(input("Taille de l'écran du pc en pouces : "))
            pc = Pc(nom, prix, quantite_stock, poids, marque, processeur, taille_ecran)
            stock.ajouter_produit(pc)
            print("Ajout d'un PC.")

        elif choix_ajout_produit == "2":
            # Logic to add a smartphone
            nom = input("Nom du smartphone : ")
            prix = float(input("Prix du smartphone : "))
            quantite_stock = int(input("Quantité en stock : "))
            poids = float(input("Poids du smartphone en kg: "))
            marque = input("Marque du smartphone : ")
            processeur = input("Processeur du smartphone : ")
            taille_ecran = float(input("Taille de l'écran du smartphone en pouces : "))
            ram = int(input("RAM du smartphone en GB : "))
            camera = int(input("Camera du smartphone en Mpx : "))
            smartphone = Smartphone(nom, prix, quantite_stock, poids, marque, processeur, taille_ecran, ram, camera)
            stock.ajouter_produit(smartphone)
            print("Ajout d'un smartphone.")

        elif choix_ajout_produit == "3":
            print("Retour au menu précédent.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


def ajouter_produit_numerique():
    while True:
        print("\n----Ajouter un produit numérique----")
        print("1. Ajouter un logiciel")
        print("2. Ajouter un jeu vidéo")
        print("3. Retour au menu précédent")

        choix_ajout_produit = input("Choisissez une option : ")
        if choix_ajout_produit == "1":
            # Logic to add a software
            nom = input("Nom du logiciel : ")
            prix = float(input("Prix du logiciel : "))
            quantite_stock = int(input("Quantité en stock : "))
            version = input("Version du logiciel : ")
            genre = input("Genre du logiciel : ")
            logiciel = Logiciel(nom, prix, quantite_stock, version, genre)
            stock.ajouter_produit(logiciel)
            print("Ajout d'un logiciel.")

        elif choix_ajout_produit == "2":
            # Logic to add a video game
            nom = input("Nom du jeu vidéo : ")
            prix = float(input("Prix du jeu vidéo : "))
            quantite_stock = int(input("Quantité en stock : "))
            version = input("Version du jeu vidéo : ")
            genre = input("Genre du jeu vidéo : ")
            jeu_video = JeuxVideo(nom, prix, quantite_stock, version, genre)
            stock.ajouter_produit(jeu_video)
            print("Ajout d'un jeu vidéo.")

        elif choix_ajout_produit == "3":
            print("Retour au menu précédent.")
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")


# Initialize stock object
stock = Stock()
main()
