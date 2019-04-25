import os

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
if EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
    EMAIL_HOST = smtp.1m6.win
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True
    EMAIL_HOST_USER = 'zhangcheng@1m6.win'
    EMAIL_HOST_PASSWORD = '74r7J8fBHDP5'
elif EMAIL_BACKEND == 'anymail.backends.mailgun.EmailBackend':
    ANYMAIL = {
        "MAILGUN_API_KEY": 'api-08acd72decac37706db9b077542114ba',
        "MAILGUN_SENDER_DOMAIN": 'smtp.1m6.win',
    }
