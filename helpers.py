class Configuration:
        def __init__(self, API_KEY, API_SECRET_KEY, BEARER_TOKEN, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
            self.API_KEY=API_KEY
            self.API_SECRET_KEY=API_SECRET_KEY
            self.BEARER_TOKEN=BEARER_TOKEN
            self.ACCESS_TOKEN=ACCESS_TOKEN
            self.ACCESS_TOKEN_SECRET=ACCESS_TOKEN_SECRET

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
