'''
Create a list of the top 3 places you want to travel to. Then create a while loop to print out that list neatly.

Modify your list so it's a dictionary, and for each place you want to visit add 3 reasons why. 
Then modify your program so that you use both a while loop and a for loop to print out the list of places
For each place, a list of the reasons why you want to visit that place.

Using a while loop, create a program with a counter that starts at 1, then takes that number and doubles it every time the loop runs. 
This while loop should keep going until the counter is greater than or equal to 100,000,000.

'''

places = {'Bali':['Diving', 'Sharks', 'Women'], 'Tamil Nadu':['Yoga', 'Temples', 'Meditation'], 'Singapore':['finance', 'business', 'women']}

for key, value in places.items():
    print('\n',key.title())
    x = 0
    while x < len(value):
        print('  ',value[x].title())
        x += 1    
