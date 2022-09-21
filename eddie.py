import random

greetings = ["Yo","What's going on?","Howdy Partner","What's cookin' good looking","Beep boop, I am a robot""Hi, my name is Eddie. Who are you?"]
goodbyes = ["Smell ya later","See you soon","Goodbye","Speak soon homie"]

keywords = ["Music","pet","book","game","how are you","hi","good"]
responses = ["Music tastes like rainbows","Pets are a life saver","books are tight","Wanna play a game?","I am good","Hello!, how are you","Glad to hear it :)"]

print (random.choice(greetings))
user = input ("Say something (or type bye to quit)")
user = user.lower()

while (user != "bye"):
  keyword_found = False

  for index in range(len(keywords)):
    if (keywords[index] in user):
      print("Bot: " + responses[index])
      keyword_found = True
      
  if (keyword_found == False):
    new_keyword = input("I'm currently learning. Can you tell me what keyword should I respond to")
    keywords.append(new_keyword)
    new_response = input("How should I respond to " + new_keyword + "? ")
    responses.append(new_response)

  user = input("Say something (or type bye to quit): ")
  user = user.lower()

print(random.choice(goodbyes))   
    