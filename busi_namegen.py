import requests
import random

word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()


the_name=''
the_business=''
the_word=''
suggestions=''
number=0


def Name():
   global the_name
   while True:
      your_name=input("What is your name(enter either First or Last Name) :")
      if your_name.isalpha():
         the_name+=your_name
         break
      else:
         print("Please try to use letters from the alphabet!")
   
Name()

def busi():
   global the_business
   while True:
      your_business=input("What is your businesss centered around(Ex:Fishing,Clothes,Sports, etc):")
      if your_business.isalpha():
         the_business+=your_business
         break
      else:
         print("Please try to use letters from the alphabet!")
busi()


def suggest():
   global the_word
   global suggestions
   for word in WORDS:
      gen=random.choice(WORDS).capitalize()
      print(gen.decode('utf-8'))
      happy_or=input("Do you like the word that describes your business? (yes or no or maybe)")
      if happy_or=="yes":
         the_word+=str(gen.decode('utf-8'))
         break
      elif happy_or=="maybe":
         global number 
         suggestions+=str(gen.decode('utf-8'))+"\n"
         number+=1
      if number==5:
         print(suggestions,"\n")
         would_you=input("Which one of the suggestions do you like?")
         if would_you in suggestions:
            the_word+=would_you
            break
         else:
            print("Type the word in the suggestions correctly!")
                
      
            
suggest()

print(the_name,"'s","new business name will be:",the_name,"'s",the_word,the_business) 















   
  
      
   



     