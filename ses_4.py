# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode: 
# ○ __init__ : instanțiem numărător și numitor 
# ○ __str__  : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea 
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea 
# ○ inverse: returnează o nouă fracție (inversa fracției)

# 4 / 5 + 6 / 7 = (4 * 7 + 6 * 5) / (5 * 7) = 58 / 35
# 4 / 5 - 6 / 7 = (4 * 7 - 6 * 5) / (5 * 7) = - 2 / 35

class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor
    
    def __str__(self) -> str:
        return f'{self.numarator} / {self.numitor}'
    
    def __add__(self, alta) -> str:
        new_numarator = self.numarator * alta.numitor + alta.numarator * self.numitor
        new_numitor = self.numitor * alta.numitor
        return f'{new_numarator} / {new_numitor}'
    
    def __sub__(self, alta) -> str:
        new_numarator = self.numarator * alta.numitor - alta.numarator * self.numitor
        new_numitor = self.numitor * alta.numitor
        return f'{new_numarator} / {new_numitor}'
    
    def inversa(self):
        return f'{self.numitor} / {self.numarator}'
        
    
fr = Fractie(4, 5)
fr2 = Fractie(6, 7)
print(fr)

print(fr.__add__(fr2))
print(fr.__sub__(fr2))
print(fr.inversa())