import sys
import os
import warnings
from types import ModuleType

# Backport imghdr for Python 3.13+
if sys.version_info >= (3, 13):
    # Create a minimal imghdr module
    def test_jpeg(h, f):
        if h[6:10] in (b'JFIF', b'Exif') or h.startswith(b'\xff\xd8'):
            return 'jpeg'
    
    def test_png(h, f):
        if h.startswith(b'\211PNG\r\n\032\n'):
            return 'png'
    
    def test_gif(h, f):
        if h[:6] in (b'GIF87a', b'GIF89a'):
            return 'gif'
    
    def test_bmp(h, f):
        if h.startswith(b'BM'):
            return 'bmp'
    
    def test_webp(h, f):
        if len(h) >= 12 and h.startswith(b'RIFF') and h[8:12] == b'WEBP':
            return 'webp'
    
    def what(file, h=None):
        if h is None:
            if isinstance(file, (str, os.PathLike)):
                with open(file, 'rb') as f:
                    h = f.read(32)
            else:
                loc = file.tell()
                h = file.read(32)
                file.seek(loc)
        for tf in (test_jpeg, test_png, test_gif, test_bmp, test_webp):
            res = tf(h, None)
            if res:
                return res
        return None

    # Create and inject the module
    imghdr_module = ModuleType('imghdr')
    imghdr_module.what = what
    sys.modules['imghdr'] = imghdr_module
    warnings.warn("Using custom imghdr backport for Python 3.13+", RuntimeWarning)

import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)

# Initialize start time
StartTime = time.time()

# Initialize the Client
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="RAUSHAN"),
)

if __name__ == "__main__":
    print("𝙰𝚕𝚙𝚑𝚊 𝚂𝚎𝚜𝚜𝚒𝚘𝚗 𝙶𝚎𝚗 𝚜𝚝𝚊𝚛𝚝𝚒𝚗𝚐...")
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

    uname = app.get_me().username
    print(f"@{uname} NOW ALPHA SESSION GEN IS READY TO GEN SESSION")
    
    idle()
    
    app.stop()
    print("𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐒𝐭𝐨𝐩𝐩...")
