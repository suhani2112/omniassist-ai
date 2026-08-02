import datetime


class AgentLogger:


    def __init__(self):

        self.logs = []



    def log(self, request_id, event, data):

        entry = {
            "request_id": request_id,
            "time": str(datetime.datetime.now()),
            "event": event,
            "data": data
        }

        self.logs.append(entry)



    def get_logs(self):

        return self.logs