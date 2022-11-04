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

# Initialize questions
def initQuestion():
    # setup Question into a dictionary with id, Question, Helpful, Not Helpful
    item_id = 0
    for item in faq_list:
        faq_data.append({"id": item_id, "Question": item, "Helpful": 0, "Not Helpful": 0})
        item_id += 1
    # prime some Helpful responses
    for i in range(10):
        id = getRandomQuestion()['id']
        addQuestionHelpful(id)
    # prime some Helpful responses
    for i in range(5):
        id = getRandomQuestion()['id']
        addQuestionNotHelpful(id)
        
# Return all questions from faq_data
def getQuestion():
    return(faq_data)

# question getter
def getQuestion(id):
    return(faq_data[id])

# Return random question from faq_data
def getRandomQuestion():
    return(random.choice(faq_data))

# Liked Question
def favoriteQuestion():
    best = 0
    bestID = -1
    for question in getQuestion():
        if question['Helpful'] > best:
            best = question['Helpful']
            bestID = question['id']
    return faq_data[bestID]
    
# Least Helpful Question
def badQuestion():
    worst = 0
    worstID = -1
    for question in getQuestion():
        if question['Not Helpful'] > worst:
            worst = question['Not Helpful']
            worstID = question['id']
    return faq_data[worstID]

# Add to helpful for requested id
def addQuestionHelpful(id):
    faq_data[id]['Helpful'] = faq_data[id]['Helpful'] + 1
    return faq_data[id]['Helpful']

# Add to not helpful for requested id
def addQuestionNotHelpful(id):
    faq_data[id]['Not Helpful'] = faq_data[id]['Not Helpful'] + 1
    return faq_data[id]['Not Helpful']

# Print Question
def printQuestion(question):
    print(question['id'], question['Question'], "\n", "Helpful:", question['Helpful'], "\n", "Not Helpful:", question['Not Helpful'], "\n")

# Number of questions
def countQuestion():
    return len(faq_data)

# Test question Model
if __name__ == "__main__": 
    initQuestion()  # initialize questions
    
    # Most helpful and least helpful
    best = favoriteQuestion()
    print("Most Helpful", best['Helpful'])
    printQuestion(best)
    worst = badQuestion()
    print("Least Helpful", worst['Not Helpful'])
    printQuestion(worst)
    
    # Random question
    print("Random Question")
    printQuestion(getRandomQuestion())
    
    # Count of Questions
    print("Question Count: " + str(countQuestion()))