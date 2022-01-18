"""Example of black + logging + pylint"""

import logging

logging.basicConfig(
    format="%(asctime)s %(message)s", filename="example_2.log", level=logging.DEBUG
)


def calculate_sum(dod_a, dod_b):
    """Calculates sum of two numbers"""
    logging.info(f"Got {dod_a} and {dod_b} [+]")
    return dod_a + dod_b


def calculate_mul(mul_a, mul_b):
    """Calculates mul of two numbers"""
    logging.warning(f"Got {mul_a} and {mul_b} [*]")
    return mul_a * mul_b


if __name__ == "__main__":
    print(calculate_sum(10, 20))
    print(calculate_mul(5, 2))
    print(
        "End! End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End!E"
        "nd!End!End!End!End!End!End!End!End!End!End!End!End!End!End!End! "
    )
