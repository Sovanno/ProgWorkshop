import pytest
from playwright.sync_api import Playwright
from AutoAPI.config import BookingAPI
from jsonschema import validate
from jsons.jsons import schematok, valid_token_data, invalid_token_data

@pytest.mark.parametrize("username,password", valid_token_data)
def test_get_token_valid(playwright: Playwright, username, password):
    request_context = playwright.request.new_context()
    api = BookingAPI(request_context)

    response = api.get_token(username, password)
    assert response.status == 200, f"Expected status code 200, got {response.status}"

    response_json = response.json()
    validate(instance=response_json, schema=schematok)

    request_context.dispose()

@pytest.mark.parametrize("username,password", invalid_token_data)
def test_get_token_invalid(playwright: Playwright, username, password):
    request_context = playwright.request.new_context()
    api = BookingAPI(request_context)

    response = api.get_token(username, password)
    assert response.status == 401, f"Expected status code 401, got {response.status}"

    request_context.dispose()
