import yaml
from configparser import ConfigParser
from common.logger import log


class ReadData:
    def load_ini(self, file_path):
        log.info("加载 {} 文件.....".format(file_path))
        config = ConfigParser()
        config.read(file_path, encoding="utf-8")
        data = config._sections
        log.info("读到数据 ===》 {}".format(data))
        return data

    def load_yaml(self, file_path):
        log.info("加载 {} 文件.....".format(file_path))
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        log.info("读到数据 ===》 {}".format(data))
        return data

data = ReadData()
