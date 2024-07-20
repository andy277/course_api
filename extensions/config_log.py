import logging

def config_log(log) -> logging.Logger:
    logger = logging.getLogger(log)

    handler = logging.FileHandler('log/main.log')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger