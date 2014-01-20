class TVROBOT:
    'log_path': 'logs',
    'completed_move_method': 'LOCAL',
    'torrent_ratio_threshold': 0.49,

    API = {
        'cookie_secret': 'butts',
        'host_pattern': r'localhost',
        'host_port': '8888'
    }

    MEDIA = {
        'server': '127.0.0.1',
        'port': 22,
        'user': 'tvrobot',
        'password': 'lol',
        'remote_path': {
            'Movie': '/media/Storage/Movies',
            'Set': '/media/Storage/Movies',
            'Episode': '/media/Storage/TV',
            'Season': '/media/Storage/TV',
            'Series': '/media/Storage/TV',
        }
    }

    FILETYPES = {
        "video": (
            'mkv', 'avi', 'mp4', 'm2ts', 'm2s', '3gp', 'ts', 'm4v'
        ),
        "compressed": (
            'zip', 'rar'
        )
    }

class TVRAGE:
    'tz_offset': -10800,
    'api_key': 'butts'

class TWILIO:
    ACCOUNT = {
        'ACCOUNT_SID': 'sid',
        'AUTH_TOKEN': 'auth',
        'phone_number': '+15555555555'
    }

    'split_long_sms': True

class DATABASE:
    MYSQL = {
        'server': 'soemhost',
        'port': 3306,
        'user': 'tvrobot',
        'password': 'lol', 
        'schema': 'TvRobot'
    }

class TRANSMISSION:
    'server': 'somehost',
    'port': 9091,
    'user': 'tvrobot',
    'password': 'lol',
    'SSH': {
        'port': 22,
        'user': 'tvrobot',
        'password': 'lol',
    }

class SELENIUM:
    'server': 'somehost',
    'port': '4444',
    'timeout': 30,
    'log_path': 'logs'