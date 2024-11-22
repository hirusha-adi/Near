import sys
from pocketbase import PocketBase
from pocketbase.services.record_service import RecordService
from loguru import logger

DB_URL: str = "http://127.0.0.1:8090"
POCKETBASE_AUTH_EMAIL: str = "hirushaadi@gmail.com"
POCKETBASE_AUTH_PASSWORD: str = "11111111"

conn = PocketBase(DB_URL)

# Authentication
user_data = conn.collection("users").auth_with_password(
    POCKETBASE_AUTH_EMAIL, POCKETBASE_AUTH_PASSWORD
)
if not(user_data.is_valid):
    sys.exit("Unable to authenticate with Pocketbase!")
logger.success(f"Database authentication successful! Logged in as {user_data.record.id} ({user_data.record.name} - {user_data.record.email})")


record = conn.collection('settings_embeds').get_full_list(query_params={"filter": f'key~"thumbnail_"'})
print(record)
print(type(record))