from ftplib import FTP
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
