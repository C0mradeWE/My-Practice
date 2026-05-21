class ProfileNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class LoginFailedError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class DownloadFailedError(Exception):
    def __init__(self, *args):
        super().__init__(*args)