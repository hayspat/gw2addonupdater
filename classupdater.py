from urllib.request import urlopen
from pathlib import Path
import json, wget, os, shutil, platform, configparser, requests

def createconfig():
    # Create the configuration file as it doesn't exist yet
    cfgfile = open(inipath, 'w')
    # Add content to the file
    Config = configparser.ConfigParser()
    Config.add_section('arcdps')
    Config.set('arcdps', 'version', '0')
    Config.set('arcdps', 'status', 'disabled')
    Config.add_section('gw2radial')
    Config.set('gw2radial', 'version', '0')
    Config.set('gw2radial', 'status', 'disabled')
    Config.add_section('d9vk')
    Config.set('d9vk', 'version', '0')
    Config.set('d9vk', 'status', 'disabled')
    Config.add_section('path')
    Config.set('path', 'gw2path', "None")
    Config.write(cfgfile)
    cfgfile.close()

def arcgetversion():
    content = requests.get('https://www.deltaconnected.com/arcdps/x64/d3d9.dll.md5sum')
    try:
        content.raise_for_status()
    except Exception as exc:
        print('Bir hata oluştu: %s' % (exc))
    md5 = content.text[:32]
    return md5
    
class AddonUpdater:
    def __init__(self, name, url, version="0", status = "disabled"):
        self.name = name 
        self.url = url
        self.version = parser.get(self.name, 'version')
        self.status = parser.get(self.name, 'status')
        if self.name != "arcdps":
            version = self.getversion()
            self.latestversion = version[0]
            self.downloadurl = version[1]
            self.zipname = version[2]
        else:
            self.latestversion = arcgetversion()
            self.downloadurl = self.url
        
    def getversion(self):  
        with urlopen (self.url) as response:
            source = response.read()
        data = json.loads(source)
        latestversion = data[0]['tag_name']
        downloadurl = data[0]['assets'][0]['browser_download_url']
        zipname = data[0]['assets'][0]['name']
        return latestversion, downloadurl, zipname       
                    
    def unpack(self):
        os.chdir(currentdir)  
        if os.path.exists('./.tmp') == False:
            os.mkdir('./.tmp')
        os.chdir(os.path.join(currentdir, ".tmp"))
        if self.name != "arcdps":
            wget.download(self.downloadurl)
            filename = shutil.unpack_archive(self.zipname, os.path.join(currentdir, ".tmp", self.name))
            os.remove(self.zipname)
        if self.name == "arcdps":
            if os.path.exists('./arcdps') == False:
                os.mkdir('./arcdps')
            os.chdir(os.path.join(currentdir, ".tmp", "arcdps"))
            try:
                os.remove("./d3d9.dll")
            except:
                wget.download(self.downloadurl)

    def setname():
        if (d9vk.status == "enabled") and (arcdps.status == "enabled") and (gw2radial.status == "enabled"):
            arcdps.fn = "d3d9.dll"
            gw2radial.fn = "d3d9_chainload.dll"
            d9vk.fn = "d3d9_mchain.dll"
        elif (d9vk.status == "enabled" and arcdps.status == "enabled") and (gw2radial.status == "disabled"):
            arcdps.fn = "d3d9.dll"
            d9vk.fn = "d3d9_chainload.dll"
            gw2radial.fn = "none"
        elif (d9vk.status  == "enabled" and gw2radial.status == "enabled") and (arcdps.status == "disabled"):
            gw2radial.fn = "d3d9.dll"
            d9vk.fn = "d3d9_chainload.dll"
            arcdps.fn = "none"
        elif (arcdps.status == "enabled" and gw2radial.status == "enabled") and d9vk.status == "disabled":
            arcdps.fn = "d3d9.dll"
            gw2radial.fn = "d3d9_chainload.dll"
            d9vk.fn = "none"
        elif (arcdps.status == "disabled" and gw2radial.status == "disabled") and d9vk.status == "enabled":
            gw2radial.fn = "none"
            arcdps.fn = "none"
            d9vk.fn = "d3d9.dll"
        elif (arcdps.status == "disabled" and d9vk.status == "disabled") and gw2radial.status == "enabled":
            gw2radial.fn = "d3d9.dll"
            arcdps.fn = "none"
            d9vk.fn = "none"
        elif (d9vk.status == "disabled" and gw2radial.status == "disabled") and arcdps.status == "enabled":
            gw2radial.fn = "none"
            arcdps.fn = "d3d9.dll"
            d9vk.fn = "none"
        elif d9vk.status == "disabled" and gw2radial.status == "disabled" and arcdps.status == "disabled":
            gw2radial.fn = "none"
            arcdps.fn = "none"
            d9vk.fn = "none"
        
    def copy(self):
        if os.path.exists(os.path.join(parser["path"]["gw2path"], "bin64")) == False:
            os.mkdir(os.path.join(parser["path"]["gw2path"], "bin64"))
        bindir = os.listdir(os.path.join(parser["path"]["gw2path"], "bin64"))
        for item in bindir:
            if item.startswith("d3d9"):
                os.remove(os.path.join(parser["path"]["gw2path"], "bin64", item))
        for i in [arcdps, gw2radial, d9vk]:
            if i.name == "d9vk":
                dllpath = os.path.join(currentdir, ".tmp", i.name, i.name + "-" + i.latestversion, pla, "d3d9.dll")
            if i.name == "gw2radial":
                dllpath = os.path.join(currentdir, ".tmp", i.name, "d3d9.dll")
            if i.name == "arcdps":
                dllpath = os.path.join(currentdir, ".tmp", i.name, "d3d9.dll")
            if i.fn != "none":
                if os.path.isfile(dllpath):
                    shutil.copy(dllpath, os.path.join(parser["path"]["gw2path"], "bin64", i.fn))
                else:
                    self.unpack()
                    shutil.copy(dllpath, os.path.join(parser["path"]["gw2path"], "bin64", i.fn))

                    
  

currentdir = Path(__file__).parent.absolute()
inipath = os.path.join(currentdir, "settings.ini")
if not os.path.isfile(inipath):
    createconfig()
parser = configparser.ConfigParser()
parser.read(inipath)


    
if platform.architecture()[0] == "64bit":
    pla = "x64"
else:
    pla = "x32"
    
    
d9vk = AddonUpdater("d9vk", "https://api.github.com/repos/Joshua-Ashton/d9vk/releases")
gw2radial = AddonUpdater("gw2radial", "https://api.github.com/repos/Friendly0Fire/GW2Radial/releases")
arcdps = AddonUpdater("arcdps", "https://www.deltaconnected.com/arcdps/x64/d3d9.dll")
