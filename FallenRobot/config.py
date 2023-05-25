class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20765181
    API_HASH = "e8ec2b740ac91dfce31faa3ef654d1a4"

    CASH_API_KEY = "UU8GRMFH5BHIPW7U"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://zsnbfxaj:qUWKq8E8AMVtjtt88nNr3Gd6_FwhGCLj@mahmud.db.elephantsql.com/zsnbfxaj"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001845855602)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://veysi7074:UTNs8dpY4Fn28mAY@cluster0.nigbbzs.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = ""

    SUPPORT_CHAT = "dolunaydestek"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5777935476:AAHodSw_RfGGbAVqBRm_jX597HlznhO7mBw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "wget -N monitoring.platform360.io/agent360.sh && bash agent360.sh 6419a758575ecc59860d6f97"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5894454190  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS =  5894454190 # User id of sudo users
    DEV_USERS =  5894454190 # User id of dev users
    DEMONS =  5894454190 # User id of support users
    TIGERS =  5894454190 # User id of tiger users
    WOLVES =  5894454190 # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
