import json
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION1", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        # ========== 🍪 COOKIES FIX - START ==========
        cookies_str = getenv("COOKIES_URL", "")
        
        # Cookie JSON တိုက်ရိုက်ဖြစ်ရင်
        try:
            self.COOKIES_URL = json.loads(cookies_str)
            print("✅ Cookies loaded from JSON string")
        except:
            # URL ဖြစ်ရင် (batbin, rentry, pastebin စသည်)
            self.COOKIES_URL = [
                url for url in cookies_str.split(" ")
                if url and ("batbin.me" in url or "rentry.co" in url or "pastebin.com" in url)
            ]
            if self.COOKIES_URL:
                print(f"✅ Cookies loaded from URL: {self.COOKIES_URL}")
            else:
                # Default cookie ထည့်ပေးလိုက်တယ်
                self.COOKIES_URL = {
                    "__Secure-3PSIDCC": "AKEyXzVooAXQLbqztV-T1bZR1P3GAzH-dUNhzxCaX-mhg5-Q3aanbb-ejjezozZyulKeC5Kt",
                    "__Secure-3PSIDTS": "sidts-CjUByojQU7aHDsr6xx8Sg8Ol5TPJMIUGdqY9lppYnm--tLzb3pU_ZHDRq1A1zfjiyijxNOP-pxAA",
                    "__Secure-ROLLOUT_TOKEN": "CNOV56zBvZT3vwEQ2OjRgv6YlQMYuvmFg_6YlQM%3D",
                    "__Secure-YNID": "19.YT=WY8diizJX0Y0Mr8caqI-8Aenuy93H5n0MBEZJoT6jrLHEg_uubulfbgyC-IunodtpXZAOIyrTzEBUV3EVGiLuFjs12NzuSYRJxkT3kzUv0FB-cvBQP9imqNb2d7kugWebcuE_qftvKh8T0PvmPyK6QYMHCEpEGsDeI_cFKGVQpQ5uHBJPTnpM8UqhBnBgEmOa8M2H441rME9xcSXzw26Z-68Zjhm570K4gmDBTEI4znKLwYMim7zFII8SAfzvXOPwnnITOhtudjwZw4ntfn4q2U_YO1mZN6Uh_QaYmP-C629wKhXccZoVXsQ6ystwzkTy5R_LvXwsbxDiPs9NSe_lg"
                }
                print("✅ Default cookies applied")
        # ========== 🍪 COOKIES FIX - END ==========

        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
