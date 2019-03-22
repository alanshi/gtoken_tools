import os
from configparser import ConfigParser
import subprocess

import pyotp


PWD = '跳板机密码'


# copy token to clipboard
def set_clipboard_data(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    p.communicate()


# get token
def get_gtoken():

    config_file = os.path.expanduser('~/.gauth')

    cfg = ConfigParser()
    cfg.read(config_file)

    key = cfg.get('youname', 'secret')
    totp = pyotp.TOTP(key)
    token = '{0}{1}'.format(PWD, totp.now())

    set_clipboard_data(bytes(token, 'utf-8'))
    print('token 已经复制,请直接粘贴')

if __name__ == '__main__':

    get_gtoken()