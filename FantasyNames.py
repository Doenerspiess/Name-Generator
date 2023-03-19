# fantasy name generator 0.1 #


import string
import random
import tkinter as tk
from tkinter import ttk
#from tkinter.ttk import *
from ttkthemes import ThemedTk


fantasy = 1 # determines how "fantasyesque" the name should be. 0 = normal, 10 = very fantastic
gender = 1 # determines how male (1) or female (10) the name should be. Values around 5 should give fairly unisex names
language = 'a' # 'e' = use english names as basis, 'd' = use german names as basis; every other character: Use both languages as basis
NumberOfNames = 1 # define how many names should be generated

#s = tk.ttk.Style()
#print(s.theme_names())
#s.theme_use('clam')

# Create the GUI
root = ThemedTk(themebg=True)
#print(root.get_themes())
root.set_theme('breeze')
#root = tk.Tk()
root.title("Fantasy Name Generator")
root.geometry("400x600")

# Create a menu which lets you choose the language
label = ttk.Label(root, text="Select a language")
label.pack()

def lang(event):
    global language
    language = langs.get()[0]

langs = tk.StringVar()
menu = ttk.Combobox(root, textvariable = langs)
menu['values'] = ['ger', 'eng', 'all']
menu['state'] = 'readonly'
menu.pack(fill=tk.X, padx = 5, pady = 5)
menu.bind('<<ComboboxSelected>>', lang)
root.config(menu=menu)

#placeholder
label = ttk.Label(root, text="")
label.pack(pady=1)

# Create a slider for the "fantasyness"
label = ttk.Label(root, text="How fantasyesque should the name be?")
label.pack()
FanSlider = ttk.Scale(root, from_=1, to=9, orient=tk.HORIZONTAL, length=200)
FanSlider.pack(pady=5)
# Create a label to display the selected value

# Function to update the label with the selected value
def update_fan(val):
    global fantasy
    fantasy = val
    fantasy = float(fantasy)
    fantasy = int(fantasy)
# Bind the slider's value to the label text
FanSlider.config(command=update_fan)

#placeholder
label = ttk.Label(root, text="")
label.pack(pady=1)

# Create a slider for the gender
label = ttk.Label(root, text="gender")
label.pack()
GenSlider = ttk.Scale(root, from_=1, to=9, orient=tk.HORIZONTAL, length=200)
GenSlider.pack(pady=5)
# Create a label to display the selected value
label = ttk.Label(root, text="male                                     female")
label.pack()
# Function to update the label with the selected value
def update_gen(val):
    global gender
    gender = float(val)
    gender = int(gender)
# Bind the slider's value to the label text
GenSlider.config(command=update_gen)

#placeholder
label = ttk.Label(root, text="")
label.pack(pady=1)

# Create a field in which the amount of names to be generated can be entered
label = ttk.Label(root, text="Number of Names to generate:")
label.pack(pady=5)

# Create an entry widget for the user to enter an integer
NameNumber = ttk.Entry(root, width=20)
NameNumber.pack(pady=10)



# define globale variables and data

vowels = ['a', 'e', 'i', 'o', 'u', 'y'] # y is used as a vowel here ("fantasy-y" :) )
vowelWeights = [2, 1.5, 1.3, 0.4, 0.7, 1] # higher value = more "female", lower value = more "male"

VOWELS = [letter.upper() for letter in vowels] # uppercase vowels

alphabet = string.ascii_lowercase  # get all letters of the alphabet in lowercase
vows = "aeiouy"  # define a string with all vowels
consonants = [letter for letter in alphabet if letter not in vows]  # generate a list of all letters that are not vowels
CONSONANTS = [letter.upper() for letter in consonants] # uppercase consonants
    
# list of male first names
e_mNames = ['Adam', 'Alex', 'Andrew', 'Anthony', 'Austin', 'Benjamin', 'Bradley', 'Brandon', 'Brian', 'Caleb', 'Charles', 'Christian', 'Christopher', 'Daniel', 'David', 'Derek', 'Dominic', 'Dylan', 'Edward', 'Elijah', 'Eric', 'Ethan', 'Evan', 'Frank', 'Gabriel', 'George', 'Grant', 'Gregory', 'Henry', 'Isaac', 'Jacob', 'James', 'Jason', 'Jeffrey', 'Jeremy', 'Jesse', 'John', 'Jonathan', 'Jordan', 'Joseph', 'Joshua', 'Justin', 'Keith', 'Kenneth', 'Kevin', 'Kyle', 'Larry', 'Logan', 'Lucas', 'Mark', 'Matthew', 'Maxwell', 'Michael', 'Nathan', 'Nicholas', 'Noah', 'Oliver', 'Oscar', 'Patrick', 'Paul', 'Peter', 'Philip', 'Quentin', 'Raymond', 'Richard', 'Robert', 'Ryan', 'Samuel', 'Scott', 'Sean', 'Stephen', 'Steven', 'Taylor', 'Thomas', 'Timothy', 'Travis', 'Trevor', 'Tyler', 'Victor', 'Vincent', 'Wesley', 'William', 'Zachary', 'Aiden', 'Brady', 'Cole', 'Dante', 'Eddie', 'Felix', 'Gavin', 'Hector', 'Isaiah', 'Jonah', 'Kaden', 'Landon', 'Miles', 'Nolan', 'Peter', 'Ricky', 'Simon', 'Tanner', 'Walter', 'Zane']
d_mNames = ['Andreas', 'Anton', 'Alexander', 'Bruno', 'Benjamin', 'Bernd', 'Christian', 'Daniel', 'David', 'Dominik', 'Erik', 'Felix', 'Florian', 'Franz', 'Frederik', 'Georg', 'Hans', 'Heinrich', 'Jakob', 'Jan', 'Johann', 'Jonas', 'Jonathan', 'Julian', 'Jürgen', 'Karl', 'Klaus', 'Lars', 'Lukas', 'Manuel', 'Marcel', 'Markus', 'Martin', 'Max', 'Moritz', 'Nico', 'Niklas', 'Oliver', 'Oskar', 'Paul', 'Peter', 'Philipp', 'Ralf', 'Robert', 'Roland', 'Sebastian', 'Stefan', 'Thomas', 'Tim', 'Thorsten', 'Tobias', 'Uwe', 'Volker', 'Werner', 'Wolfgang', 'Arne', 'Björn', 'Carsten', 'Dennis', 'Enno', 'Fiete', 'Gerd', 'Henrik', 'Ingo', 'Janik', 'Karim', 'Kjell', 'Leif', 'Lorenz', 'Matthias', 'Nils', 'Peer', 'Rainer', 'Till', 'Tilo']

# list of female first names
e_fNames = ['Abigail', 'Alexandra', 'Alyssa', 'Amanda', 'Amber', 'Amy', 'Angela', 'Anna', 'Ashley', 'Bethany', 'Brittany', 'Caroline', 'Cassandra', 'Catherine', 'Chelsea', 'Christina', 'Claire', 'Crystal', 'Danielle', 'Elizabeth', 'Emily', 'Emma', 'Erica', 'Erin', 'Gabrielle', 'Hailey', 'Hannah', 'Heather', 'Isabella', 'Jacqueline', 'Jasmine', 'Jennifer', 'Jessica', 'Jocelyn', 'Jordan', 'Julia', 'Julie', 'Kaitlyn', 'Karen', 'Katherine', 'Kathryn', 'Kayla', 'Kelly', 'Kelsey', 'Kimberly', 'Lauren', 'Leah', 'Lillian', 'Lindsey', 'Madeline', 'Makayla', 'Maria', 'Mary', 'Megan', 'Melanie', 'Melissa', 'Morgan', 'Natalie', 'Nicole', 'Olivia', 'Paige', 'Rachel', 'Rebecca', 'Samantha', 'Sarah', 'Savannah', 'Shannon', 'Shelby', 'Sierra', 'Stephanie', 'Sydney', 'Tiffany', 'Vanessa', 'Victoria', 'Whitney', 'Zoe', 'Ariel', 'Brianna', 'Carly', 'Destiny', 'Elena', 'Giselle', 'Jenna', 'Kylie', 'Lana', 'Mia', 'Nadia', 'Nina', 'Penelope', 'Raquel', 'Sabrina', 'Sofia', 'Summer', 'Tara', 'Valerie']
d_fNames = ['Alexandra', 'Alina', 'Amelie', 'Anja', 'Anna', 'Anne', 'Annika', 'Agnes', 'Barbara', 'Bianca', 'Carina', 'Carla', 'Carolin', 'Claudia', 'Diana', 'Doris', 'Daphne', 'Elisabeth', 'Ella', 'Ellen', 'Emily', 'Emma', 'Elsa', 'Franziska', 'Gabi', 'Hanna', 'Helena', 'Ines', 'Isabell', 'Jana', 'Janina', 'Jasmin', 'Jennifer', 'Johanna', 'Julia', 'Karin', 'Katharina', 'Katja', 'Kerstin', 'Klara', 'Laura', 'Lea', 'Lisa', 'Maren', 'Maria', 'Marie', 'Marlene', 'Marina', 'Martina', 'Melanie', 'Nina', 'Petra', 'Renate', 'Sabine', 'Sandra', 'Silke', 'Simone', 'Sophie', 'Stefanie', 'Susanne', 'Tanja', 'Theresa', 'Ulrike', 'Ursula', 'Vanessa', 'Verena', 'Yvonne', 'Bella', 'Celia', 'Elke', 'Fiona', 'Greta', 'Jule', 'Kira', 'Lara', 'Lena', 'Maike', 'Nora', 'Paula', 'Romy', 'Ronja', 'Sina', 'Tina', 'Toni', 'Vera', 'Zara', 'Zoe']

# list of unisex first names
e_uNames = ['Adrian', 'Alexis', 'Avery', 'Cameron', 'Casey', 'Dakota', 'Drew', 'Jamie', 'Jesse', 'Jordan', 'Kendall', 'Logan', 'Morgan', 'Peyton', 'Riley', 'Robin', 'Sage', 'Sam', 'Shawn', 'Sidney', 'Skyler', 'Spencer', 'Taylor', 'Terry', 'Tracy', 'Tyler', 'Valentine', 'Wade', 'Wyatt']
d_uNames = ['Adrian', 'Alex', 'Chris', 'Dominique', 'Jannik', 'Jordan', 'Kai', 'Kim', 'Leandro', 'Leslie', 'Luca', 'Marvin', 'Maxi', 'Micha', 'Milan', 'Nico', 'Noah', 'Pascal', 'Remy', 'Robin', 'Sandy', 'Sascha', 'Sina', 'Toni', 'Valentin', 'Yannick', 'Yannik', 'Yara']

# define list of letter combinations which are "forbidden" because they are too hard to pronounce or make no sense:
forbidden = ["zf", "bhf", "bhg", "hzh", "hgf", "tdd", "iij", "xxx", "www", "zzz", "jgj", "jjj", "iii", "uuu", "aaa", "yyy", "ooo", "eee", "rrr", "vvv", "cbh", "cb", "nlm", "stq", "hhh", "hh", "bdj" "tdp", "mbp", "csv", "vw", "nh", "zgf", "cd", "bkl", "px", "xp", "xf", "lx", "xl", "xk", "kx", "mx", "nx", "fx", "gx", "hx", "dx", "cx", "jx", "px", "qx", "sx", "tx", "vx", "wx", "zx"]
forbiddenEnd = ["sss", "xb", "xc", "xd", "xf", "xg", "xh", "xj", "xk", "xl", "xm", "xn", "xp", "xq", "xr", "xs", "xt", "xv", "xw", "xz", "dr", "kr", "kz", "pr", "dz", "cr", "br", "gr", "hr", "lr", "mr", "nr", "qr", "sr", "tr", "vr", "wr", "zr", "bz", "cz", "gz", "hz", "jz", "pz", "qz", "sz"]
forbiddenStart = ["Ft", "Ng", "Qr", "Rq", "Mg", "Lc", "Bp", "Pb", "Lk", "Lb", "Ld", "Lf", "Lg", "Lh", "Lj", "Lm", "Ln", "Lp", "Lq", "Lr", "Ls", "Lt", "Lv", "Lw", "Lx", "Lz"]
for i in forbidden:
    forbiddenStart.append(i[0].upper() + i[1:len(i)])
for i in range (len(consonants)): # define all double letters as forbidden starts
    forbiddenStart.append(CONSONANTS[i]+consonants[i])
    if i < len(vowels):
        forbiddenStart.append(VOWELS[i]+vowels[i])

for i in forbiddenStart:
    forbidden.append(i)
#print(forbidden)

testcounter = 0

def vow(uppercase, end):
    vowelCommonness = [1, 0.9, 0.8, 0.5, 0.6, 0.3]
    if end == 1:
        endfactor = 1.5
    else:
        endfactor = 1
    weights = []
    vowelCommonness = [x**((9-fantasy)/9) for x in vowelCommonness]
    for i in vowelWeights:
        weights.append((i**((gender-5)/4))**endfactor)
    weights = [100*x for x in weights]
    weights = [a*b for a,b in zip(weights, vowelCommonness)]
    vowSum = 0
    for i in weights:
        vowSum = vowSum + i
    select = random.randint(0, int(vowSum))
    c = 1
    while c < len(weights):
        weights[c] = weights[c] + weights[c-1]
        c = c+1
    for x in range(len(weights)):
        if select <= weights[x]:
            if uppercase == 1:
                return vowels[x].upper()
            else:
                return vowels[x]

def cons(uppercase):
    consonantCommonness = [0.02, 0.03, 0.04, 0.02, 0.01, 0.06, 0.04, 0.03, 0.19, 0.11, 0.2, 0.02, 0.002, 0.09, 0.09, 0.07, 0.02, 0.01, 0.01, 0.01]
    weights = []
    consonantCommonness = [x**((9-fantasy)/9) for x in consonantCommonness]
    #print(consonantCommonness)
    #for i in vowelWeights:
     #   weights.append((i**((gender-5)/4))**endfactor)
    #weights = [100*x for x in weights]
    #weights = [a*b for a,b in zip(weights, vowelCommonness)]
    for p in consonantCommonness:
        weights.append(p*1000)
    conSum = 0
    for i in weights:
        conSum = conSum + i
    select = random.randint(0, int(conSum))
    c = 1
    while c < len(weights):
        weights[c] = weights[c] + weights[c-1]
        c = c+1
    #print(len(weights))
    for x in range(len(weights)):
        if select <= weights[x]:
            if uppercase == 1:
                #print(consonants[x].upper())
                return consonants[x].upper()
            else:
                return consonants[x]
    
for i in range(100):
    cons(1)

def generate_names():
    NumberOfNames = NameNumber.get()
    if not NumberOfNames.isnumeric():
        output.config(text = "Please provide a valid number of names to generate")
        return
    NumberOfNames = int(NumberOfNames)
    global testcounter
    nameList = []

    for n in range(NumberOfNames):
        if language == 'e':
            if gender < 3:
                name = random.choice(e_mNames)
            elif gender >= 3 and gender < 5:
                name = random.choice(random.choice([e_mNames, e_uNames]))
            elif gender == 5:
                name = random.choice(random.choice([e_mNames, e_uNames, e_fNames]))
            elif gender >= 6 and gender < 8:
                name = random.choice(random.choice([e_fNames, e_uNames]))
            else:
                name = random.choice(e_fNames)

        elif language == 'd':
            if gender < 3:
                name = random.choice(d_mNames)
            elif gender >= 3 and gender < 5:
                name = random.choice(random.choice([d_mNames, d_uNames]))
            elif gender == 5:
                name = random.choice(random.choice([d_mNames, d_uNames, d_fNames]))
            elif gender >= 6 and gender < 8:
                name = random.choice(random.choice([d_fNames, d_uNames]))
            else:
                name = random.choice(d_fNames)
        else:
            #No language selected, use all names
            if gender < 3:
                name = random.choice(random.choice([e_mNames, d_mNames]))
            elif gender >= 3 and gender < 5:
                name = random.choice(random.choice([d_mNames, d_uNames, e_mNames, e_uNames]))
            elif gender == 5:
                name = random.choice(random.choice([d_mNames, d_uNames, d_fNames, e_mNames, e_uNames, e_fNames]))
            elif gender >= 6 and gender < 8:
                name = random.choice(random.choice([d_fNames, d_uNames, e_fNames, e_uNames]))
            else:
                name = random.choice(random.choice([e_fNames, d_fNames]))

        #print(name)
        length = len(name)

        for i in range(fantasy):
            replace = random.randint(0, length-1)
            if replace == length - 1:
                endChar = 1
            else:
                endChar = 0
            oldName = name
            if replace == 0:
                if name[replace] in CONSONANTS:
                    name = name[0:replace] + cons(1) + name[replace+1:length]
                else:
                    name = name[0:replace] + vow(1, endChar) + name[replace+1:length]

            elif name[replace] in consonants:
                name = name[0:replace] + cons(0) + name[replace+1:length]

            else:
                name = name[0:replace] + vow(0, endChar) + name[replace+1:length]
                
            for end in forbiddenEnd: # check for forbidden endings
                if name[(len(name)-len(end)):(len(name))] == end:
                    name = oldName
                    testcounter = testcounter + 1
                    i = i-1
            for x in forbidden: # check for forbidden letter combinations
                if x in name:
                    name = oldName
                    testcounter = testcounter + 1
                    i = i-1
        #print(name)
        nameList.append(name)
    
    #print("Forbidden violations detected: " + str(testcounter))

    #print(nameList)
    output.config(text = nameList)
    #output.insert(tk.END, "\n")
    
button = ttk.Button(root, text="GENERATE", command=generate_names)
button.place(x=150, y=320)
button.pack(pady=5)

# Create a window to display the generated names
output = ttk.Label(root, width = 30, text = "", wraplength = 250, font = ("Arial", 14), anchor="center")
#output.place(x= 35, y=370)
output.pack(pady=15)


root.mainloop()

