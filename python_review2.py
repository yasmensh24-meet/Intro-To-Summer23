def createytvideo():
	#take a dictionary inside  the function
	yt={
	"Title":"",
	"Description":"descriotion",
	"Likes":0,
	"Dislikes":0,
	"comments":{}

	}


	description=input("give me a description")
	title=input("give me a title")
	yt["Title"]=title
	yt["Description"]= description




youtube = createytvideo()

def like(youtube):

	if "Likes" in youtube:
		youtube["Likes"]= youtube["Likes"] +1

return youtube

def dislike(youtube)
	if "Dislikes" in youtube
		youtube["Dislikes"]=youtube["Dislikes"]+1

return youtube

user = input("enter your name")
 def addcomment(youtubevideo,username,comment_text):
 	youtube["comments"][username]=comment_text