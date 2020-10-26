import config as cfg
from iConfig_Reader import iConfig_Reader
class configReader(iConfig_Reader):

    @staticmethod
    def get_setting(name):
        cfg_new = cfg.config_settings
        return cfg_new[name]


