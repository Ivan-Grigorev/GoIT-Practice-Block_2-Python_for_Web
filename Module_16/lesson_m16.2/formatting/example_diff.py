import logging

logging.basicConfig(format="%(asctime)s %(message)s",
                    filename='example_3.log',
                    level=logging.DEBUG
                    )


def calculate_sum(a, b):
    logging.info(f"Got {a} and {b} [+]")
    return a + b


def calculate_mul(a, b):
    logging.warning(f"Got {a} and {b} [*]")
    return a * b


if __name__ == '__main__':
    print(calculate_sum(10, 20))
    print(calculate_mul(5, 2))
    print("End!")
