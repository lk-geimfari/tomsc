from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(amount: int = 1, price: float = 0.0, state: str = ""):
    tax = await get_tax_by_state(state)
    price = await calculate_discount_price(amount, price)

    return {
        "tax": tax,
        "state": state,
        "discount_price": price,
        "total_price": price + (price * (tax / 100)),
    }


async def get_tax_by_state(state_code: str = "") -> float:
    states = {
        "UT": 6.85,
        "NV": 8.0,
        "TX": 6.25,
        "AL": 4.0,
        "CA": 8.25,
    }
    try:
        return states[state_code]
    except KeyError:
        return 0.0


async def calculate_discount_price(amount: int = 1,
                                   price: float = 0.0) -> float:
    if amount <= 0:
        return 0

    discount = 0
    total_price = price * amount

    if total_price < 1_000:
        return total_price
    elif 1_000 <= total_price < 5_000:
        discount = 3
    elif 5_000 <= total_price < 7_000:
        discount = 5
    elif 7_000 <= total_price < 10_000:
        discount = 7
    elif 10_000 <= total_price < 50_000:
        discount = 10
    elif total_price >= 50_000:
        discount = 15

    return total_price - (total_price / 100) * discount
