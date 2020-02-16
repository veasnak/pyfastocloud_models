from pymodm import MongoModel, fields

import pyfastocloud_models.constants as constants


class Epg(MongoModel):
    uri = fields.CharField(default='http://0.0.0.0/epg.xml', max_length=constants.MAX_URL_LENGTH, required=True)
    extension = fields.CharField(max_length=5, required=False)
