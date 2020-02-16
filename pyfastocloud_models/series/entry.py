from datetime import datetime

from pymodm import MongoModel, fields

import pyfastocloud_models.constants as constants


class Serial(MongoModel):
    class Meta:
        collection_name = 'series'

    DEFAULT_SERIES_NAME = 'Serial'
    MIN_SERIES_NAME_LENGTH = 3
    MAX_SERIES_NAME_LENGTH = 30

    def get_id(self) -> str:
        return str(self.pk)

    @property
    def id(self):
        return self.pk

    created_date = fields.DateTimeField(default=datetime.now)  # for inner use
    name = fields.CharField(default=DEFAULT_SERIES_NAME, max_length=MAX_SERIES_NAME_LENGTH,
                            min_length=MIN_SERIES_NAME_LENGTH)
    group = fields.CharField(default=constants.DEFAULT_STREAM_GROUP_TITLE,
                             max_length=constants.MAX_STREAM_GROUP_TITLE_LENGTH,
                             min_length=constants.MIN_STREAM_GROUP_TITLE_LENGTH, required=True)
    description = fields.CharField(default=constants.DEFAULT_STREAM_DESCRIPTION,
                                   min_length=constants.MIN_STREAM_DESCRIPTION_LENGTH,
                                   max_length=constants.MAX_STREAM_DESCRIPTION_LENGTH,
                                   required=True)
    season = fields.IntegerField(default=1, min_value=0, required=True)
    visible = fields.BooleanField(default=True, required=True)
