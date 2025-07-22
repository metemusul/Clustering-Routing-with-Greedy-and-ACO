# koordinat verileri
# STEP 1
# örnek koordinatları tanımlayalım 
# ilk olarak birkac nokta olusturalım bunları rastgelede yapabiliriz örnek veriylede çalışabiliriz


import numpy as np 

def generate_coordinates(n_points = 30, seed= 42):
    np.random.seed(seed)
    return np.random.randint(0,100,size=(n_points,2))