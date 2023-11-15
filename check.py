fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 3, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 4, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 5, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 6, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 7, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 8, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]

print(fake_trades[2:][:5])
