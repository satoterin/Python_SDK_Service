from hunter_sdk.client import HunterClient
from hunter_sdk.storage import InMemoryStorage


class HunterService:
    """Service layer to interact with Hunter API and storage."""

    def __init__(self, api_key: str) -> None:
        self.client = HunterClient(api_key)
        self.storage = InMemoryStorage()

    def validate_email(self, email: str) -> dict:
        """Validate email and store the result."""
        validation_result = self.client.email_verifier(email)
        self.storage.create(email, validation_result)
        return validation_result