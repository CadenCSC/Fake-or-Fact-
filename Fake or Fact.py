#Caden Read
#L2 CSC

import customtkinter #Imports a custom version of tkinter with better customisation options
import os #Imports the users OS 
import random #Imports the ability for randomization
import tkinter as tk #Imports Tkinter as TK which allows the user to type TK instead of tkinter

root = customtkinter.CTk() #Sets up the main window
root.title("Fake or Fact?") #Sets the text of the title of the main window
root.geometry('1350x800') #Sets the size of thw window in pixels
customtkinter.set_appearance_mode("dark") #Sets the window mode to dark

font_path = os.path.join(os.path.dirname(__file__), "BebasNeue-Regular.ttf") #Uses the OS import to access the users folder that the program is located inside and searches for the file BebasNeue-Regular.ttf
customtkinter.FontManager.load_font(font_path) #Uses the Custom tkinter import to handle importing the font

#Sets the Bebas Neue
Titlefont = customtkinter.CTkFont(family="Bebas Neue", size=100)
Questionfont = customtkinter.CTkFont(family="Bebas Neue", size=60)
Buttonfont = customtkinter.CTkFont(family="Bebas Neue", size=35)
Scorefont = customtkinter.CTkFont(family="Bebas Neue", size=50)

Titlelbl = customtkinter.CTkLabel(root, text = "Fake or Fact?") #Creates a label on the main window and sets the text to Fake or fact?
Titlelbl.place(relx = 0.5, rely = 0.1, anchor = "center") #Sets the location of the label to 50% of the x pixels, and 10% of the y pixels
Titlelbl.configure(font=Titlefont) #Uses the CTK configure method to set the font of the text to the Titlefont variable

score = 0 #Sets score to 0
scoretxt = customtkinter.CTkLabel(root, text = f"Score: {score}") #Creates the score label and sets the text to score and the value of the score variable
scoretxt.configure(font=Scorefont) #Uses the CTK configure method to set the font of the text to the Titlefont variable
scoretxt.place(relx= 0.85, rely = 0.1)#Sets the location of the label to 85% of the x pixels, and 10% of the y pixels

#List of questions with the key being their true or false answer
question_list= {
        "NASA announced it will send cats to Mars to test their ability to always land on their feet.": False,
        "A penguin won mayoral elections in a small town in Norway.": True,
        "Google plans to replace all search results with AI-generated memes.": False,
        "Scientists trained rats to play miniature golf.": True,
        "A man legally married a burrito in Las Vegas.": False,
        "Taco Bell attempted to buy the Liberty Bell and rename it the Taco Liberty Bell.": True,
        "A squirrel was knighted by the Queen of England.": False,
        "A man in Florida tried to rob a bank using a live alligator.": True,
        "Bananas are now classified as an endangered species.": False,
        "An octopus predicted the outcome of every World Cup match correctly.": True,
        "The Eiffel Tower is secretly a giant Wi-Fi antenna.": False,
        "A baby goat was elected honorary mayor in a Vermont town.": True,
        "The moon was declared a no-sock zone by the UN.": False,
        "A cat led hikers out of a forest when they got lost.": True,
        "The sun was recently copyrighted by a social media influencer.": False,
        "A potato chip shaped like Elvis sold for $1.2 million.": True,
        "A dolphin was appointed head of security at an aquarium.": True,
        "New Zealand declared itself a unicorn sanctuary.": False,
        "Elon Musk bought the moon to turn it into a luxury resort.": False,
        "A town banned time travel after multiple paradoxes occurred.": True,
        "The Great Wall of China is actually a giant noodle.": False,
        "A man built a real-life Iron Man suit using kitchen appliances.": True,
        "Russia developed a weather control machine shaped like a bear.": False,
        "An artist created a sculpture of air and sold it for $18,000.": True,
        "A cheese wheel was elected sheriff in Wisconsin.": False,
        "A dog received an honorary degree from a university.": True,
        "France passed a law making croissants mandatory at breakfast.": False,
        "A woman married a roller coaster in an official ceremony.": True,
        "Cats can now apply for driver’s licenses in Liechtenstein.": False,
        "A group of hamsters ran a successful lemonade stand.": True,
        "McDonald's launched a new sandwich made entirely of lettuce.": False,
        "A duck was found floating on a pizza box across the Atlantic.": True,
        "Dolphins are now legally considered citizens in Portugal.": False,
        "A man lived in IKEA for two weeks without anyone noticing.": True,
        "A teenager built a working time machine out of old microwaves.": False,
        "An AI was elected to a city council in Japan.": True,
        "Kangaroos have been discovered to speak fluent Morse code.": False,
        "A town in Nebraska outlawed forks in favor of chopsticks.": False,
        "A parrot testified in court as a witness.": True,
        "An old woman trained bees to dance on command.": True,
        "The US is replacing the national anthem with a TikTok remix.": False,
        "A bird flew from Canada to Brazil wearing a GoPro.": True,
        "Pizza was declared a vegetable in one US school district.": True,
        "An astronaut grew potatoes on the International Space Station.": True,
        "A highway in Germany was paved with recycled chocolate.": False,
        "An elephant learned to paint portraits of tourists.": True,
        "A cow escaped from a slaughterhouse and became a model.": True,
        "The UK switched driving sides every Wednesday for equality.": False,
        "A village holds an annual worm-charming competition.": True,
        "A cheese company made a 10-foot-tall statue of cheddar Jesus.": False,
        "A horse enrolled in an online college course.": True,
        "Scientists discovered a species of fish that can sing jazz.": False,
        "An ice cream flavor was created to taste like sadness.": True,
        "A crow was caught stealing credit cards in a mall.": True,
        "A sandwich museum opened in a submarine.": False,
        "The moon is shrinking due to global warming.": False,
        "Someone won the lottery using numbers from a fortune cookie.": True,
        "A robot monk gives spiritual advice in a Buddhist temple.": True,
        "A squirrel invented a new method of planting trees.": False,
        "A man tried to pay his taxes using Monopoly money.": True,
        "A vending machine dispenses jokes instead of snacks.": True,
        "Aliens signed a peace treaty with Iceland in 1997.": False,
        "A duck ran for president in Canada.": True,
        "A town passed a law requiring everyone to smile on Mondays.": True,
        "A fish drove a tiny submarine in a lab experiment.": True,
        "Balloons are now banned in Antarctica to protect penguins.": True,
        "A kangaroo was caught sneaking into movie theaters.": True,
        "A goat opened a yoga studio in San Francisco.": False,
        "A chef cooked a meal using only solar power and mirrors.": True,
        "A town was taken over by cats for one whole day.": True,
        "The Eiffel Tower was turned upside down as a prank.": False,
        "NASA sent pizza dough to space to test zero-gravity baking.": True,
        "A banana peel was elected to city council as a joke candidate.": False,
        "A rooster became famous for painting with its beak.": True,
        "A haunted toaster was put up for auction and sold for $3,000.": True,
        "A mayor in Texas declared “No Pants Day” an official holiday.": True,
        "All clowns in Italy went on strike at once.": False,
        "A bear learned to juggle at a circus retirement center.": True,
        "A snail won a national race after a caffeine boost.": True,
        "A scientist taught ants to play checkers.": False,
        "A celebrity opened a museum of their own facial expressions.": True,
        "The internet was briefly shut down to let it “rest.”": False,
        "Pineapples were banned in a town for being “too tropical.”": False,
        "A fish museum built entirely underwater opened in Fiji.": True,
        "A man balanced 12 watermelons on his head while skateboarding.": True,
        "The world’s smallest zoo fits inside a shoebox.": True,
        "An opera was composed entirely using cat meows.": True,
        "A farmer trained cows to respond to TikTok dances.": False,
        "A couple got married on a rollercoaster mid-loop.": True,
        "Scientists discovered a tree that screams when cut.": True,
        "A new sport called “extreme ironing” is now Olympic-qualified.": False,
        "A camel became TikTok-famous for its dramatic sneezes.": True,
        "A rat earned a medal for bravery after sniffing out landmines.": True,
        "The government proposed replacing passports with DNA tattoos.": False,
        "A town in Australia elected a dog as mayor for 5 years.": True,
        "A robot broke a chess player's finger during a match.": True,
        "NASA confirmed the sun is actually a portal to another dimension.": False,
        "An iguana was discovered living in a McDonald’s salad bar.": False,
        "An artist turned 1,000 jellybeans into a working car engine.": False,
        "A jellyfish was taught how to solve mazes in a lab.": True,
        "A ghost was hired to work night security at a museum.": False,
        "The moon is made of cheese, but only in Switzerland.": False
    }

def random_question(): #Function for random_question
    global correct_answer, Questionlbl #Sets the variables 
    random_question = random.choice(list(question_list.keys())) #Uses the random import to pick a random question and key from the question_list dictionary
    correct_answer = question_list[random_question] #It sets the correct answer

    if "Questionlbl" in globals(): #Checks if the Questionlabel is already created and at the global level not at the function level. This is done to make sure its not created multiple times.
        Questionlbl.configure(text = random_question) #Changes the text of the questionlbl  
    else:
        Questionlbl = customtkinter.CTkLabel(root, text=random_question, text_color="white", wraplength=800, justify="center") #Sets up the Questionlbl function as text and configures it
        Questionlbl.configure(font=Questionfont) #Uses the CTK configure method to set the font of the text to the Titlefont variable
        Questionlbl.place(relx = 0.5, rely = 0.3, anchor = "center") #Places the questionlbl at the correct place. 

def fakeclicked():
    global score #sets the score variable to global so it can be accessed and change outside of the function

    answer_window = customtkinter.CTkToplevel(root) #Creates a new window ontop of the old window
    answer_window.title("ANSWER") #Sets the title of the window
    answer_window.transient(root) #Makes the window be associated with the root window
    answer_window.grab_set() #Makes it so the user has to interact with this window before the main window.

    answer_window.geometry('300x200') #Sets the Size of the window

    if correct_answer == False: #Checks if the users answer is the same as the one in the dictionary of questions.
        score += 1 #Adds 1 to the score variable
        latest_answer = "CORRECT" #Sets the latest answer varible to correct
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer) #Makes text on the answer window and sets the text to the latest answer varibale.
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center") #Places the aswrlbl text in the center of the window
        scoretxt.configure(text = f"Score: {score}") #Changes the text of the score variable.
    else:
        latest_answer = "INCORRECT" #Sets the latest answer varible to incorrect
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer) #Makes text on the answer window and sets the text to the latest answer varibale.
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center") #Places the aswrlbl text in the center of the window

    random_question() #Runs the random question function to get a new question

def factclicked():
    global score #sets the score variable to global so it can be accessed and change outside of the function

    answer_window = customtkinter.CTkToplevel(root) #Creates a new window ontop of the old window
    answer_window.title("ANSWER") #Sets the title of the window
    answer_window.transient(root) #Makes the window be associated with the root window
    answer_window.grab_set() #Makes it so the user has to interact with this window before the main window.


    answer_window.geometry('300x200') #Sets the size of the window
 
    if correct_answer == True: #Checks if the users answer is the same as the one in the dictionary of questions.
        score += 1 #Adds 1 to the score variable
        latest_answer = "CORRECT" #Sets the latest answer varible to correct
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer) #Makes text on the answer window and sets the text to the latest answer varibale.
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center") #Places the aswrlbl text in the center of the window
        scoretxt.configure(text = f"Score: {score}") #Changes the text of the score variable.
    else:
        latest_answer = "INCORRECT" #Sets the latest answer varible to incorrect
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer) #Makes text on the answer window and sets the text to the latest answer varibale.
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center") #Places the aswrlbl text in the center of the window

    random_question() #Runs the random question function to get a new question

def buttons(): #Create the button function
    btnfake = customtkinter.CTkButton(root, text = "FAKE" , text_color = "White", command=fakeclicked) #Sets up the fake button with the text fake and sets the command of it to the fakeclicked fucntion
    btnfake.configure(fg_color = "Red", width = 400, height = 80, font=Buttonfont) #Configures the fake button to be red and sets its font to Buttonfont
    btnfake.pack( padx=  200, pady = 40) #Adds padding around the button so its not just the size of the text
    btnfake.place(relx = 0.1, rely = 0.8, anchor = "w") #Places the button in the correct place and sets its anchor to the west side of the button

    btnfact = customtkinter.CTkButton(root, text = "FACT", text_color = "White", command=factclicked) #Sets up the fact button with the text fact and sets the command of it to the factclicked fucntion
    btnfact.configure(fg_color = "Green", width = 400, height = 80, font=Buttonfont) #Configures the fact button to be red and sets its font to Buttonfont
    btnfact.pack( padx=  200, pady = 40) #Adds padding around the button so its not just the size of the text
    btnfact.place(relx = 0.9, rely = 0.8, anchor = "e") #Places the button in the correct place and sets its anchor to the east side of the button

buttons() #Runs the button function
random_question() #Runs the random question function

root.mainloop() #Runs the root window