import os
import json
import urllib
import datetime
from ftplib import FTP
from geobricks_mod16.config.gaul2modis import countries_map
from geobricks_mod16.config.mod16_config import config as conf


def list_layers(product_type):
    ftp = FTP(conf['source']['ftp']['base_url'])
    ftp.login()
    ftp.cwd(conf['source']['ftp']['data_dir'])
    ls = []
    ftp.retrlines('NLST', ls.append)
    ftp.quit()
    out = []
    tmp_buffer = []
    for line in ls:
        try:
            if '_' + product_type + '_' in line and line not in tmp_buffer:
                tmp_buffer.append(line)
                file_path = 'ftp://' + conf['source']['ftp']['base_url'] + conf['source']['ftp']['data_dir']
                file_path += line
                out.append({
                    'file_name': line,
                    'file_path': file_path,
                    'label': line,
                    'size': None
                })
        except ValueError:
            pass
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
