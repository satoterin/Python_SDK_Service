import os
from dotenv import load_dotenv
from hunter_sdk.service import HunterService

# Load environment variables from .env file
load_dotenv()

# Get API_KEY and EMAIL_ADDRESS from environment variables. If not found, use default values.
# Replace the default values with your own API_KEY and EMAIL_ADDRESS
API_KEY = os.getenv("HUNTER_API_KEY") or "a21b21087da4a074eb5f5e958d824dab9bb62fe6"
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS") or "dennisclay0304@gmail.com"

# Check if API_KEY and EMAIL_ADDRESS are set
if API_KEY is None or EMAIL_ADDRESS is None:
    raise ValueError("API_KEY and EMAIL_ADDRESS environment variables must be set.")


def main() -> None:
    """Main function to demonstrate HunterService usage."""
    service = HunterService(API_KEY)
    validation_result = service.validate_email(EMAIL_ADDRESS)
    storage_contents = service.storage.view_storage()
    print("Validation result:", validation_result)
    print("In-Memory Storage:", storage_contents)



if __name__ == "__main__":
    main()