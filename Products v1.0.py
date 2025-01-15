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
            print(f"Le prix total : {prix_total}\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
        else:
            print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
        poids_total = self.poids * self.quantite_stock
        print(f"\nProduit Physique: {self.nom},\nPrix: {self.prix}€,\nQuantité en stock: {self.quantite_stock},\nPoids total: {poids_total}kg")

class ProduitNumerique(Produit, Vente):
    def __init__(self, nom, prix, quantite_stock, version):
        super().__init__(nom, prix, quantite_stock)
        self.version = version

    def vendre(self, quantite_vendue):
        if quantite_vendue <= self.quantite_stock:
            self.quantite_stock -= quantite_vendue
            prix_total = quantite_vendue * self.prix
            print(f"\nLe prix Total est: {prix_total}\nVente de {quantite_vendue} {self.nom} effectuée.\nNouvelle quantité en stock: {self.quantite_stock}")
        else:
            print(f"Quantité insuffisante en stock pour la vente de {quantite_vendue} {self.nom}.")

    def afficher_details(self):
        print(f"Produit Numérique: {self.nom}, Prix: {self.prix}€, Quantité en stock: {self.quantite_stock}, Version: {self.version}")

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
        else:
            print(f"Le produit {produit.nom} n'est pas en stock.")

    def afficher_stock(self):
        if not self.produits_en_stock:
            print("Le stock est vide.")
        else:
            print("Contenu du stock :")
            for produit in self.produits_en_stock:
                produit.afficher_details()

# Initialisation du stock
stock = Stock()

while True:
    print("\nMenu :")
    print("1. Ajouter un produit au stock")
    print("2. Vendre un produit")
    print("3. Afficher le stock")
    print("4. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        nom = input("Nom du produit : ")
        prix = float(input("Prix du produit : "))
        quantite_stock = int(input("Quantité en stock : "))
        type_produit = input("Type de produit (Physique/Numérique) : ")
        if type_produit.lower() == "physique":
            poids = float(input("Poids du produit en kg: "))
            produit = ProduitPhysic(nom, prix, quantite_stock, poids)
        elif type_produit.lower() == "numerique":
            version = input("Version du produit : ")
            produit = ProduitNumerique(nom, prix, quantite_stock, version)
        else:
            print("Type de produit non valide.")
            continue
        stock.ajouter_produit(produit)

    elif choix == "2":
        nom_produit = input("Nom du produit à vendre : ")
        quantite_vendue = int(input("Quantité à vendre : "))
        produit_a_vendre = None
        for produit in stock.produits_en_stock:
            if produit.nom == nom_produit:
                produit_a_vendre = produit
                break
        if produit_a_vendre:
            stock.vendre_produit(produit_a_vendre, quantite_vendue)
        else:
            print(f"Le produit {nom_produit} n'est pas en stock.")

    elif choix == "3":
        stock.afficher_stock()

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
