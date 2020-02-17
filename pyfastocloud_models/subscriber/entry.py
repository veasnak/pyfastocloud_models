from datetime import datetime
from hashlib import md5
from bson.objectid import ObjectId
from enum import IntEnum

from pymodm import MongoModel, fields, EmbeddedMongoModel

from pyfastocloud_models.service.entry import ServiceSettings
from pyfastocloud_models.stream.entry import IStream
import pyfastocloud_models.constants as constants
from pyfastocloud_models.utils.utils import date_to_utc_msec


def is_vod_stream(stream: IStream):
    if not stream:
        return False
    if not stream.visible:
        return False
    stream_type = stream.get_type()
    return stream_type == constants.StreamType.VOD_PROXY or stream_type == constants.StreamType.VOD_RELAY or \
           stream_type == constants.StreamType.VOD_ENCODE


def is_live_stream(stream: IStream):
    if not stream:
        return False
    if not stream.visible:
        return False
    stream_type = stream.get_type()
    return stream_type == constants.StreamType.PROXY or stream_type == constants.StreamType.RELAY or \
           stream_type == constants.StreamType.ENCODE or stream_type == constants.StreamType.TIMESHIFT_PLAYER or \
           stream_type == constants.StreamType.COD_RELAY or stream_type == constants.StreamType.COD_ENCODE or \
           stream_type == constants.StreamType.EVENT


def is_catchup(stream: IStream):
    if not stream:
        return False
    if not stream.visible:
        return False
    stream_type = stream.get_type()
    return stream_type == constants.StreamType.CATCHUP


def for_subscribers_stream(stream: IStream):
    if not stream:
        return False
    if not stream.visible:
        return False
    return is_vod_stream(stream) or is_live_stream(stream) or is_catchup(stream)


class Device(EmbeddedMongoModel):
    ID_FIELD = 'id'
    NAME_FIELD = 'name'
    STATUS_FIELD = 'status'
    CREATED_DATE_FIELD = 'created_date'

    DEFAULT_DEVICE_NAME = 'Device'
    MIN_DEVICE_NAME_LENGTH = 2
    MAX_DEVICE_NAME_LENGTH = 32

    class Status(IntEnum):
        NOT_ACTIVE = 0
        ACTIVE = 1
        BANNED = 2

        @classmethod
        def choices(cls):
            return [(choice, choice.name) for choice in cls]

        @classmethod
        def coerce(cls, item):
            return cls(int(item)) if not isinstance(item, cls) else item

        def __str__(self):
            return str(self.value)

    id = fields.ObjectIdField(required=True, default=ObjectId, primary_key=True)
    created_date = fields.DateTimeField(default=datetime.now)
    status = fields.IntegerField(default=Status.NOT_ACTIVE)
    name = fields.CharField(default=DEFAULT_DEVICE_NAME, min_length=MIN_DEVICE_NAME_LENGTH,
                            max_length=MAX_DEVICE_NAME_LENGTH, required=True)

    def get_id(self) -> str:
        return str(self.id)

    def to_dict(self) -> dict:
        return {Device.ID_FIELD: self.get_id(), Device.NAME_FIELD: self.name, Device.STATUS_FIELD: self.status,
                Device.CREATED_DATE_FIELD: date_to_utc_msec(self.created_date)}


class UserStream(EmbeddedMongoModel):
    FAVORITE_FIELD = 'favorite'
    PRIVATE_FIELD = 'private'
    RECENT_FIELD = 'recent'

    sid = fields.ReferenceField(IStream, required=True)
    favorite = fields.BooleanField(default=False)
    private = fields.BooleanField(default=False)
    recent = fields.DateTimeField(default=datetime.utcfromtimestamp(0))
    interruption_time = fields.IntegerField(default=0, min_value=0, max_value=constants.MAX_VIDEO_DURATION_MSEC,
                                            required=True)

    def get_id(self) -> str:
        return str(self.pk)

    def to_dict(self) -> dict:
        res = self.sid.to_dict()
        res[UserStream.FAVORITE_FIELD] = self.favorite
        res[UserStream.PRIVATE_FIELD] = self.private
        res[UserStream.RECENT_FIELD] = date_to_utc_msec(self.recent)
        return res

    def to_front_dict(self):
        res = self.sid.to_front_dict()
        res[UserStream.FAVORITE_FIELD] = self.favorite
        res[UserStream.PRIVATE_FIELD] = self.private
        res[UserStream.RECENT_FIELD] = date_to_utc_msec(self.recent)
        return res


class Subscriber(MongoModel):
    class Meta:
        collection_name = 'subscribers'
        allow_inheritance = True

    MAX_DATE = datetime(2100, 1, 1)
    ID_FIELD = 'id'
    EMAIL_FIELD = 'login'
    PASSWORD_FIELD = 'password'

    class Status(IntEnum):
        NOT_ACTIVE = 0
        ACTIVE = 1
        DELETED = 2

        @classmethod
        def choices(cls):
            return [(choice, choice.name) for choice in cls]

        @classmethod
        def coerce(cls, item):
            return cls(int(item)) if not isinstance(item, cls) else item

        def __str__(self):
            return str(self.value)

    SUBSCRIBER_HASH_LENGTH = 32

    email = fields.CharField(max_length=64, required=True)
    first_name = fields.CharField(max_length=64, required=True)
    last_name = fields.CharField(max_length=64, required=True)
    password = fields.CharField(min_length=SUBSCRIBER_HASH_LENGTH, max_length=SUBSCRIBER_HASH_LENGTH, required=True)
    created_date = fields.DateTimeField(default=datetime.now)
    exp_date = fields.DateTimeField(default=MAX_DATE)
    status = fields.IntegerField(default=Status.NOT_ACTIVE)
    country = fields.CharField(min_length=2, max_length=3, required=True)
    language = fields.CharField(default=constants.DEFAULT_LOCALE, required=True)

    servers = fields.ListField(fields.ReferenceField(ServiceSettings, on_delete=fields.ReferenceField.PULL), default=[])
    devices = fields.EmbeddedDocumentListField(Device, default=[])
    max_devices_count = fields.IntegerField(default=constants.DEFAULT_DEVICES_COUNT)
    streams = fields.EmbeddedDocumentListField(UserStream, default=[])

    def get_id(self) -> str:
        return str(self.pk)

    @property
    def id(self):
        return self.pk

    def created_date_utc_msec(self):
        return date_to_utc_msec(self.created_date)

    def expiration_date_utc_msec(self):
        return date_to_utc_msec(self.exp_date)

    def add_server(self, server: ServiceSettings):
        self.servers.append(server)
        self.save()

    def add_device(self, device: Device):
        if len(self.devices) < self.max_devices_count:
            self.devices.append(device)
            self.save()

    def remove_device(self, sid: ObjectId):
        devices = self.devices.filter(id=sid)
        devices.delete()
        self.save()

    def find_device(self, sid: ObjectId):
        devices = self.devices.filter(id=sid)
        return devices.first()

    def generate_playlist(self, did: str, lb_server_host_and_port: str) -> str:
        result = '#EXTM3U\n'
        sid = str(self.id)
        for stream in self.streams:
            if stream.private:
                result += stream.sid.generate_playlist(False)
            else:
                result += stream.sid.generate_device_playlist(sid, self.password, did, lb_server_host_and_port, False)

        return result

    def all_streams(self):
        return self.streams

    def add_official_stream_by_id(self, oid: ObjectId):
        user_stream = UserStream(sid=oid)
        self.add_official_stream(user_stream)

    def add_official_stream(self, user_stream: UserStream):
        found_streams = self.streams.filter(sid=user_stream.sid)
        if not found_streams:
            self.streams.append(user_stream)
            self.streams.save()

    def _add_official_stream(self, stream: IStream):
        user_stream = UserStream(sid=stream.id)
        self.add_official_stream(user_stream)

    def add_own_stream(self, user_stream: UserStream):
        found_streams = self.streams.filter(sid=user_stream.sid)
        if not found_streams:
            user_stream.private = True
            self.streams.append(user_stream)
            self.streams.save()

    def _add_own_stream(self, stream: IStream):
        user_stream = UserStream(sid=stream.id)
        user_stream.private = True
        self.add_own_stream(user_stream)

    def remove_official_stream(self, stream: IStream):
        streams = self.streams.filter(sid=stream)
        streams.delete()
        self.streams.save()

    def remove_official_stream_by_id(self, sid: ObjectId):
        original_stream = IStream.objects(id=sid).first()
        self.remove_official_stream(original_stream)

    def remove_own_stream_by_id(self, sid: ObjectId):
        stream = IStream.objects(id=sid).first()
        streams = self.streams.filter(sid=stream, private=True)
        for stream in streams:
            stream.sid.delete()
        streams.delete()
        self.streams.save()

    def remove_all_own_streams(self):
        streams = self.streams.filter(private=True)
        for stream in streams:
            stream.sid.delete()
        streams.delete()
        self.streams.save()

    def find_own_stream(self, sid: ObjectId):
        return IStream.objects(id=sid).first()

    def official_streams(self):
        return self.streams.filter(private=False)

    def own_streams(self):
        return self.streams.filter(private=True)

    def all_available_servers(self):
        return self.servers

    def all_available_official_streams(self) -> [IStream]:
        streams = []
        for serv in self.servers:
            for stream in serv.streams:
                if is_live_stream(stream):
                    streams.append(stream)

        return streams

    def all_available_official_vods(self) -> [IStream]:
        streams = []
        for serv in self.servers:
            for stream in serv.streams:
                if is_vod_stream(stream):
                    streams.append(stream)

        return streams

    def all_available_official_catchups(self) -> [IStream]:
        streams = []
        for serv in self.servers:
            for stream in serv.streams:
                if is_catchup(stream):
                    streams.append(stream)

        return streams

    def select_all_streams(self, select: bool):
        for stream in self.all_available_official_streams():
            if is_live_stream(stream):
                if select:
                    self._add_official_stream(stream)
                else:
                    self.remove_official_stream(stream)

    def select_all_vods(self, select: bool):
        for stream in self.all_available_official_vods():
            if is_vod_stream(stream):
                if select:
                    self._add_official_stream(stream)
                else:
                    self.remove_official_stream(stream)

    def select_all_catchups(self, select: bool):
        for stream in self.all_available_official_catchups():
            if is_catchup(stream):
                if select:
                    self._add_official_stream(stream)
                else:
                    self.remove_official_stream(stream)

    def delete_fake(self, *args, **kwargs):
        self.remove_all_own_streams()
        self.status = Subscriber.Status.DELETED
        self.save()
        # return Document.delete(self, *args, **kwargs)

    @staticmethod
    def make_md5_hash_from_password(password: str) -> str:
        m = md5()
        m.update(password.encode())
        return m.hexdigest()

    @staticmethod
    def generate_password_hash(password: str) -> str:
        return Subscriber.make_md5_hash_from_password(password)

    @staticmethod
    def check_password_hash(hash_str: str, password: str) -> bool:
        return hash_str == Subscriber.generate_password_hash(password)

    @classmethod
    def make_subscriber(cls, email: str, first_name: str, last_name: str, password: str, country: str, language: str,
                        exp_date=MAX_DATE):
        return cls(email=email, first_name=first_name, last_name=last_name,
                   password=Subscriber.make_md5_hash_from_password(password), country=country,
                   language=language, exp_date=exp_date)
