import tkinter as tk
import customtkinter
import os
import random

root = customtkinter.CTk()
root.title("Fake or Fact?")
root.geometry('1350x800')
customtkinter.set_appearance_mode("dark")

def titlerectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        (x1+radius, y1), (x-radius, y1),
        (x2, y1), (x2, y1+radius),          
        (x2, y2-radius), (x2, y2),           
        (x2-radius, y2), (x1+radius, y2),    
        (x1, y2), (x1, y2-radius),           
        (x1, y1+radius), (x1, y1) 
    ]


font_path = os.path.join(os.path.dirname(__file__), "BebasNeue-Regular.ttf")
customtkinter.FontManager.load_font(font_path)

Titlefont = customtkinter.CTkFont(family="Bebas Neue", size=100)
Questionfont = customtkinter.CTkFont(family="Bebas Neue", size=60)
Buttonfont = customtkinter.CTkFont(family="Bebas Neue", size=35)
Scorefont = customtkinter.CTkFont(family="Bebas Neue", size=50)


Titlelbl = customtkinter.CTkLabel(root, text = "Fake or Fact")
Titlelbl.place(relx = 0.5, rely = 0.1, anchor = "center")
Titlelbl.configure(font=Titlefont)

score = 0
scoretxt = customtkinter.CTkLabel(root, text = f"Score: {score}")
scoretxt.configure(font=Scorefont)
scoretxt.place(relx= 0.85, rely = 0.1)


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

def random_question():
    global correct_answer, Questionlbl
    random_question = random.choice(list(question_list.keys()))
    correct_answer = question_list[random_question]

    if "Questionlbl" in globals():
        Questionlbl.configure(text = random_question)
    else:
        Questionlbl = customtkinter.CTkLabel(root, text=random_question, text_color="white", wraplength=800, justify="center")
        Questionlbl.configure(font=Questionfont)
        Questionlbl.place(relx = 0.5, rely = 0.3, anchor = "center")


def fakeclicked():
    global score

    answer_window = customtkinter.CTkToplevel()
    answer_window.title("ANSWER")
    if correct_answer == False:
        score += 1
        latest_answer = "CORRECT"
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer)
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center")
        scoretxt.configure(text = f"Score: {score}")
    else:
        score += 0
        latest_answer = "INCORRECT"
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer)
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center")

    random_question()

def factclicked():
    global score

    answer_window = customtkinter.CTkToplevel()
    answer_window.title("ANSWER")

    if correct_answer == True:
        score += 1
        latest_answer = "CORRECT"
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer)
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center")
        scoretxt.configure(text = f"Score: {score}")
    else:
        score += 0
        latest_answer = "INCORRECT"
        aswrlbl = customtkinter.CTkLabel(answer_window, text = latest_answer)
        aswrlbl.place(relx = 0.5, rely = 0.3, anchor = "center")

    random_question()

def buttons():
    btnfake = customtkinter.CTkButton(root, text = "FAKE" , text_color = "White", command=fakeclicked)
    btnfake.configure(fg_color = "Red", width = 400, height = 80, font=Buttonfont)
    btnfake.pack( padx=  200, pady = 40)
    btnfake.place(relx = 0.1, rely = 0.8, anchor = "w")

    btnfact = customtkinter.CTkButton(root, text = "FACT", text_color = "White", command=factclicked)
    btnfact.configure(fg_color = "Green", width = 400, height = 80, font=Buttonfont)
    btnfact.pack( padx=  200, pady = 40)
    btnfact.place(relx = 0.9, rely = 0.8, anchor = "e")

buttons()
random_question()

root.mainloop()