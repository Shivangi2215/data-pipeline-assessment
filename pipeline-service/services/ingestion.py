import requests
from models.customer import Customer

FLASK_URL = "http://mock-server:5000/api/customers"


def fetch_all_customers():
    page = 1
    limit = 10
    all_data = []

    while True:
        response = requests.get(FLASK_URL, params={"page": page, "limit": limit})
        data = response.json().get("data", [])

        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data


def upsert_customers(db, customers):
    count = 0

    for c in customers:
        existing = db.query(Customer).filter_by(customer_id=c["customer_id"]).first()

        if existing:
            for key, value in c.items():
                setattr(existing, key, value)
        else:
            db.add(Customer(**c))

        count += 1

    db.commit()
    return count
