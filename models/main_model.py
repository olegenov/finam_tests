from .base_model import BaseModel
from ..pages.strategies_page import StrategiesPage


class Main(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
