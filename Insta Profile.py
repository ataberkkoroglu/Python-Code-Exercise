import instaloader
ig=instaloader.Instaloader()
ig.login("username","password")
dp=input("Enter Insta username: ")
ig.download_profile(dp,download_stories_only=True)


"""Hashtag=instaloader.Hashtag()
Hashtag.get_posts()
"""