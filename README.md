# BeautifulSoup Kullanarak E-kitap/PDF indirme Uygulaması
Bu proje,BeaitufulSoup kütüphanesini kullanarak web içerikli pdf dosyalarını indirmeye yarar.

Gereksinimler:
Bu proje için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:
-requests
-beautifulsoup4

Kullanım
e-kitap.py dosyasını bir metin düzenleyici veya IDE ile açın.
İndirmek istediğiniz e-kitabın bulunduğu URL'yi url değişkenine atayın:
url = "https://www.example.com/ebook-page"
Python dosyasını çalıştırın:
python e-kitap.py

Dikkat Edilmesi Gerekenler:
İndirmek istediğiniz web sayfasının HTML yapısına bağlı olarak, indirme bağlantısını bulmak için soup.find() metodundaki arama kriterlerini güncellemeniz gerekebilir.
