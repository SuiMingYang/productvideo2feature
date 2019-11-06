import configparser

def setConf():
    config_url="./config.conf"
    conf = configparser.RawConfigParser()
    conf.read(config_url,encoding='utf-8')
    return conf

conf = setConf()