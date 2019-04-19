from update_info import __app__, __author__, __develop__, __asset_update_log__, __download_folder__
from update_info import __develop_server_host__, __develop_update_url__, __develop_server_root__, __develop_server_password__
from update_info import __release_server_host__, __release_update_url__, __release_server_root__, __release_server_password__
try:
    from client_config import ClientConfig
    PUBLIC_KEY = ClientConfig.PUBLIC_KEY
    APP_NAME = ClientConfig.APP_NAME
    COMPANY_NAME = ClientConfig.COMPANY_NAME
    UPDATE_URLS = ClientConfig.UPDATE_URLS  # will overwrite
    MAX_DOWNLOAD_RETRIES = ClientConfig.MAX_DOWNLOAD_RETRIES
except ImportError:
    PUBLIC_KEY = '9H9vx4jfGx0e8ZXTHE1Wl6kl0S9U/cRckB531UhblA0'  # test server public key
    APP_NAME = __app__
    COMPANY_NAME = __author__
    UPDATE_URLS = []  # will overwrite
    MAX_DOWNLOAD_RETRIES = 3

APP_VERSION = '0.0.1'
AUTHOR = __author__

DEVELOP_ENVIRONMENT = __develop__

DEVELOP_SERVER_HOST = __develop_server_host__
DEVELOP_URL = __develop_update_url__
# DEVELOP_AUTHORIZE = True
DEVELOP_ROOT = __develop_server_root__
DEVELOP_PASSWORD = __develop_server_password__

RELEASE_SERVER_HOST = __release_server_host__
RELEASE_URL = __release_update_url__
# RELEASE_AUTHORIZE = True
RELEASE_ROOT = __release_server_root__
RELEASE_PASSWORD = __release_server_password__

ASSET_UPDATE_LOG = __asset_update_log__

DOWNLOAD_FOLDER = __download_folder__


# 测试环境
if DEVELOP_ENVIRONMENT:
    UPDATE_SERVER_HOST = DEVELOP_SERVER_HOST
    UPDATE_URLS = DEVELOP_URL
    AUTHORIZE_HEADER = {
        'basic_auth': '{root}:{password}'.format(root=DEVELOP_ROOT, password=DEVELOP_PASSWORD)}
# 发布环境
else:
    UPDATE_SERVER_HOST = RELEASE_SERVER_HOST
    UPDATE_URLS = RELEASE_URL
    AUTHORIZE_HEADER = {
        'basic_auth': '{root}:{password}'.format(root=RELEASE_ROOT, password=RELEASE_PASSWORD)}
