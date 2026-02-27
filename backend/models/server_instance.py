# Epic Title: As a system administrator, I want to implement load balancing strategies, so that the server load is distributed evenly and system availability is improved.

class ServerInstance:
    def __init__(self, instance_id: int, address: str, status: str):
        self.instance_id = instance_id
        self.address = address
        self.status = status