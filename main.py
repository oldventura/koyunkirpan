import time
from argparse import ArgumentParser
from runner import runner
from praw import Reddit

if __name__ == '__main__':

  reddit = Reddit(
    "bot",
    config_interpolation="basic"
  )
  
  x = runner(reddit)
  
  argparser = ArgumentParser(description='Ak koyun ak bacağından, kara koyun kara bacağından asılır.')
  
  argparser.add_argument('-i', '--id', type=str, dest="post_id",  help='Post/Submission ID')
  argparser.add_argument('-u', '--url', type=str, dest="post_url", help='Post/Submission URL')

  args = argparser.parse_args()
  
  if args.post_url is not None:
    x.doComment(post_id=args.post_id)
  elif args.post_id is not None:
    x.doComment(post_url=args.post_url)
  else:
    # Select a Random Submission and Comment
    print('Starting script...\n')
    if time.strftime('%H') in x.working_hours:
      try:
        x.doComment(None)
      except Exception as e:
        print('Exception found.', str(e))
    else:
      print('Sorry, not in working hours.')

  # Replying to Comment Replies
  for item in reddit.inbox.unread(limit=None):
    if item.type == "comment_reply":
      x.reply_on_comment(item.id)
    item.mark_read()
