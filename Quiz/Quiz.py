from Geography import Geography
from Languages import Languages

subject = input("What subject would you like to do a quiz on?: ")
if(subject == "Geography"):
    Quiz = Geography()
    Quiz.run()
if(subject == "Languages"):
    Quiz = Languages()
    Quiz.run()



