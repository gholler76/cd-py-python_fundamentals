# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)  # with a comma
print("Hello"+name)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)  # with a comma
# print("Hello" + name)  # with a +	-- this one should give us an error!
print(f"Hello {name}")  # fixed line 10 by using f string to add the integer
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string

all_caps = "mf doom"
print(all_caps.upper())  # converts a string to all upper case

# counts how many times the (substring) appears in the called string
food = "bananarama"
print(food.count("na"))

pile = "haystackhaystackhaystackhaystackhaystackneedlehaystackhaystack"
# finds the index position where the (substring) starts
print(pile.find("needle"))

scream = "BE QUIET"  # converts a string to all lower case
print(scream.lower())
