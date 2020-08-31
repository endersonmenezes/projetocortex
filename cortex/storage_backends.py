from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from django.core.files.storage import Storage, DefaultStorage


class StaticStorage(S3Boto3Storage):
    if not settings.DEBUG:
        location = 'static'
    else:
        pass


class PublicMediaStorage(S3Boto3Storage):
    if not settings.DEBUG:
        location = 'media/public'
        file_overwrite = False
    else:
        pass


class PrivateMediaStorage(S3Boto3Storage):
    if not settings.DEBUG:
        location = 'media/private'
        default_acl = 'private'
        file_overwrite = False
        custom_domain = False
    else:
        pass