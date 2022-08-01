from .base_model import BaseModel


class Blogs(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Blogs, self).__init__(*args, **kwargs)
