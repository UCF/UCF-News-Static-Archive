import os
import os.path
import re
import chardet
import codecs

ARCHIVE_SOURCE_DIR = 'news.ucf.edu/UCFnews'
ARCHIVE_TARGET_DIR = 'news.ucf.edu/output'


for filename in os.listdir(ARCHIVE_SOURCE_DIR):
  filepath = os.path.join(ARCHIVE_SOURCE_DIR, filename)
  if not os.path.isdir(filepath):
    
    out_filename = filename.replace('?','_').replace('=', '_').replace('&', '_') + '.html'
    
    with codecs.open(filepath, 'r', 'utf-8') as input:
      article_page = filename.startswith('index?page=article')
      archive_page = filename.startswith('index?page=newsarchive')
      if article_page or archive_page:
        content = input.read()
        
        # Remove all script tags
        content = re.sub('<script[^>]+></script>', '', content)
        
        # Remove all css links except print
        content = re.sub('<link [^>]+>', '', content)
        
        # Rewrite print stylesheet for all media
        content = content.replace('</title>', '</title><link href="css/print.css" rel="stylesheet" type="text/css" />')
        
        if archive_page:
          content = re.sub(r'href="index\?page=article&(?:amp;)?id=([^"]+)"', r'href="index_page_article_id_\1.html"', content)
          content = re.sub(r'href="index\?page=newsarchive&(?:amp;)?archive\.offset=(\d+)&(?:amp;)?fiscal_year=(\d+)"', r'href="index_page_newsarchive_archive.offset_\1_fiscal_year_\2.html"', content)
          content = re.sub(r'href="index\?page=newsarchive&(?:amp;)?fiscal_year=(\d+)"', r'href="index_page_newsarchive_fiscal_year_\1.html"', content)
          
        with open(os.path.join(ARCHIVE_TARGET_DIR, out_filename), 'w') as output:
          output.write(content.encode('utf-8'))