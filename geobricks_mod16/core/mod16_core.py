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

def list_days(year):
    """
    List all the available days for a given MODIS product and year.
    @param year: e.g. '2010'
    @type year: str | int
    @return: An array of code/label objects.
    """
    year = year if type(year) is str else str(year)
    year = year if year[0] == 'Y' else 'Y' + year
    if conf['source']['type'] == 'FTP':
        ftp = FTP(conf['source']['ftp']['base_url'])
        ftp.login()
        ftp.cwd(conf['source']['ftp']['data_dir'])
        ftp.cwd(year)
        l = ftp.nlst()
        ftp.quit()
        l.sort()
        out = []
        for s in l:
            date = day_of_the_year_to_date(s, year).strftime('%d %B')
            out.append({'code': s, 'label': date})
        return out

def day_of_the_year_to_date(day, year):
    """
    Convert a day of an year to a date
    @param day: day of the year
    @type day: str | int
    @param year: year of reference
    @type year: str | int
    @return: the date of the day/year i.e. "2012-01-20"
    """
    year = year if year[0] != 'Y' else year[1:]
    year = year if type(year) is int else int(year)
    day = day if day[0] != 'D' else day[1:]
    day = day if type(day) is int else int(day)
    first_of_year = datetime.datetime(year, 1, 1).replace(month=1, day=1)
    ordinal = first_of_year.toordinal() - 1 + day
    return datetime.date.fromordinal(ordinal)
