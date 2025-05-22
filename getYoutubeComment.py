from itertools import islice
from youtube_comment_downloader import *

downloader = YoutubeCommentDownloader()
#snow white official trailer
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=iV46TJKL8cU&t=5s', sort_by=SORT_BY_POPULAR)

#for comment in comments:
for comment in islice(comments, 10):
    print(comment)
    #print(comment['text'])