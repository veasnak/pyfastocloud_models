from enum import IntEnum

MIN_COUNTRY_LENGTH = 2
MAX_COUNTRY_LENGTH = 2048
MIN_URL_LENGTH = 3
MAX_URL_LENGTH = 2048
MIN_PATH_LENGTH = 1
MAX_PATH_LENGTH = 255

PRECISION = 2

DATE_JS_FORMAT = '%m/%d/%Y %H:%M:%S'

DEFAULT_HLS_PLAYLIST = 'master.m3u8'
DEFAULT_LOCALE = 'en'
AVAILABLE_LOCALES = DEFAULT_LOCALE, 'ru'
AVAILABLE_LOCALES_PAIRS = [(DEFAULT_LOCALE, 'English'), ('ru', 'Russian')]

INVALID_AUDIO_SELECT = -1
DEFAULT_LOOP = False
DEFAULT_AVFORMAT = False
DEFAULT_HAVE_VIDEO = True
DEFAULT_HAVE_AUDIO = True
DEFAULT_RELAY_VIDEO = False
DEFAULT_RELAY_AUDIO = False
DEFAULT_DEINTERLACE = False
MIN_FRAME_RATE = 1
INVALID_FRAME_RATE = 0
MAX_FRAME_RATE = 100
MIN_VOLUME = 0
MIN_PRICE = 0.0
MAX_PRICE = 1000.0
DEFAULT_VOLUME = 1
MAX_VOLUME = 10
MIN_AUDIO_CHANNELS_COUNT = 1
INVALID_AUDIO_CHANNELS_COUNT = 0
MAX_AUDIO_CHANNELS_COUNT = 8
INVALID_WIDTH = 0
INVALID_HEIGHT = 0
INVALID_VIDEO_BIT_RATE = 0
INVALID_AUDIO_BIT_RATE = 0
MIN_ALPHA = 0
MAX_ALPHA = 1
DEFAULT_LOGO_ALPHA = MAX_ALPHA
DEFAULT_LOGO_X = 0
DEFAULT_LOGO_Y = 0
INVALID_LOGO_PATH = str()
INVALID_RATIO_NUM = 0
INVALID_RATIO_DEN = 0
DEFAULT_AUTO_EXIT_TIME = 0
DEFAULT_RESTART_ATTEMPTS = 10
MIN_TIMESHIFT_CHUNK_DURATION = 1
DEFAULT_TIMESHIFT_CHUNK_DURATION = 120
DEFAULT_CATCHUP_CHUNK_DURATION = 12
DEFAULT_CATCHUP_EXIT_TIME = 3600
MAX_TIMESHIFT_CHUNK_DURATION = 600
MIN_TIMESHIFT_CHUNK_LIFE_TIME = 1
DEFAULT_TIMESHIFT_CHUNK_LIFE_TIME = 12 * 3600
MAX_TIMESHIFT_CHUNK_LIFE_TIME = 30 * 12 * 3600
MIN_TIMESHIFT_DELAY = MIN_TIMESHIFT_CHUNK_LIFE_TIME
DEFAULT_TIMESHIFT_DELAY = 3600
MAX_TIMESHIFT_DELAY = MAX_TIMESHIFT_CHUNK_LIFE_TIME

TS_VIDEO_PARSER = 'tsparse'
H264_VIDEO_PARSER = 'h264parse'
H265_VIDEO_PARSER = 'h265parse'
DEFAULT_VIDEO_PARSER = H264_VIDEO_PARSER

AAC_AUDIO_PARSER = 'aacparse'
AC3_AUDIO_PARSER = 'ac3parse'
MPEG_AUDIO_PARSER = 'mpegaudioparse'
DEFAULT_AUDIO_PARSER = AAC_AUDIO_PARSER

AVAILABLE_VIDEO_PARSERS = [(TS_VIDEO_PARSER, 'ts'), (H264_VIDEO_PARSER, 'h264'), (H265_VIDEO_PARSER, 'h265')]
AVAILABLE_AUDIO_PARSERS = [(MPEG_AUDIO_PARSER, 'mpeg'), (AAC_AUDIO_PARSER, 'aac'), (AC3_AUDIO_PARSER, 'ac3')]

EAVC_ENC = 'eavcenc'
OPEN_H264_ENC = 'openh264enc'
X264_ENC = 'x264enc'
NV_H264_ENC = 'nvh264enc'
NV_H265_ENC = 'nvh265enc'
VAAPI_H264_ENC = 'vaapih264enc'
VAAPI_MPEG2_ENC = 'vaapimpeg2enc'
MFX_H264_ENC = 'mfxh264enc'
X265_ENC = 'x265enc'
MSDK_H264_ENC = 'msdkh264enc'
DEFAULT_VIDEO_CODEC = X264_ENC

LAME_MP3_ENC = 'lamemp3enc'
FAAC = 'faac'
VOAAC_ENC = 'voaacenc'
DEFAULT_AUDIO_CODEC = FAAC

AVAILABLE_VIDEO_CODECS = [(EAVC_ENC, 'eav'), (OPEN_H264_ENC, 'openh264'), (X264_ENC, 'x264'), (NV_H264_ENC, 'nvh264'),
                          (NV_H265_ENC, 'nvh265'), (VAAPI_H264_ENC, 'vaapih264'), (VAAPI_MPEG2_ENC, 'vaapimpeg2'),
                          (MFX_H264_ENC, 'mfxh264'), (X265_ENC, 'x265'), (MSDK_H264_ENC, 'msdkh264')]
AVAILABLE_AUDIO_CODECS = [(LAME_MP3_ENC, 'mpeg'), (FAAC, 'aac'), (VOAAC_ENC, 'voaac')]

DEFAULT_SERVICE_ROOT_DIR_PATH = '~/streamer'
DEFAULT_SERVICE_LOG_PATH_TEMPLATE_3SIS = 'http://{0}:{1}/service/log/{2}'
DEFAULT_STREAM_LOG_PATH_TEMPLATE_3SIS = 'http://{0}:{1}/stream/log/{2}'
DEFAULT_STREAM_PIPELINE_PATH_TEMPLATE_3SIS = 'http://{0}:{1}/stream/pipeline/{2}'

DEFAULT_TEST_URL = 'test'

DEFAULT_STREAM_NAME = 'Stream'
DEFAULT_STREAM_ICON_URL = 'https://fastocloud.com/static/images/unknown_channel.png'
DEFAULT_STREAM_PREVIEW_ICON_URL = 'https://fastocloud.com/static/images/unknown_preview.png'
INVALID_TRAILER_URL = 'https://fastocloud.com/static/video/invalid_trailer.m3u8'
DEFAULT_STREAM_GROUP_TITLE = ''
DEFAULT_STREAM_DESCRIPTION = ''
DEFAULT_STREAM_TVG_NAME = ''
DEFAULT_STREAM_TVG_ID = ''
DEFAULT_DEVICES_COUNT = 10

MIN_STREAM_NAME_LENGTH = 0
MAX_STREAM_NAME_LENGTH = 64
MIN_STREAM_TVG_NAME_LENGTH = 0
MAX_STREAM_TVG_NAME_LENGTH = 64
MIN_STREAM_TVG_ID_LENGTH = 0
MAX_STREAM_TVG_ID_LENGTH = 64
MIN_STREAM_GROUP_TITLE_LENGTH = 0
MAX_STREAM_GROUP_TITLE_LENGTH = 64
MIN_STREAM_DESCRIPTION_LENGTH = 0
MAX_STREAM_DESCRIPTION_LENGTH = 4096

MAX_VIDEO_DURATION_MSEC = 3600 * 1000 * 365

AVAILABLE_COUNTRIES = [('AF', 'Afghanistan'),
                       ('AX', 'Åland Islands'),
                       ('AL', 'Albania'),
                       ('DZ', 'Algeria'),
                       ('AS', 'American Samoa'),
                       ('AD', 'Andorra'),
                       ('AO', 'Angola'),
                       ('AI', 'Anguilla'),
                       ('AQ', 'Antarctica'),
                       ('AG', 'Antigua and Barbuda'),
                       ('AR', 'Argentina'),
                       ('AM', 'Armenia'),
                       ('AW', 'Aruba'),
                       ('AU', 'Australia'),
                       ('AT', 'Austria'),
                       ('AZ', 'Azerbaijan'),
                       ('BS', 'Bahamas'),
                       ('BH', 'Bahrain'),
                       ('BD', 'Bangladesh'),
                       ('BB', 'Barbados'),
                       ('BY', 'Belarus'),
                       ('BE', 'Belgium'),
                       ('BZ', 'Belize'),
                       ('BJ', 'Benin'),
                       ('BM', 'Bermuda'),
                       ('BT', 'Bhutan'),
                       ('BO', 'Bolivia), Plurinational State of'),
                       ('BQ', 'Bonaire), Sint Eustatius and Saba'),
                       ('BA', 'Bosnia and Herzegovina'),
                       ('BW', 'Botswana'),
                       ('BV', 'Bouvet Island'),
                       ('BR', 'Brazil'),
                       ('IO', 'British Indian Ocean Territory'),
                       ('BN', 'Brunei Darussalam'),
                       ('BG', 'Bulgaria'),
                       ('BF', 'Burkina Faso'),
                       ('BI', 'Burundi'),
                       ('KH', 'Cambodia'),
                       ('CM', 'Cameroon'),
                       ('CA', 'Canada'),
                       ('CV', 'Cape Verde'),
                       ('KY', 'Cayman Islands'),
                       ('CF', 'Central African Republic'),
                       ('TD', 'Chad'),
                       ('CL', 'Chile'),
                       ('CN', 'China'),
                       ('CX', 'Christmas Island'),
                       ('CC', 'Cocos (Keeling) Islands'),
                       ('CO', 'Colombia'),
                       ('KM', 'Comoros'),
                       ('CG', 'Congo'),
                       ('CD', 'Congo), the Democratic Republic of the'),
                       ('CK', 'Cook Islands'),
                       ('CR', 'Costa Rica'),
                       ('CI', 'Côte d\'Ivoire'),
                       ('HR', 'Croatia'),
                       ('CU', 'Cuba'),
                       ('CW', 'Curaçao'),
                       ('CY', 'Cyprus'),
                       ('CZ', 'Czech Republic'),
                       ('DK', 'Denmark'),
                       ('DJ', 'Djibouti'),
                       ('DM', 'Dominica'),
                       ('DO', 'Dominican Republic'),
                       ('EC', 'Ecuador'),
                       ('EG', 'Egypt'),
                       ('SV', 'El Salvador'),
                       ('GQ', 'Equatorial Guinea'),
                       ('ER', 'Eritrea'),
                       ('EE', 'Estonia'),
                       ('ET', 'Ethiopia'),
                       ('FK', 'Falkland Islands (Malvinas)'),
                       ('FO', 'Faroe Islands'),
                       ('FJ', 'Fiji'),
                       ('FI', 'Finland'),
                       ('FR', 'France'),
                       ('GF', 'French Guiana'),
                       ('PF', 'French Polynesia'),
                       ('TF', 'French Southern Territories'),
                       ('GA', 'Gabon'),
                       ('GM', 'Gambia'),
                       ('GE', 'Georgia'),
                       ('DE', 'Germany'),
                       ('GH', 'Ghana'),
                       ('GI', 'Gibraltar'),
                       ('GR', 'Greece'),
                       ('GL', 'Greenland'),
                       ('GD', 'Grenada'),
                       ('GP', 'Guadeloupe'),
                       ('GU', 'Guam'),
                       ('GT', 'Guatemala'),
                       ('GG', 'Guernsey'),
                       ('GN', 'Guinea'),
                       ('GW', 'Guinea-Bissau'),
                       ('GY', 'Guyana'),
                       ('HT', 'Haiti'),
                       ('HM', 'Heard Island and McDonald Islands'),
                       ('VA', 'Holy See (Vatican City State)'),
                       ('HN', 'Honduras'),
                       ('HK', 'Hong Kong'),
                       ('HU', 'Hungary'),
                       ('IS', 'Iceland'),
                       ('IN', 'India'),
                       ('ID', 'Indonesia'),
                       ('IR', 'Iran), Islamic Republic of'),
                       ('IQ', 'Iraq'),
                       ('IE', 'Ireland'),
                       ('IM', 'Isle of Man'),
                       ('IL', 'Israel'),
                       ('IT', 'Italy'),
                       ('JM', 'Jamaica'),
                       ('JP', 'Japan'),
                       ('JE', 'Jersey'),
                       ('JO', 'Jordan'),
                       ('KZ', 'Kazakhstan'),
                       ('KE', 'Kenya'),
                       ('KI', 'Kiribati'),
                       ('KP', 'Korea), Democratic People\'s Republic of'),
                       ('KR', 'Korea), Republic of'),
                       ('KW', 'Kuwait'),
                       ('KG', 'Kyrgyzstan'),
                       ('LA', 'Lao People\'s Democratic Republic'),
                       ('LV', 'Latvia'),
                       ('LB', 'Lebanon'),
                       ('LS', 'Lesotho'),
                       ('LR', 'Liberia'),
                       ('LY', 'Libya'),
                       ('LI', 'Liechtenstein'),
                       ('LT', 'Lithuania'),
                       ('LU', 'Luxembourg'),
                       ('MO', 'Macao'),
                       ('MK', 'Macedonia), the former Yugoslav Republic of'),
                       ('MG', 'Madagascar'),
                       ('MW', 'Malawi'),
                       ('MY', 'Malaysia'),
                       ('MV', 'Maldives'),
                       ('ML', 'Mali'),
                       ('MT', 'Malta'),
                       ('MH', 'Marshall Islands'),
                       ('MQ', 'Martinique'),
                       ('MR', 'Mauritania'),
                       ('MU', 'Mauritius'),
                       ('YT', 'Mayotte'),
                       ('MX', 'Mexico'),
                       ('FM', 'Micronesia), Federated States of'),
                       ('MD', 'Moldova), Republic of'),
                       ('MC', 'Monaco'),
                       ('MN', 'Mongolia'),
                       ('ME', 'Montenegro'),
                       ('MS', 'Montserrat'),
                       ('MA', 'Morocco'),
                       ('MZ', 'Mozambique'),
                       ('MM', 'Myanmar'),
                       ('NA', 'Namibia'),
                       ('NR', 'Nauru'),
                       ('NP', 'Nepal'),
                       ('NL', 'Netherlands'),
                       ('NC', 'New Caledonia'),
                       ('NZ', 'New Zealand'),
                       ('NI', 'Nicaragua'),
                       ('NE', 'Niger'),
                       ('NG', 'Nigeria'),
                       ('NU', 'Niue'),
                       ('NF', 'Norfolk Island'),
                       ('MP', 'Northern Mariana Islands'),
                       ('NO', 'Norway'),
                       ('OM', 'Oman'),
                       ('PK', 'Pakistan'),
                       ('PW', 'Palau'),
                       ('PS', 'Palestinian Territory), Occupied'),
                       ('PA', 'Panama'),
                       ('PG', 'Papua New Guinea'),
                       ('PY', 'Paraguay'),
                       ('PE', 'Peru'),
                       ('PH', 'Philippines'),
                       ('PN', 'Pitcairn'),
                       ('PL', 'Poland'),
                       ('PT', 'Portugal'),
                       ('PR', 'Puerto Rico'),
                       ('QA', 'Qatar'),
                       ('RE', 'Réunion'),
                       ('RO', 'Romania'),
                       ('RU', 'Russian Federation'),
                       ('RW', 'Rwanda'),
                       ('BL', 'Saint Barthélemy'),
                       ('SH', 'Saint Helena), Ascension and Tristan da Cunha'),
                       ('KN', 'Saint Kitts and Nevis'),
                       ('LC', 'Saint Lucia'),
                       ('MF', 'Saint Martin (French part)'),
                       ('PM', 'Saint Pierre and Miquelon'),
                       ('VC', 'Saint Vincent and the Grenadines'),
                       ('WS', 'Samoa'),
                       ('SM', 'San Marino'),
                       ('ST', 'Sao Tome and Principe'),
                       ('SA', 'Saudi Arabia'),
                       ('SN', 'Senegal'),
                       ('RS', 'Serbia'),
                       ('SC', 'Seychelles'),
                       ('SL', 'Sierra Leone'),
                       ('SG', 'Singapore'),
                       ('SX', 'Sint Maarten (Dutch part)'),
                       ('SK', 'Slovakia'),
                       ('SI', 'Slovenia'),
                       ('SB', 'Solomon Islands'),
                       ('SO', 'Somalia'),
                       ('ZA', 'South Africa'),
                       ('GS', 'South Georgia and the South Sandwich Islands'),
                       ('SS', 'South Sudan'),
                       ('ES', 'Spain'),
                       ('LK', 'Sri Lanka'),
                       ('SD', 'Sudan'),
                       ('SR', 'Suriname'),
                       ('SJ', 'Svalbard and Jan Mayen'),
                       ('SZ', 'Swaziland'),
                       ('SE', 'Sweden'),
                       ('CH', 'Switzerland'),
                       ('SY', 'Syrian Arab Republic'),
                       ('TW', 'Taiwan), Province of China'),
                       ('TJ', 'Tajikistan'),
                       ('TZ', 'Tanzania), United Republic of'),
                       ('TH', 'Thailand'),
                       ('TL', 'Timor-Leste'),
                       ('TG', 'Togo'),
                       ('TK', 'Tokelau'),
                       ('TO', 'Tonga'),
                       ('TT', 'Trinidad and Tobago'),
                       ('TN', 'Tunisia'),
                       ('TR', 'Turkey'),
                       ('TM', 'Turkmenistan'),
                       ('TC', 'Turks and Caicos Islands'),
                       ('TV', 'Tuvalu'),
                       ('UG', 'Uganda'),
                       ('UA', 'Ukraine'),
                       ('AE', 'United Arab Emirates'),
                       ('GB', 'United Kingdom'),
                       ('US', 'United States'),
                       ('UM', 'United States Minor Outlying Islands'),
                       ('UY', 'Uruguay'),
                       ('UZ', 'Uzbekistan'),
                       ('VU', 'Vanuatu'),
                       ('VE', 'Venezuela), Bolivarian Republic of'),
                       ('VN', 'Viet Nam'),
                       ('VG', 'Virgin Islands), British'),
                       ('VI', 'Virgin Islands), U.S.'),
                       ('WF', 'Wallis and Futuna'),
                       ('EH', 'Western Sahara'),
                       ('YE', 'Yemen'),
                       ('ZM', 'Zambia'),
                       ('ZW', 'Zimbabwe')]


def round_value(value: float):
    return round(value, PRECISION)


class UserAgent(IntEnum):
    GSTREAMER = 0
    VLC = 1
    FFMPEG = 2
    WINK = 3
    CHROME = 4
    MOZILLA = 5
    SAFARI = 6

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class HlsType(IntEnum):
    HLS_PULL = 0
    HLS_PUSH = 1

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class MessageType(IntEnum):
    TEXT = 0
    HYPERLINK = 1

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class PlayerMessage:
    message = str()
    ttl = 0
    type = MessageType.TEXT

    def __init__(self, message: str, ttl: int, message_type: MessageType):
        self.message = message
        self.ttl = ttl
        self.type = message_type


class StreamType(IntEnum):
    PROXY = 0
    VOD_PROXY = 1
    RELAY = 2
    ENCODE = 3
    TIMESHIFT_PLAYER = 4
    TIMESHIFT_RECORDER = 5
    CATCHUP = 6
    TEST_LIFE = 7
    VOD_RELAY = 8
    VOD_ENCODE = 9
    COD_RELAY = 10
    COD_ENCODE = 11
    EVENT = 12

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class VodType(IntEnum):
    VODS = 0
    SERIES = 1

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)
