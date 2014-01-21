class TVROBOT:
    'log_path': 'logs',
    'completed_move_method': 'LOCAL',
    'torrent_ratio_threshold': 0.09,

    API = {
        'cookie_secret': 'd4de3be272c5b457dd5fec769b51b2c3',
        'host_pattern': r'localhost',
        'host_port': '8888'
    }

    MEDIA = {
        'server': '127.0.0.1',
        'port': 22,
        'user': 'tvrobot',
        'password': 'lol',
        'remote_path': {
            'Movie': '/Ext4/Movies',
            'Set': '/Ext4/Movies',
            'Episode': '/Ext4/Tv.Shows',
            'Season': '/Ext4/Tv.Shows',
            'Series': '/Ext4/Tv.Shows',
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
    'tz_offset': -3600,
    'api_key': '967oJgtZnzEPUAYPbxWI'

class TWILIO:
    ACCOUNT = {
        'ACCOUNT_SID': 'ACfbd69e8db8aa5bb80c5a57cbb678edd4',
        'AUTH_TOKEN': '74b0f7c80ae21f3feb5ad476bcbb6c8b',
        'phone_number': '+14195176268'
    }

    'split_long_sms': True

class DATABASE:
    MYSQL = {
        'server': '192.168.1.117',
        'port': 3306,
        'user': 'tvrobot',
        'password': 'fuckyeabody', 
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