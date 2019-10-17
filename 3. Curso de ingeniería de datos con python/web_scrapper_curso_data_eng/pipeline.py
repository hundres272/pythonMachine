import logging
logging.basicConfig(level=logging.INFO)
import subprocess
import datetime

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal','elpais']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info('Starting extract process')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    for news_site_uid in news_sites_uids:
        name = '{news_site_uid}_{datetime}_articles'.format(
    					news_site_uid=news_site_uid,
    					datetime=now)
        print(name)
#        subprocess.run(['python','main.py', news_site_uid], cwd='./extract')
        # subprocess.run(['find','.','-name','{}*'.format(news_site_uid),
        #                 '-exec','mv','{}','../transform/{}_.csv'.format(name),
        #                 ';'],cwd='./extract')
        subprocess.run(['move',name,'../transform/{}_.csv'.format(name)],cwd='./extract')

def _transform():
    logger.info('Starting  transform process')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python','newspaper_receipe.py',dirty_data_filename],cwd='./transform')
        subprocess.run(['rm',dirty_data_filename],cwd='./transform')
        subprocess.run(['mv',clean_data_filename, '../load/{}.csv'.format(news_site_uid)],cwd='./transform')

def _load():
    logger.info('Starting load process')
    for news_site_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_site_uid)
        subprocess.run(['python','main.py',clean_data_filename],cwd='./load')
        subprocess.run('rm',clean_data_filename)

if __name__ == '__main__':
    main()
