#!/usr/bin/python3
import os, sys, requests, hashlib, wget
print('Guild Wars 2 klasörünün olduğu dizini girin:')
# Gw2 klasörünü gir, öyle bir klasör yoksa doğru girilene kadar loopta kal.
def checkpath():
    global folderpath
    folderpath = input()
    while os.path.exists(folderpath) == False:
        print('Böyle bir dizin yok, yeniden dizin girin.')
        folderpath = input()
checkpath()
os.chdir(os.path.join(folderpath)) # Çalışma dizinini değiştir.

# bin64 klasörü var mı kontrol et yoksa oluştur.
def bin64():
    if os.path.exists('./bin64') == False:
        os.mkdir('./bin64')
bin64()        
os.chdir(os.path.join(folderpath, "bin64")) # Çalışma klasörünü bin64 e al.
#md5 dosyasını indir
content = requests.get('https://www.deltaconnected.com/arcdps/x64/d3d9.dll.md5sum')
# Dosya indirilirken sorun çıktıysa hata ver.
try:
    content.raise_for_status()
except Exception as exc:
    print('Bir hata oluştu: %s' % (exc))
md5 = content.text[:32] # İndirilien dosyayı .text ile texte dönüştür. Md5 herzaman 32 karakterdir. indirilen dosyadan ilk 32 karakteri al.
arcpath = os.path.join(folderpath, "bin64", 'd3d9.dll')
def update():
    if os.path.isfile(os.path.join(arcpath)) == True: #Arcdps dosyası bulunduysa md5 i karşılaştır, uyuşmuyorsa güncelle.
        f = open(arcpath, "rb")
        bytes = f.read() # read file as bytes
        checkmd5 = hashlib.md5(bytes).hexdigest()
        if str(md5) == str(checkmd5):
            print("ArcDPS güncel")
        else:
            print('ArcDPS güncelleniyor.')
            os.remove(arcpath)
            wget.download("https://www.deltaconnected.com/arcdps/x64/d3d9.dll", arcpath)
    else:
        print("Sistemde ArcDPS bulunamadı, indiriliyor.")
        wget.download("https://www.deltaconnected.com/arcdps/x64/d3d9.dll", arcpath)
update()

#md5 değerlerini doğrula.