from flask import Flask,render_template, url_for

import praw
reddit = praw.Reddit(client_id='QBQ9ugfZwtWY-A',
                     client_secret='-UD-meoD4JN6kp08UnDn6PGFl_82vg',
                     password="ca17062001",
                     user_agent="testscript by u/chinmayaswami",
                     username="chinmayaswami")

python=reddit.subreddit('Python').top(limit=5)
dataisbeautiful=reddit.subreddit('dataisbeautiful').top(limit=5)
learnmachinelearning=reddit.subreddit('learnmachinelearning').top(limit=5)

app=Flask(__name__)

@app.route("/")
def index():
      return render_template('index.html', python=python, dataisbeautiful=dataisbeautiful, learnmachinelearning=learnmachinelearning)





if __name__ == "__main__":
    app.run()