website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()               # Baş ve sondaki boşlukları sil
result = ' Hello World '.lstrip()              # Sondaki Boşlukları sil. lstrip = leftStrip
result = ' Hello World '.rstrip()              # Baştaki boşlukları sil. RStirp = RightStirp

result = website.lstrip('htp:/')               # Soldan başla htp:/ karakterlerini sil

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = 'www.sadikturan.com'.strip('w.moc')   # Baş ve sondaki "w . m c o" karakterlerini sil

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
result = course.upper()
result = course.title()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')                      # websitesi içinde kaç adet 'a' harfi var
result = website.count('www')                    # Websitesi içinde kaç ader 'www' kelimesi var
result = website.count('www',0,10)               # Websitesinin 0 ile 10. karakterleri arasında kaç adet 'www' var

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result = website.startswith('www')
result = website.startswith('http')
result = website.endswith('com')

# 6-  'website' içinde '.com' ifadesi var mı?
result = website.find('com')                     # 'com' ifadesi yazı dizimizde var mı?
result = website.find('com',0,10)                # 0 ile 10. index arasında 'com' ifadesi var mı?
result = course.find('Python')
result = course.rfind('Python')                  # sağ taraftan 'python' var mı diye arar

result = website.index('com')
result = website.rindex('com')
# result = website.rindex('comm') # exception

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()                        # Harf mi
result = 'Hello'.isalpha()
result = course.isdigit()                        # Rakam mı?
result = '123'.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50, '*')
result = 'Contents'.ljust(50, '*')               # 50 karakterlik dizi oluştur ve bu yazıyı sola yasla
result = 'Contents'.rjust(50, '*')               # 50 karakterlik dizi oluştur ve bu yazıyı sağa yasla

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-')
result = course.replace(' ', '-',5)              # 5 Karakterdeki boşluklar '-' olarak değiştir
result = course.replace(' ', '')                 # Boşlukları sil

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')  # 'world' kelimesini 'there' olarak değiştir.

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')                       # boşluklar ile ayır diziyi. kelimeleri bulur
# result = result[2]
# result = result[5]

#print(result)
