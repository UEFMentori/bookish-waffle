class Ostoskori:
    def __init__(self, alkusumma):
        self.summa = alkusumma
        self.koodi = ""

    def lisaa_koodi(self, koodi):
        self.koodi = koodi

    def laske_hinta(self):
        #ALE10 antaa 10% alennuksen, jos summa on yli 50 euroa
        if self.summa >= 50 and self.koodi == "ALE10":
            return self.summa * 0.9
        return self.summa


#python kommentti