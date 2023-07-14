import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23104044"))
    API_HASH = os.environ.get("API_HASH", "f02a56885f32a83417b2b266d18473a8")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6327144227:AAE7EkSQS-HN5d4-bI8KJTrAF1UBBhfq51s")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5980613692")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://fsclecture:yuvraj178@cluster0.rt7bwpq.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "fsclecture")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQFgiiwAX5BppSEOTBDaTyCdeHDapfB2XEN7kvs0A-_X6VdOpPLMCXlGjijNgw4c2LkxO0VsbBxeyYXlC8PuevAJV3AX3tTLikp58HdJaEKYcehII6gcZBv6VH5dLbCcwVSZ03U4FQoSZ9UKRb4XCKjSnaQEmA-naVUhgzrfhaeh58UsofVL-atWeXl2GwQ6Nyjnk27q6ueZQj8qz1_ECIZArHtKGbx3xhS8TQs3Oob5SMGFCGo3tVunkg_KD12WpeyodTxw-VffHEp_dBuYshEqOu02IaRYEtouIG4MvkhRFgQ4Lvhk4azS-tcwg8yAH1Zy8-bPCXz7Hl374uJMYUUj5jUxJQAAAAF8H9juAQ")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001891823505"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Forward_infinity_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
