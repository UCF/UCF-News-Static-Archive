import os
import os.path
import re
import chardet
import codecs
import string

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

        # Update header information
        content = string.replace(content, '<a href="index?page=news">UCF Newsroom</a>', '<a href="/">UCF News Archive</a>')
        
        # Rewrite print stylesheet for all media
        content = string.replace(content, '</title>', '</title><link href="css/print.css" rel="stylesheet" type="text/css" />')

        content = string.replace(content, '<p id="print_head">News &amp; Information <br/>www.news.ucf.edu <br/>407-823-5007 <br/>Twitter:@UCFNewsroom</p>','<div id="print_head"><ul style="list-style: none; margin-left: 0; padding-left: 0"><li>News &amp; Information</li><li><a href="http://today.ucf.edu/">today.ucf.edu</a></li><li><a href="tel:407-823-5007">407-823-5007</a></li><li>Twitter: <a href="http://twitter.com/UCF">@UCF</a></li></ul></div>')
        
        if archive_page:
          content = re.sub(r'href="index\?page=article&(?:amp;)?id=([^"]+)"', r'href="index_page_article_id_\1.html"', content)
          content = re.sub(r'href="index\?page=newsarchive&(?:amp;)?archive\.offset=(\d+)&(?:amp;)?fiscal_year=(\d+)"', r'href="index_page_newsarchive_archive.offset_\1_fiscal_year_\2.html"', content)
          content = re.sub(r'href="index\?page=newsarchive&(?:amp;)?fiscal_year=(\d+)"', r'href="index_page_newsarchive_fiscal_year_\1.html"', content)
          
        with open(os.path.join(ARCHIVE_TARGET_DIR, out_filename), 'w') as output:
          output.write(content.encode('utf-8'))