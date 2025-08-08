import sys
import os
import warnings
from types import ModuleType

# Comprehensive imghdr backport for Python 3.13
if sys.version_info >= (3, 13):
    # Create a robust imghdr module replacement
    def test_jpeg(h, f):
        if h[6:10] in (b'JFIF', b'Exif') or h.startswith(b'\xff\xd8'):
            return 'jpeg'
    
    def test_png(h, f):
        if h.startswith(b'\211PNG\r\n\032\n'):
            return 'png'
    
    def test_gif(h, f):
        if h[:6] in (b'GIF87a', b'GIF89a'):
            return 'gif'
    
    def test_tiff(h, f):
        if h[:2] in (b'MM', b'II'):
            return 'tiff'
    
    def test_bmp(h, f):
        if h.startswith(b'BM'):
            return 'bmp'
    
    def test_webp(h, f):
        if len(h) >= 12 and h.startswith(b'RIFF') and h[8:12] == b'WEBP':
            return 'webp'
    
    def test_exr(h, f):
        if h.startswith(b'\x76\x2f\x31\x01'):
            return 'exr'
    
    def what(file, h=None):
        if h is None:
            if isinstance(file, (str, os.PathLike)):
                with open(file, 'rb') as f:
                    h = f.read(32)
            else:
                loc = file.tell()
                h = file.read(32)
                file.seek(loc)
                
        tests = (test_jpeg, test_png, test_gif, test_tiff, test_bmp, test_webp, test_exr)
        for test_function in tests:
            res = test_function(h, None)
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

# Configure logging to show in render.com console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logging.getLogger("pymongo").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

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
    logger.info("𝙰𝚕𝚙𝚑𝚊 𝚂𝚎𝚜𝚜𝚒𝚘𝚗 𝙶𝚎𝚗 𝚜𝚝𝚊𝚛𝚝𝚒𝚗𝚐...")
    try:
        app.start()
        logger.info("Pyrogram client started successfully")
    except (ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid) as e:
        logger.exception("Authentication failed: ")
        raise
    except Exception as e:
        logger.exception("Fatal error during startup: ")
        raise

    try:
        uname = app.get_me().username
        logger.info(f"@{uname} NOW ALPHA SESSION GEN IS READY TO GEN SESSION")
        idle()
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
    except Exception as e:
        logger.exception("Runtime error: ")
    finally:
        app.stop()
        logger.info("𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐒𝐭𝐨𝐩𝐩𝐞𝐝")
