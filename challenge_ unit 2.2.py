#Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. 
#Define the player class
class player:
  def play (self):
         print ("The player is playing cricket.")
# Define the batsman class,derived from player
class Batsman (player):
      def play (self):
             print ("The batsman is batting.")
 #Define the bowler class, dervied from player
class bowlaer (player):
        def play (self):
            print("The bowler is bowling.")
# create objects of batsmans and bowler classes
batsman = Batsman()
bowler =  bowler()
   #call the play() method for each object
batsman. play()
bowler . play()