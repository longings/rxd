import random
from django.utils import timezone
from hashlib import sha1
from django.utils.encoding import smart_bytes
from django.utils.six import text_type


def generate_sha1(string, salt=None):
    if not isinstance(string, (str, text_type)):
        string = str(string)

    if not salt:
        salt = sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

    salted_bytes = (smart_bytes(salt))+smart_bytes(string)
    hash_ = sha1(salted_bytes).hexdigest()

    return salt, hash_


def upload(instance, filename):
    """
    RXD_UPLOAD_DIR:
        User could upload a picture into media directory, where has a subdir according to his id
    and then save to  the different subdir named by year$month under the subdir.
    """
    extension = filename.split('.')[-1]
    salt, hs = generate_sha1(instance.user.username)

    year_month = timezone.now()

    # path = '%(id)s/%(ym)s' % {
    #     'id': instance.user.id,
    #     'ym': year_month.year + year_month.month,
    # }

    rxd_upload = '%(id)s/%(ym)s/rxd_%(hash)s.%(ext)s' % {
        'id': instance.user.id,
        'ym': str(year_month.year) + '_' + str(year_month.month),
        'hash': hs,
        #'st': salt,
        'ext': extension,
    }

    return rxd_upload
