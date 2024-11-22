import sys
from loguru import logger
from pocketbase import PocketBase
from pocketbase.services.record_service import RecordService

POCKETBASE_URL: str = "http://127.0.0.1:8090"
POCKETBASE_AUTH_EMAIL: str = "hirushaadi@gmail.com"
POCKETBASE_AUTH_PASSWORD: str = "11111111"

try:
    conn = PocketBase(POCKETBASE_URL)

    # Authentication
    user_data = conn.collection("users").auth_with_password(
        POCKETBASE_AUTH_EMAIL, POCKETBASE_AUTH_PASSWORD
    )
    if not(user_data.is_valid):
        logger.error("Unable to authenticate with Pocketbase!")
        sys.exit()
    logger.success(f"Database authentication successful! Logged in as {user_data.record.id} ({user_data.record.name} - {user_data.record.email})")

except Exception as e:
    logger.error(f"Unable to connect to Pocketbase! {e}")
    sys.exit()

class Collections:
    def settings_embeds() -> RecordService:
        return conn.collection("settings_embeds")
