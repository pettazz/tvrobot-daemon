tvrobot = {
    'completed_move_method': 'LOCAL',
    'torrent_ratio_threshold': 0.49,

    'daemon': {
        'log_path': '/var/log/tvrobotd/',
        'working_directory': '/etc/tvrobotd/'
    },

    'api': {
        'cookie_secret': 'lol',
        'host_pattern': r'localhost',
        'host_port': '8888'
    },

    'media': {
        'server': '127.0.0.1',
        'port': 22,
        'user': 'tvrobot',
        'password': 'lol',
        'remote_path': {
            'Movie': '/Movies',
            'Set': '/Movies',
            'Episode': '/TVShows',
            'Season': '/TVShows',
            'Series': '/TVShows',
        }
    },

    'filetypes': {
        "video": (
            'mkv', 'avi', 'mp4', 'm2ts', 'm2s', '3gp', 'ts', 'm4v'
        ),
        "compressed": (
            'zip', 'rar'
        )
    }
}

trakt = {
    'api_key': 'bananahammock'
}

twilio = {
    'account': {
        'ACCOUNT_SID': 'rofl',
        'AUTH_TOKEN': 'lol',
        'phone_number': '+15558675309'
    },

    'split_long_sms': True
}

database = {
    'mysql': {
        'server': 'localhost',
        'port': 3306,
        'user': 'tvrobot',
        'password': 'lol', 
        'schema': 'trvobot'
    }
}

transmission = {
    'server': 'localhost',
    'port': 9091,
    'user': 'tvrobot',
    'password': 'lol',
    'ssh': {
        'port': 22,
        'user': 'tvrobot',
        'password': 'lol',
    }
}
