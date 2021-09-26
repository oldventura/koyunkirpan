# koyunkirpan
Source code for the reddit bot account u/koyunkirpan

## Installation
```
$ git clone https://github.com/oldventura/koyunkirpan.git
$ cd koyunkirpan
$ pip -r requirements.txt
$ mv praw.example.ini praw.ini
```

* After that configure the file `praw.ini` and enter your own credentials inside `<placeholders>`
* Edit your crontab and add this file if you want your bot to make comments automatically every * minutes or so.

## Usage
#### Normal usage:
```
python main.py
```
* Collects total of 100 posts from hot and new.
* Selects one random post
* Collects keywords from this post and top comments
* Searches for similar posts
* Collects top 5 comments from similar posts
* Compares keywords from these comments to find the best fit
* Comments the best fit on the selected post

#### Comment on specific post:
```
python main.py -u <post_url>
```
```
python main.py --url <post_url>
```
or
```
python main.py -i <post_id>
```
```
python main.py --id <post_id>
```
* Finds the submission on reddit by the post id
* Finds the submission on reddit by the post url
* **Submission by url takes precedence over the submission by id.**
* Collects keywords from this post and top comments
* Searches for similar posts
* Collects top 5 comments from similar posts
* Compares keywords from these comments to find the best fit
* Comments the best fit on the selected post
