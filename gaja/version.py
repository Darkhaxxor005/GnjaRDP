import pkg_resources
from impacket import __path__


try:
    version = pkg_resources.get_distribution('impacket').version
except pkg_resources.DistributionNotFound:
    version = "?"
    print("Cannot determine RDP version. "
          "If running from source you should at least run \"python setup.py egg_info\"")
BANNER = ('''


  /$$$$$$                                    /$$$$$$$  /$$$$$$$  /$$$$$$$ 
 /$$__  $$                                  | $$__  $$| $$__  $$| $$__  $$
| $$  \__/  /$$$$$$  /$$$$$$$  /$$  /$$$$$$ | $$  \ $$| $$  \ $$| $$  \ $$
| $$ /$$$$ |____  $$| $$__  $$|__/ |____  $$| $$$$$$$/| $$  | $$| $$$$$$$/
| $$|_  $$  /$$$$$$$| $$  \ $$ /$$  /$$$$$$$| $$__  $$| $$  | $$| $$____/ 
| $$  \ $$ /$$__  $$| $$  | $$| $$ /$$__  $$| $$  \ $$| $$  | $$| $$      
|  $$$$$$/|  $$$$$$$| $$  | $$| $$|  $$$$$$$| $$  | $$| $$$$$$$/| $$      
 \______/  \_______/|__/  |__/| $$ \_______/|__/  |__/|_______/ |__/      
                         /$$  | $$                                        
                        |  $$$$$$/     version{}                                   
                         \______/                                         



\n''').format(version)

def getInstallationPath():
    return 'RDP Library Installation Path: {}'.format(__path__[0])
