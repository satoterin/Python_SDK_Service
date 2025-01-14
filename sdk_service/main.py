import os
from dotenv import load_dotenv
from hunter_sdk.service import HunterService

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("HUNTER_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")


def main() -> None:
    """Main function to demonstrate HunterService usage."""
    service = HunterService(API_KEY)
    validation_result = service.validate_email(EMAIL_ADDRESS)
    storage_contents = service.storage.view_storage()
    print("Validation result:", validation_result)
    print("In-Memory Storage:", storage_contents)



if __name__ == "__main__":
    main()