from playwright.sync_api import Playwright
from AutoAPI.config import BookingAPI
from jsonschema import validate
from jsons.jsons import schematok

class TestGetToken:
    def test_get_token(self, playwright: Playwright):
        request_context = playwright.request.new_context()
        api = BookingAPI(request_context)
        username = "admin"
        password = "password123"

        response = api.get_token(username, password)

        assert response.status == 200, f"Expected status code 200, got {response.status}"

        response_json = response.json()
        validate(instance=response_json, schema=schematok)

        request_context.dispose()
