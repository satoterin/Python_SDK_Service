from hunter_sdk.service import HunterService

API_KEY = "a21b21087da4a074eb5f5e958d824dab9bb62fe6"


def main() -> None:
    """Main function to demonstrate HunterService usage."""
    service = HunterService(API_KEY)
    email_address = "dennisclay0304@gmail.com"
    validation_result = service.validate_email(email_address)
    storage_contents = service.storage.view_storage()
    print("Validation result:", validation_result)
    print("In-Memory Storage:", storage_contents)



if __name__ == "__main__":
    main()