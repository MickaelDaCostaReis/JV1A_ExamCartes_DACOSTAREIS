class Carte:
    def __init__(self, coutEnMana, nom, description, type):
        self.__mana=coutEnMana
        self.__nom=nom
        self.__desc=description
        self.__type=type    #Détermine le type de la carte jouée

    def getDesc(self):
        return self.__desc
    def getNom(self):
        return self.__nom
    def getType(self):
        return self.__type
    def getCout(self):
        return self.__mana

class Mage:
    def __init__(self,nom,pointsDeVie=30,manaMax=10) -> None:
        self.__nom=nom
        self.__PVs=pointsDeVie
        self.__manaMax=manaMax   
        self.__mana=manaMax
        self.__main=[]
        self.__defausse=[]
        self.__zoneDeJeu=[]
        self.__type="Mage"
    # GET/SET
    def getNom(self):
        return self.__nom
    def getMana(self):
        return self.__mana
    def setMana(self,valeur):
        self.__mana=valeur
    def getPV(self):
        return self.__PVs    
    def setmanaMax(self, manaMax):
        self.__manaMax=manaMax
    def getmanaMax(self):
        return self.__manaMax
    def addCarte(self,carte):
        self.__main.append(carte)
    def getType(self):
        return self.__type
    #  AFFICHAGES
    def afficheMain(self):
        if(len(self.__main)==0):
            print("Votre main est vide")  
        else:
            print("Votre main :")
            for i in range(len(self.__main)):
                print(f"({self.__main[i].getNom()})")
    def afficheZoneDeJeu(self):
        if(len(self.__zoneDeJeu)==0):
            print("Votre zone de jeu est vide")  
        else:
            print("Votre zone de jeu :") 
            for i in range(len(self.__zoneDeJeu)):
                print(f"({self.__zoneDeJeu[i].getNom()})")
    def afficheDefausse(self):
        if(len(self.__defausse)==0):
            print("Votre défausse est vide")  
        else:
            print("Votre défausse :")
            for i in range(len(self.__defausse)):
                print(f"({self.__defausse[i].getNom()})")
    def afficheManas(self):
        print(f"Mana : {self.__mana}/{self.__manaMax}")
    # ACTIONS       
    def jouer(self, index):
        if(self.getMana()>=self.__main[index].getCout()):
            self.setMana((self.getMana())-(self.__main[index].getCout()))
            if(self.__main[index].getType()=="Cristal"):
                self.__main[index].augmenteManaMax(self)
                self.__zoneDeJeu.append(self.__main.pop(index))
            elif(self.__main[index].getType()=="Créature"):
                self.__zoneDeJeu.append(self.__main.pop(index))
            elif(self.__main[index].getType()=="Blast"):
                self.__defausse.append(self.__main.pop(index))         
        else:
            print("Vous n'avez pas assez de mana.")
            return 0
    def recupMana(self):
        self.setMana(self.__manaMax)
    def attaquer(self, IndexCreature, ennemi): 
        if(ennemi.getType()=="Créature"):
            self.__zoneDeJeu[IndexCreature].attaquer(ennemi)
            if(self.__zoneDeJeu[IndexCreature].mourir()):
                self.__defausse.append(self.__zoneDeJeu.pop(IndexCreature))
                # Pour la créature ennemi ????????????????
        else:
            self.__zoneDeJeu[IndexCreature].attaquer(ennemi)


class Cristal(Carte):
    def __init__(self, coutEnMana, nom, description, valeur):
        super().__init__(coutEnMana, nom, description, type="Cristal")
        self.__valeur=valeur
    def augmenteManaMax(self, target):
        target.setmanaMax(target.getmanaMax()+self.__valeur)


class Creature(Carte):
    def __init__(self, coutEnMana, nom, description, pointsDeVie, ScoreATK):
        super().__init__(coutEnMana, nom, description, type="Créature")
        self.__PVs=pointsDeVie
        self.__atk=ScoreATK
    def getATK(self):
        return self.__atk
    def getPV(self):
        return self.__PVs
    def setPV(self,nvPV):
        self.__PVs=nvPV
    def affichePV(self):
        print(self.__PVs)

    def mourir(self):                 
        if(self.__PVs<=0):
            return True
        return False
    def attaquer(self,target):
        if(target.getType()=="Créature"):
            self.__PVs=self.__PVs-target.getATK()
            target.setPV(target.getPV()-self.__atk)
        else:
            target.setPV(target.getPV()-self.__atk)
            if(target.getPV()<=0):
                print(f"{target.getName()} est mort.")


class Blast(Carte):
    def __init__(self, coutEnMana, nom, description, valeur):
        super().__init__(coutEnMana, nom, description, type="Blast")
        self.__valeur=valeur
    

blast=Blast(5,"Boule De Feu","lance une boule de feu",2)
crea=Creature(4,"Bob","Juste Bob.",5,5)
crea2=Creature(5,"La mère de Bob","Juste la mère de Bob",400,400)
crist=Cristal(1,"Crystal qui coute 1","Donne 1 cristal de mana supplémentaire",1)
Moi=Mage("BGdeLaStreet")
Moi.addCarte(blast)
Moi.addCarte(crist)
Moi.afficheMain()
Moi.afficheManas()
Moi.afficheDefausse()
Moi.jouer(1)
Moi.afficheMain()
Moi.afficheDefausse()
Moi.afficheManas()
Moi.recupMana()
Moi.afficheManas()