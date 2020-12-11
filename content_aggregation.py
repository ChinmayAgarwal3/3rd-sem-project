
import praw
reddit = praw.Reddit(client_id='QBQ9ugfZwtWY-A',
                     client_secret='-UD-meoD4JN6kp08UnDn6PGFl_82vg',
                     password="ca17062001",
                     user_agent="testscript by u/fakebot3",
                     username="chinmayaswami")


python=reddit.subreddit('Python').top(limit=10)
for submission in python:
      print('Title:{}, ups:{}'.format(submission.title, submission.ups))
