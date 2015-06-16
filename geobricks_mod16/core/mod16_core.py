import os
import json
import urllib
import datetime
from ftplib import FTP
from geobricks_mod16.config.gaul2modis import countries_map
from geobricks_mod16.config.mod16_config import config as conf


def list_years():
    """
    List all the available years for the MOD16 Project.
    @return: An array of code/label objects.
    """
    if conf['source']['type'] == 'FTP':
        ftp = FTP(conf['source']['ftp']['base_url'])
        ftp.login()
        ftp.cwd(conf['source']['ftp']['data_dir'])
        l = ftp.nlst()
        ftp.quit()
        l.sort(reverse=True)
        out = []
        for s in l:
            out.append({'code': s, 'label': s[1:]})
        return out
