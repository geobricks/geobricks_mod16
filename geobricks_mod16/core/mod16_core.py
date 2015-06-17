# import os
from ftplib import FTP
from geobricks_mod16.config.mod16_config import config as conf


def list_layers(product_type):
    """
    List all the available layers for the given product type.
    @param product_type: 'ET' or 'PET'.
    @type product_type: str
    @return: List of code/label objects.
    """
    ftp = FTP(conf['source']['ftp']['base_url'])
    ftp.login()
    ftp.cwd(conf['source']['ftp']['data_dir'])
    ls = []
    ftp.retrlines('NLST', ls.append)
    ftp.quit()
    out = []
    tmp_buffer = []
    for line in ls:
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
    return out

# def download(product_type):
#     ftp = FTP(conf['source']['ftp']['base_url'])
#     ftp.login()
#     ftp.cwd(conf['source']['ftp']['data_dir'])
#     file_names = ftp.nlst()
#     for filename in file_names:
#         print 'Downloading ' + filename + '...'
#         local_filename = os.path.join('/home/kalimaha/Desktop/MOD16/', filename)
#         file = open(local_filename, 'wb')
#         ftp.retrbinary('RETR '+ filename, file.write)
#         file.close()
#         print '\t...done.'
#     ftp.quit()
