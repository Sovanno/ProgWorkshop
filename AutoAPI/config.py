import json
from typing import Dict
from playwright.sync_api import APIRequestContext

class BookingAPI:
    def __init__(self, request_context: APIRequestContext):
        self.request_context = request_context
        self.base_url = "https://restful-booker.herokuapp.com"

    def create_booking(self, date: Dict):
        response = self.request_context.post(
            f"{self.base_url}/booking",
            data=json.dumps(date),
            headers={"Content-Type": "application/json"}
        )
        return response

    def get_token(self, username: str, password: str):
        date = {"username": username, "password": password}
        response = self.request_context.post(
            f"{self.base_url}/auth",
            data=json.dumps(date),
            headers={"Content-Type": "application/json"}
        )
        return response

    def delete_booking(self, booking_id: int, token: str):
        response = self.request_context.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers={
                "Content-Type": "application/json",
                "Cookie": f"token={token}"
            }
        )
        return response

    def get_booking(self, booking_id: int):
        response = self.request_context.get(f"{self.base_url}/booking/{booking_id}")
        return response
