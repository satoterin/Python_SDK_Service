import requests


class HunterClient:
    """Client to interact with Hunter API."""

    base_url = "https://api.hunter.io/v2"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def domain_search(self, domain: str) -> dict:
        """Search for domain information."""
        url = f"{self.base_url}/domain-search"
        query_params = {"domain": domain, "api_key": self.api_key}
        response = requests.get(url, params=query_params)
        return response.json()

    def email_finder(self, domain: str, first_name: str, last_name: str) -> dict:
        """Find email by domain and name."""
        url = f"{self.base_url}/email-finder"
        query_params = {
            "domain": domain,
            "first_name": first_name,
            "last_name": last_name,
            "api_key": self.api_key,
        }
        response = requests.get(url, params=query_params)
        return response.json()

    def email_verifier(self, email: str) -> dict:
        """Verify email address."""
        url = f"{self.base_url}/email-verifier"
        query_params = {"email": email, "api_key": self.api_key}
        response = requests.get(url, params=query_params)
        return response.json()