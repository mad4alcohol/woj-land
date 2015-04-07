MASTER_PORT = 5555
MASTER_IP = '192.168.1.105'
MASTER_ADDR = 'tcp://%s:%s' % (MASTER_IP, MASTER_PORT)

HEARTBEAT_DAEMON_IP = '192.168.1.105'
HEARTBEAT_DAEMON_PORT = 21558
HEARTBEAT_DAEMON_ADDR = 'tcp://%s:%s' % (HEARTBEAT_DAEMON_IP,
                                         HEARTBEAT_DAEMON_PORT)

HEARTBEAT_INTERVAL = 10

LANGS_CONF_DIR = './conf'

LOCAL_WOJ_DIR_PREFIX = './woj'
LOCAL_JUDGE_DIR_PREFIX = '../../judge'