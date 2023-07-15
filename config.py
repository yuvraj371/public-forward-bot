import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "12327086"))
    API_HASH = os.environ.get("API_HASH", "b9f2b28ac8a9ee7a13d76f224d6a1b62")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6366543585:AAH3qX1_M0W3-SORnG8pVCbaETqna03pYcY")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6310080453")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://krishna:krishna123@cluster1.ohpp83e.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "krishna")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQC8GK4AMKOs3vq06nCudSCqjTUlOWV9qi7V8SWkIGf2CJJS9kYVGYPx71Xd5bzqVT87N_gXgvd9t_zQeRTncifXcC-mrB_cVLl3vfIA4rvSpKwx2bQq1yA0Kx9xFsw9VQ3TBy7nssMhjSTszdzMDMyyE6CxoavkGNtHkrCAxyCkcWik59YKv8xlrzlvFbwodqEitJ-9inJ77uJl5M2eqGEZ3_ccYuaTfGU2aBP7-9w3TTIbC3jhZ4LXNRfY8JHHBxafZm9v7YSrfCA4u4rLeBcOQfq7akpgKM6FjvGHsTJg3ztuRRzhUpluT9ZS3PPl3Ypn6sp9KU4LU1G2KU14JqT1e4ztIgAAAAF4HC_FAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001690922221"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Forward_infinity_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
