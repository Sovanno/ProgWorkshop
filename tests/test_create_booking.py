from playwright.sync_api import Playwright
from AutoAPI.config import BookingAPI
from jsonschema import validate
from jsons.jsons import schemaadd

class TestCreateBooking:
    def test_create_booking(self, playwright: Playwright):
        request_context = playwright.request.new_context()
        api = BookingAPI(request_context)

        date = {
            "firstname": "Samara",
            "lastname": "2009",
            "totalprice": 200000,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-07"
            },
            "additionalneeds": "Breakfast"
        }

        response = api.create_booking(date)

        assert response.status == 200 or response.status == 201, f"Expected status code 200 or 201, got {response.status}"

        response_json = response.json()
        validate(instance=response_json, schema=schemaadd)

        booking_id = response_json["bookingid"]

        auth_response = api.get_token("admin", "password123")
        auth_token = auth_response.json()["token"]

        delete_response = api.delete_booking(booking_id, auth_token)
        assert delete_response.status == 201 or delete_response.status == 200, f"Expected status code 200 or 201, got {delete_response.status}"

        get_response = api.get_booking(booking_id)
        assert get_response.status == 404, f"Expected status code 404, got {get_response.status}"

        request_context.dispose()
