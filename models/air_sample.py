class AirSample:
    def __init__(self, param_code, obs_count, max_val, date, location):
        self.param_code = param_code
        self.obs_count = obs_count
        self.max_val = max_val
        self.date = date
        self.location = location

    def __str__(self):
        return f"{self.param_code} | {self.obs_count} | {self.max_val} | {self.date} | {self.location}"