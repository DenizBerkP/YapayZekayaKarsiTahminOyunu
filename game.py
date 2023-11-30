import random
import numpy as np

for level in range(1,10): #Her Seviye İçin Sayıyı 1 Arttır.
    y = [i for i in [random.randint(0, 60 * level) for _ in range(10)]] # 0 ile (60 * Seviye) arasında 10 adet rastgele sayı üret ve y listesine kaydet. 
    X = [2 * level * i + random.randint(-3, 3) for i in y ]  # X listesindeki sayıyı sırayla 2 ile, Seviye ile çarp ve -3 ile +3 arasında bir sayı ekle. X listesine kaydet.
    n = random.randint(0,60) # n = Gelecek sorunun cevabı.
    t = 2 * l * n + random.randint(-3, 3) #t = Gelecek sorunun y değeri. 
    X.append(t) 

    print("Seviye: ", level)
    print("y değerleri:", y)
    print("X değerleri:", X)

    tahmin = int(input("Son X değerine bakarak Y değerini tahmin et:"))

    gercek_X = X[-1]
    gercek_y = n

    if tahmin == gercek_y:
        print("Tebrikler! Doğru tahmin ettiniz.")
        print(f"Gerçek Y değeri: {gercek_y}")

    else:
        print("Üzgünüm, yanlış tahmin ettiniz.")
        print(f"Doğru cevap: {gercek_y}")

    from sklearn.linear_model import LinearRegression 
    X = np.array(X[:-1]).reshape(-1, 1)
    y = np.array(y)

    model = LinearRegression() # Linear Regression modelini oluştur.
    model.fit(X, y)  # Modeli X ve y değerleri ile eğit.

    # Tahmin
    tahmin_n = (model.predict(np.array([[t]]))) # Modele t değerinden n değerini tahmin ettir.

    print(f"Yapay Zekanın Tahmini {tahmin_n[0]}") 
