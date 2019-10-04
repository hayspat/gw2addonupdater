import os, sys, requests, hashlib, wget


def bin64():
    if not os.path.exists(os.path.join(gw2path, "bin64")):
        os.mkdir('./bin64')
        
def getversion():
    content = requests.get('https://www.deltaconnected.com/arcdps/x64/d3d9.dll.md5sum')
    # Dosya indirilirken sorun çıktıysa hata ver.
    try:
        content.raise_for_status()
    except Exception as exc:
        print('Bir hata oluştu: %s' % (exc))
    md5 = content.text[:32] # İndirilien dosyayı .text ile texte dönüştür. Md5 herzaman 32 karakterdir. indirilen dosyadan ilk 32 karakteri al.
    return md5

def comparemd5():
    arcpath = os.path.join(gw2path, "bin64", 'd3d9.dll')
    if os.path.isfile(arcpath): #Arcdps dosyası bulunduysa md5 i karşılaştır, uyuşmuyorsa güncelle.
        f = open(arcpath, "rb")
        bytes = f.read() # read file as bytes
        checkmd5 = hashlib.md5(bytes).hexdigest()
        latestmd5 = getversion()
        if str(latestmd5) == str(checkmd5):
            return "Güncel"
        
        


