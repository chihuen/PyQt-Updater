from . import APP_NAME, AUTHOR, ASSET_UPDATE_LOG, DOWNLOAD_FOLDER, MAX_DOWNLOAD_RETRIES, PUBLIC_KEY
from . import AUTHORIZE_HEADER, UPDATE_URLS
from pyupdater.client import Client


class DefaultConfig:
    PUBLIC_KEY = PUBLIC_KEY
    APP_NAME = APP_NAME
    COMPANY_NAME = AUTHOR
    UPDATE_URLS = UPDATE_URLS
    MAX_DOWNLOAD_RETRIES = MAX_DOWNLOAD_RETRIES


try:
    from client_config import ClientConfig
except ImportError:
    ClientConfig = DefaultConfig


class Updater:

    def __init__(self, version):
        self.version = version
        self.cfg = ClientConfig()
        self.cfg.UPDATE_URLS = UPDATE_URLS
        self.cli = Client(self.cfg, headers=AUTHORIZE_HEADER, refresh=True, data_dir=DOWNLOAD_FOLDER)
        self.app_update = None

    def if_latest_version(self):
        try:
            app_update = self.cli.update_check(self.cfg.APP_NAME, self.version)
            return app_update.version
        except AttributeError:
            return self.version

    def download(self, callback):
        self.cli.add_progress_hook(callback)
        self.app_update = self.cli.update_check(self.cfg.APP_NAME, self.version)
        if self.app_update is None:
            return None

        self.app_update.download()
        if self.app_update.is_downloaded():
            return True

    def install(self):
        if not self.app_update:
            return None

        if self.app_update.is_downloaded():
            self.app_update.extract_restart()
        return True

    # asset
    def get_asset_latest_version(self, asset_name, asset_version):
        try:
            lib_update = self.cli.update_check(asset_name, asset_version)
            return lib_update.version
        except AttributeError as e:
            print("check_asset_update_log error ", e)
            return None

    def download_asset(self, asset_name, asset_version):
        """

        :param asset_name:
        :param asset_version:
        :return:
        """
        lib_update = self.cli.update_check(asset_name, asset_version)
        if lib_update is None:
            return None
        lib_update.download()
        if lib_update.is_downloaded():
            lib_update.extract()
        return lib_update.update_folder

    # asset-update log
    def check_asset_update_log(self):
        """
        检查update_log的版本，update_log版本需要和app版本一致
        :return: 版本号
        """
        new_version = self.get_asset_latest_version(ASSET_UPDATE_LOG, self.version)
        return new_version if new_version else self.version

    def download_asset_update_log(self):
        return self.download_asset(ASSET_UPDATE_LOG, self.version)
