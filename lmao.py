    

def sendGetWellSoonCard(friendName):
    cardFront = "https://alefiyas-stunning-site.webflow.io/"
    cardInside = generateWellWishes(friendName)
    sendCard(cardFront, cardInside)


friendName = "Alefiya"
sendGetWellSoonCard(friendName)
