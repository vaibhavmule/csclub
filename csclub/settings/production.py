from .base import *

DEBUG = False

# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

ADMINS = [('Vaibhav', 'vaibhavmule135@gmail.com'), ]

SERVER_EMAIL = 'no-replay@csclub.co'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@mg.csclub.co'
EMAIL_HOST_PASSWORD = '7aafa2dc56dcd3f42df29f48a0ac47fa-6b60e603-3b6b5468'
EMAIL_USE_TLS = True
