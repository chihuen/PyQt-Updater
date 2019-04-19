from utility.thread_manage import Thread_Manage
from update_info import __version__
from updater.updater import Updater

UPDATE_IDLE = 0
UPDATE_NEW = 1
UPDATE_DOWNLOADING = 2
UPDATE_DOWNLOADED = 3


class Model:
    APP_VERSION = __version__

    def __init__(self, controller):
        self.controller = controller
        self.thread_manage = Thread_Manage()
        self.updater = Updater(self.APP_VERSION)
        self.update_status = UPDATE_IDLE

    def req_query_update(self):
        """
        检查更新
        如果有最新更新包，显示更新日志、最新版本并修改状态为可更新
        :return:
        """
        latest_version = self.updater.if_latest_version()
        if self.APP_VERSION != latest_version:
            # 解析更新日志
            if self.APP_VERSION != self.updater.check_asset_update_log():
                # 异步下载更新日志并显示
                if not self.thread_manage.ifAlive("task_show_update_log"):
                    self.thread_manage.register("task_show_update_log", self.task_show_update_log)
                    self.thread_manage.activate("task_show_update_log")
                self.controller.signal_update_log.emit('Checking the update info...')
            else:
                # 显示默认日志并提示最新固件没有包含日志包显
                self.controller.signal_update_log.emit('No update info')
            self._set_new()
            self.controller.signal_version_fresh.emit(self.APP_VERSION, latest_version)
        else:
            # no update
            self._set_idle()
            self.controller.signal_update_log.emit('')
            self.controller.signal_version_fresh.emit(self.APP_VERSION, self.APP_VERSION)

    def _set_idle(self):
        self.controller.signal_update_tips.emit('This is the latest version')
        self.controller.signal_idle.emit()
        self.update_status = UPDATE_IDLE

    def _set_new(self):
        self.controller.signal_update_tips.emit('You can download the latest version')
        self.controller.signal_new.emit()
        self.update_status = UPDATE_NEW

    def _set_downloading(self, progress):
        self.controller.signal_update_tips.emit("Downloading...")
        self.controller.signal_downloading.emit(int(progress))
        self.update_status = UPDATE_DOWNLOADING

    def _set_downloaded(self):
        self.controller.signal_update_tips.emit("Update and restart the app")
        self.controller.signal_downloaded.emit()
        self.update_status = UPDATE_DOWNLOADED

    def req_update(self):
        if self.update_status == UPDATE_IDLE:  # 无动作
            self.req_query_update()
        elif self.update_status == UPDATE_NEW:  # 触发下载
            self.req_download_app()
        elif self.update_status == UPDATE_DOWNLOADING:  # 触发取消，未完成
            pass
        elif self.update_status == UPDATE_DOWNLOADED:  # 触发更新
            self.req_install_app()

    def req_download_app(self):
        self.thread_manage.register('download', self.task_download_app)
        self.thread_manage.activate('download')

    def req_cancel(self):
        self.thread_manage.terminate('download')
        self._set_new()

    def req_install_app(self):
        self.updater.install()

    # 线程任务
    def task_download_app(self, queue, thread_name):
        self._set_downloading(0)

        def updating(info):
            total = info.get(u'total')
            downloaded = info.get(u'downloaded')
            status = info.get(u'status')
            print(downloaded, total, status)
            self._set_downloading(int(downloaded)*100/int(total))

        while self.thread_manage.get_flag(thread_name):
            if self.updater.download(updating):
                self._set_downloaded()
                break
            else:
                pass

        self.thread_manage.deregister(thread_name)

    def task_show_update_log(self, queue, thread_name):
        """
        显示更新日志，下载后读取文件
        :param queue:
        :param thread_name:
        :return:
        """
        texts = ''
        folder = self.updater.download_asset_update_log()
        if folder:
            path = folder + '/updatelog.md'
            with open(path, 'r+') as file:

                for text in file.readlines():
                    texts += text
        self.controller.signal_update_log.emit(texts)
        self.thread_manage.deregister(thread_name)
