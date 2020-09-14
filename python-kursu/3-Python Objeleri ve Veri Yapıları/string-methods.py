# ayrıntılı bilgi: https://www.w3schools.com/python/ref_string_capitalize.asp
message = ' Hello There. My name is Sadık Turan '
message = message.split()

"""
message = message.upper()            #Karakterleri Büyük Harfe Çevirir
message = message.lower()            #karakterleri Küçük harfe çevirir
message = message.title()            #cümlenin ilk kelimelerini büyük yapar
message = message.capitalize()       #sadece cümlenin başını büyük harf yapar

message = message.strip()            # Baştaki ve sondaki Boşlukları siler
message = message.split()            # Yazıyı boşluk ile birbirinden ayırır. Kelimeler   ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
message = message.split('.')         # Yazıyı . ile birbirinden ayır. Cümleleri bulur
message= '---'.join(message)         # Ayırdıklarını  --- ile birleştir örn: Hello---There---My

index = message.find('Sadık')        # 'Sadık' kelimesini ara
isFound = message.startswith('H')    # Yazı 'H' ile mi başlıyor
isFound = message.endswith('n')      # Yazı 'n' ile mi bitiyor

message = message.replace('Sadık','Çınar')         # 'Sadık' kelimesini 'Çınar' olarak değiştir
message = message.replace('ç','c')                 # 'ç' harfini 'c' olarak değiştir
#                  .replace('ö','o')               # 'ö' Harfini 'o' olarak değiştir.
#                  .replace(' ','-')               # Boşlıkları '-' olarak değiştir.


#message = message.center(50,'*')                  # 50 karakterlik alan oluştur * ile ve yazıyı ortalar.
"""

print(message)