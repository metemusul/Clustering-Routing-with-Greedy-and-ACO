Clustering & Routing with Greedy and ACO

 Proje Amacı
Bu projede, rastgele üretilmiş koordinatlar üzerinde kümeleme (clustering) ve her küme için rota planlaması (route optimization) yapılmıştır. Uygulamanın amacı, belirli bir başlangıç noktasından başlayarak tüm noktaları dolaşıp tekrar başlangıç noktasına dönen en kısa turu (TSP - Gezgin Satıcı Problemi) oluşturmaktır.

 Kullanılan Yöntemler
1. K-means Clustering
Koordinatlar, KMeans algoritması ile 3 kümeye ayrılmıştır.

Her kümenin merkez noktası (centroid), o kümenin başlangıç noktası olarak belirlenmiştir.

2. Greedy Algorithm (Açgözlü Algoritma)
Her küme için bir greedy tabanlı TSP çözümü uygulanmıştır.

Algoritma, mevcut konuma en yakın komşuyu seçerek sırayla ilerler ve en sonunda başlangıç noktasına döner.

Hızlı ve basit bir yöntemdir ancak her zaman en kısa rotayı bulmaz.

Oluşturulan rotalar greedy_cikti/ klasörüne .png olarak kaydedilmiştir.

3. Ant Colony Optimization (ACO)
Her küme için ACO algoritmasıyla daha akıllı bir TSP çözümü uygulanmıştır.

ACO, karıncaların feromon izlerini kullanarak optimal rotaları keşfetmesini simüle eder.

Parametreler:

n_ants=20: 20 karınca

n_best=5: En iyi 5 karıncanın feromon izi artırılır

n_iterations=100: 100 iterasyon

alpha=1, beta=2: Feromon vs mesafe etkisi

decay=0.05: Feromon buharlaşma oranı

Genellikle greedy algoritmasından daha iyi çözümler üretir.

Sonuç görselleri aco_cikti/ klasörüne .png olarak kaydedilmiştir.

 Sonuçların Karşılaştırması
Kriter                  Greedy Algoritması	Ant Colony Optimization (ACO)
Hız                     Çok hızlı	        Daha yavaş
Optimizasyon Kalitesi	Genellikle alt-optimal   	Genellikle daha iyi rotalar
Yapısı	                 Deterministik	      Stokastik (tesadüfi + öğrenme)
Öğrenme Yetisi	        Yok	                   Var (feromon ile öğrenme)
Küçük Veri Seti	         Tatmin edici	    Daha iyi performans
Büyük Veri Seti	          Performansı zayıflar   	Daha uygun ama zaman maliyeti artar



ACO algoritmasında olası "divide by zero" hatalarına karşı sıfır mesafeleri önleyen koruma eklidir.

Greedy çözüm rotaları daha kısa sürede elde edilir, ancak bazen tur rotasında geri dönüşler görülebilir.

ACO çözümleri genellikle daha düzgün ve verimli rotalar çizer.