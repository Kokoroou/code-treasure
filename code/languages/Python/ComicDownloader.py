import inspect
import sys
import os
PATH_PARENT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(PATH_PARENT)
# if you confuse how it works, contact me
# Twitter: https://twitter.com/thanhtrung2314
'''
- filehandle to download and zip files
- requests to get HTML source
- BeautifulSoup to crawl data
'''
import requests
import filehandle
from bs4 import BeautifulSoup


class HentaiVN:
    '''
    Now, come on, my docs string is really nonsense
    don't watse time to read it
    '''

    def __init__(self):
        self.hostname = 'http://hentaivn.net'
        self.downloaded_files = []
        self.stored_directory = ''

    def get_data(self, link):
        '''
        GET:
        + the name of manga
        + links of all chapters
        '''
        html_source = requests.get(link).text
        crawl_data = BeautifulSoup(html_source, 'lxml')
        title_text = crawl_data.find('title').text
        # title_text = 'Truyện Hentai: chap name
        # [chap name] | Đọc Online'
        manga_name = title_text.split(':')[1].split('[')[0].strip()
        # each item in list_chapters
        # <td class="chuong_td">
        # <a target="_blank"
        # href="link">
        # <h2 class="chuong_t"
        # title="chap name chap num">
        # chap name chap num</h2></a>
        # </td>
        list_chapters = crawl_data.find('tbody').find_all(
            class_='chuong_td')
        num_of_chaps = len(list_chapters)
        print('\n-> Detect\nWeb:', self.hostname, '\nManga: ', manga_name,
              '\nChaps:', num_of_chaps)
        # to store zip file
        self.stored_directory = manga_name.strip()
        # [{'name:': .., 'link': ..}, {}, ..]
        data_list_chapters = list(map(lambda x: dict(
            name=x.text.strip(),
            link=self.hostname + x.find('a')['href']),
                                      list_chapters))
        return data_list_chapters

    def download_image(self, data_chapter):
        '''
        Download all images from specific chap
        after that, zip them all into a file
        '''
        print('Name:', data_chapter['name'], '\nLink:', data_chapter['link'])
        # chap name -> chap-name
        file_zip_name = filehandle.FileHandle().filter_file_name(
            '-'.join(data_chapter['name'].split()))
        html_source = requests.get(data_chapter['link']).text
        crawl_data = BeautifulSoup(html_source, 'lxml')
        list_images = crawl_data.find(id='image').find_all('img')
        print('{}\nDownloading...'.format('-' * 50))
        # store all downloaded file names to zip
        downloaded_file_names = []
        # create object FileHandle to handle files
        object_file_handle = filehandle.FileHandle()
        for num, img, in enumerate(list_images):
            # avoid variable in url
            # link?variable=value
            link_img = img['src'].split('?')[0]
            # http.link.file_extension
            # here I used rstrip to avoid \n
            file_extension = '.' + link_img.split('.')[-1]
            # avoid some trash in url
            # something like .jpg%blablabla
            file_extension = file_extension.split('%')[0].rstrip()
            if file_extension.lower() not in ('.jpg', '.png', '.jpeg'):
                continue
            file_name = file_zip_name + '-' + str(num) + file_extension
            # filehandle.download_file object returns file_name
            downloaded_file_names.append(object_file_handle.download_file(
                link_img, file_name))
            print('Loaded', file_name, 'succesfully!')
        # consist of html_file, icon_file, background-image_file
        print('Making html file...')
        # we should make file with different name
        # because we run many thread at the same time
        # it could take file of others
        # cause error file does not exist
        other_files = ['favicon{}.ico'.format(file_zip_name),
                       'background{}.jpg'.format(file_zip_name)]
        # make favicon file and background image file
        object_file_handle.copy_file(PATH_PARENT + '/' +\
            'html_maker/favicon.ico', object_file_handle.
                                     get_current_directory() + '/' +
                                     other_files[0])
        object_file_handle.copy_file(PATH_PARENT + '/' +\
            'html_maker/background.jpg', object_file_handle.
                                     get_current_directory() + '/' +
                                     other_files[1])
        other_files.append(object_file_handle.make_html_file(
            [data_chapter['name']] + other_files, downloaded_file_names))
        file_process = other_files + downloaded_file_names
        print('Zipping...')
        self.downloaded_files.append(object_file_handle.zip_files(
            file_process, file_zip_name + 'hentaivn.net.zip'))
        object_file_handle.delete_files(file_process)
        print('Done.')

