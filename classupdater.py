from urllib.request import urlopen
from pathlib import Path
import json, wget, os, shutil
import arcdps


class AddonUpdater:
    def __init__(self, name, url, version="0", status = "disabled"):
        self.name = name
        self.url = url
        self.version = version
        self.status = status
        if self.name != "arcdps":
            version = self.getversion()
            self.latestversion = version[0]
            self.downloadurl = version[1]
            self.zipname = version[2]
        
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
        wget.download(self.downloadurl)
        filename = shutil.unpack_archive(self.zipname, os.path.join(currentdir, ".tmp", self.name))
        os.remove(self.zipname)
        
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
        else:
            gw2radial.fn = "d3d9.dll"
            arcdps.fn = "d3d9.dll"
            d9vk.fn = "d3d9.dll"
        
        
    
  

currentdir = Path(__file__).parent.absolute()    
d9vk = AddonUpdater("d9vk", "https://api.github.com/repos/Joshua-Ashton/d9vk/releases")
gw2radial = AddonUpdater("gw2radial", "https://api.github.com/repos/Friendly0Fire/GW2Radial/releases")
arcdps = AddonUpdater("arcdps", "https://www.deltaconnected.com/arcdps/x64/d3d9.dll")
d9vk.unpack()