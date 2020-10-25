import config as cfg
class configReader:

    @staticmethod
    def get_setting(name):
        cfg_new = cfg.config_settings
        return cfg_new[name]


