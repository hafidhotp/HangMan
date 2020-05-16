import csv
import random

#opening a file and read the values as list
with open('movies.txt', newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

def movies(data):
	#this function ranodmly picks a movie from the file and return that movie 
	    return (random.choice(data[0]))

def create_qn(picked_movie):
	#this function creates the question using the picked movie
	qn=[]
	for i in range(len(picked_movie)):
		qn.append("_")
		
	return qn

def checking(movie,guess):
    #this function will check whether the user gets the answer
    mod_guess=""
    for j in guess:
        if j!=" ":
            mod_guess+=j
            
    if movie==mod_guess:
        return print("Congrats!!!") ,True  #returning two values
    else:
        return print("Oops.... Try again ") ,False
        

def reveal(letter,movie,qn):
    #this function reveals as such the user inputs letters
    for i in range(len(movie)):
        if letter==movie[i]:
            qn[i]=letter
        else:
            pass
    return qn


#main function
def play():
    picked_movie=movies(data)
    qn=create_qn(picked_movie)
    x=" ".join(qn)
    print(x)
    game_over=False
    while not game_over:
        new=""
        ch=input("guess the movie: ")
        if len(ch)==1:
            letter=ch.upper()
            new_qn=reveal(letter,picked_movie,qn)
            for j in new_qn:
                new+=j+" "
            print(new)
            x,y=checking(picked_movie,new)
            if y==True:
                game_over=True
        else:
            guessed_word=ch.upper()
            x,y=checking(picked_movie,guessed_word)
            if y==True:
                game_over=True
            
play()