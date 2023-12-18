from abc import ABC, abstractmethod

class Composition:
    def __init__(self, xprod, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def getXprod(self):
        return self.__produit

    @property
    def setquantite(self):
        return self.__quantite

from abc import ABC, abstractmethod
class Produit():
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def getnom(self):
        return self.__nom

    @property
    def getcode(self):
        return self.__code

    @abstractmethod
    def getPrixHT(self):
        pass


class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"Produit élémentaire {self.nom} ({self.code}) - Prix d'achat : {self.__prixAchat}"

    def getPrixHT(self):
        return self.__prixAchat


class ProduitCompose(Produit):
    tauxTVA = 0.18

    def __init__(self, nom, code, fraisFabrication, listeConstituants):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants

    @property
    def fraisFabrication(self):
        return self.__fraisFabrication

    @property
    def listeConstituants(self):
        return self.__listeConstituants

    def __str__(self):
        return f"Produit composé {self.nom} ({self.code}) - Frais de fabrication : {self.__fraisFabrication}"

    


# Test
p1 = ProduitElementaire("P1", "455s", 8)
p2 = ProduitElementaire("P2", "002", 9)

comp1 = Composition(p1, 6)
comp2 = Composition(p2, 8)

p3 = ProduitCompose("P3", "00t3", 9, [comp1, comp2])

print(p1)
print(p2)
print(p3)

