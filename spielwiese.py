class roboter():
    
    def __init__(self, POS, KRI, ATK, DEF):
        self.POS = POS  #POS, die Position. Ein Feld auf der Spielwiese mit den Integerkoordinaten (x,y)
        self.KRI = KRI  #int Anzahl der Kristalle die der Roboter noch übrig hat
        self.ATK = ATK  #Angriffspower als integer
        self.DEF = DEF  #Verteidigungspower als integer
    def gucken(self, POS):
        B1 = POS + (+2,+1) #soll den Status der Felder die zwei vor POS sind abrufen
        B2 = POS + (+2,+0)
        B3 = POS + (+2,-1)
    
    def angriff(self, ATK, DEF):
        pass
    def drehen(self, ROT):
        pass
    def laufen(self, STEP):
        pass
