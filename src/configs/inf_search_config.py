

class Config:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.endpoint = "https://www.googleapis.com/customsearch/v1"
        self.cx = "YOUR_CSE_ID"
        self.num_results = 10  # number of results to return

config_instance = Config()