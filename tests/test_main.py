import pytest
from fastapi.testclient import TestClient

from backend.main import app, calculate_discount_price, get_tax_by_state

client = TestClient(app)


def test_root_without_params():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "tax": 0.0,
        "state": "",
        "discount_price": 0.0,
        "total_price": 0.0
    }


@pytest.mark.parametrize(
    "amount, price, state, expected",
    [
        (1, 60000, "UT", 54493.5),
        (1, 60000, "NV", 55080.0),
        (1, 60000, "TX", 54187.5),
        (1, 60000, "AL", 53040.0),
        (1, 60000, "CA", 55207.5),
    ],
)
def test_root_with_params(amount, price, state, expected):
    response = client.get(f"/?amount={amount}&price={price}&state={state}")
    assert response.status_code == 200
    data = response.json()
    assert data['total_price'] == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "state,expected",
    [
        ("UT", 6.85),
        ("NV", 8.0),
        ("TX", 6.25),
        ("AL", 4.0),
        ("CA", 8.25),
    ],
)
async def test_get_tax_by_state(state, expected):
    result = await get_tax_by_state(state)
    assert result == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "amount, price, discount_price",
    [
        (0, 0, 0),
        (1, 1_200, 1_164.0),
        (1, 5_600, 5_320.0),
        (1, 7_450, 6_928.5),
        (1, 12_000, 10_800.0),
        (2, 35_000, 59_500.0),
    ],
)
async def test_calculate_discount_price(amount, price, discount_price):
    result = await calculate_discount_price(amount, price)
    assert result == discount_price
