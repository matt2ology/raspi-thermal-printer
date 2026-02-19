import logging
from system_check import SystemCheck


FORMAT = '[%(asctime)s]-[%(funcName)s]-[%(levelname)s] - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT
)


def main():
    logging.info("Starting thermal printer service")

    if not SystemCheck.system_ready():
        logging.error("System checks failed. Exiting.")
        return

    logging.info("System ready. Initializing printer...")


if __name__ == "__main__":
    main()
