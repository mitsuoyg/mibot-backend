from mongoengine import Document, StringField, BinaryField

import re

rgx_username = r"^[a-z][a-zñ0-9\._@]*$"  # user123._@xxx
rgx_name = r"^[a-zA-ZÀ-ÿ\s]+$"  # José García
rgx_email = r"^[^@]+@[^@]+\.[^@]+$"  # xxx@xxx.xxx


class User(Document):
    first_name = StringField(regex=rgx_name, required=True)
    last_name = StringField(regex=rgx_name, required=True)
    email = StringField(regex=rgx_email, required=True)
    username = StringField(regex=rgx_username, required=True, unique=True)
    password = BinaryField(required=True)
