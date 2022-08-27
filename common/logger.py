import logging
import os
import time

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:
    def __init__(self):
        self.file_path = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%y%m%d")))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(pathname)s %(lineno)d]:%(message)s", "%m-%d %H:%M:%S")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        file_handler = logging.FileHandler(self.file_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


log = Logger().logger

if __name__ == "__main__":
    log.info("__测试logging__")
    log.warning("warning")

