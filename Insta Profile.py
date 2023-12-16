import instaloader,time
ig=instaloader.Instaloader()

username=input("Write Your Instagram Username : ")
password=input("Write Your Instagram Password : ")
ig.login(username,password)

dp=input("Enter Insta username: ")
ig.download_profile(dp,profile_pic=True,download_tagged=True,download_stories=True)


"""Hashtag=instaloader.Hashtag()
Hashtag.get_posts()
"""