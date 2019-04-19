__version__ = "0.0.3"
__app__ = "PyQt-Updater"
__author__ = "liuzixuan"
__develop__ = True
__asset_update_log__ = "updatelog"
__download_folder_win__ = "/Users/chihuen/PycharmProjects/PyQt-Updater/download"
__download_folder_mac__ = "/Users/chihuen/PycharmProjects/PyQt-Updater/download"
__download_folder__ = ''

__develop_server_host__ = '127.0.0.1'
__develop_update_url__ = ['http://127.0.0.1:2664/Update/']
__develop_server_root__ = 'root'
__develop_server_password__ = ''

__release_server_host__ = '127.0.0.1'
__release_update_url__ = ['http://127.0.0.1:2664/Update/']
__release_server_root__ = 'root'
__release_server_password__ = ''


from dsdev_utils.system import get_system
if get_system() == 'win':
    __download_folder__ = __download_folder_win__
else:
    __download_folder__ = __download_folder_mac__