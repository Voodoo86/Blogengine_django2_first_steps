from django.utils.text import slugify
from time import time


def gen_slug(s):
    """
    Slug Generator for Any Models With it
    """
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
