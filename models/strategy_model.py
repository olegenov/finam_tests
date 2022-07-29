from .base_model import BaseModel

class Strategy(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Strategy, self).__init__(*args, **kwargs)