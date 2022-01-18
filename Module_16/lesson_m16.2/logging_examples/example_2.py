import logging


logging.basicConfig(format="%(asctime)s %(message)s",
                    filename='example_2.log',
                    level=logging.DEBUG
                    )

logging.warning("This is warning!")
logging.info("This is info!")
