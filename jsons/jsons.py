schematok = {
            "type": "object",
            "properties": {
                "token": {"type": "string"}
            },
            "required": ["token"]
        }

schemaadd = {
            "type": "object",
            "properties": {
                "bookingid": {"type": "integer"},
                "booking": {
                    "type": "object",
                    "properties": {
                        "firstname": {"type": "string"},
                        "lastname": {"type": "string"},
                        "totalprice": {"type": "integer"},
                        "depositpaid": {"type": "boolean"},
                        "bookingdates": {
                            "type": "object",
                            "properties": {
                                "checkin": {"type": "string"},
                                "checkout": {"type": "string"}
                            },
                            "required": ["checkin", "checkout"]
                        },
                        "additionalneeds": {"type": "string"}
                    },
                    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"]
                }
            },
            "required": ["bookingid", "booking"]
        }

valid_booking_data = [
    {
        "firstname": "Ялта",
        "lastname": "2007",
        "totalprice": 300000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    }
]

invalid_booking_data = [
    {},
    {
        "firstname": None,
        "lastname": "БУБУБУ",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "Вито",
        "lastname": "Сколетте",
        "totalprice": None,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "Бобик",
        "lastname": None,
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "Сикс",
        "lastname": "Найн",
        "totalprice": 100,
        "depositpaid": None,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "Арчибальд",
        "lastname": "Финикийский",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": None,
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "Рикардо",
        "lastname": "Муераз",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": None
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "Лоренццо",
        "lastname": "Медиччи",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        None: ""
    },
    {
        "firstname": "Глен",
        "lastname": "Ро",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": True,
        "additionalneeds": "Breakfast"
    },
    {
        "": "Розитта",
        "lastname": "Капоне",
        "totalprice": 1241,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast",
        "а давай ещё": True
    }
]

valid_token_data = [
    ("admin", "password123")
]

invalid_token_data = [
    ("", "password123"),
    ("admin", ""),
    ("wrong_user", "wrong_pass"),
    (None, None),
    (1, 1),
    (True, False),
    ({"Васян": 1000}, "Не нада"),
    {"name": "admin",
     "password": "password123"},
]
