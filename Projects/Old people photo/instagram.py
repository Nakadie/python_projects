"""
basic structure.

1st: import images from a specific instagram acount

2nd: make the images appear in a slideshow

3rd: update new images repeat
"""

#import images from a specific account.
import instaloader

L = instaloader.Instaloader()

posts = instaloader.Hashtag.from_name(L.context, 'kaminjapan').get_posts()

users = set()

for post in posts:
    if not post.owner_profile in users:
        L.download_post(post, '#kaminjapan')
        users.add(post.owner_profile)
    else:
        print("{} from {} skipped.".format(post, post.owner_profile))



