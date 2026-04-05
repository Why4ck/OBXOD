import shutil
import os
from pathlib import Path

def __extract():
    shutil.unpack_archive("zapret.zip", "zapret")
    files = os.listdir('zapret')
    zp_path = Path(f"zapret/{files[0]}")
    return zp_path

def read():
    z = os.listdir()
    
    
    if "zapret" in z:
        zz = os.listdir('zapret')
        
        for item in zz:
            if "zapret" in item:
                path = Path(f"zapret/{item}")
                return path
    else:
        path_2 = __extract()
        return path_2