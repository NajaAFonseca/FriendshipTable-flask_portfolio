import random

faq_data = []
faq_list = [
    "Q: How do you play Snake? A: Move the snake around to eat the blocks!",
    "Q: How do you move the snake? A: Use the arrow keys to move.",
    "Q: Can you move through the snakes body? A: If you hit the snake's tail, you lose!",
    "Q: What happens if you run into the border? A: You lose if your snake hits the border :(",
    "Q: How do you win Snake? Win snake by getting all the blocks!",
    "Q: Is snake fun? A: Yes! Snake is a super fun interactive game",
    "Q: What College Board criteria does this game meet? A: All because we just amazing like that",
    "Q: Who is the coolest teacher? A: Mr. Yeung of course"
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in joke_list:
        faq_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(faq_data)

# Joke getter
def getJoke(id):
    return(faq_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(faq_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return faq_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return faq_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    faq_data[id]['haha'] = faq_data[id]['haha'] + 1
    return faq_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    faq_data[id]['boohoo'] = faq_data[id]['boohoo'] + 1
    return faq_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(faq_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))