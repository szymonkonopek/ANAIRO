from Payload import Payload

class PayloadAnimal(Payload):
    def __init__(self, name, type, maxAllowedSpeed, specialNeeds):
        super().__init__(name, type, maxAllowedSpeed)
        self.specialNeeds = specialNeeds