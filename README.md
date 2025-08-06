# Flappy Bird Learing Project

**author**: RealVybornak

**email**: <mira.vyborny110@gmail.com>

***

## Description

Here goes the project description.

1. what purpose it serves

    For me it is a new thing to learn and how more programing works, learns me a lot of things. For others it is just a game they can play if they want.

2. how it works

    It is all run in python with the help of modules "random" and "pygame" I have constructed a code that is almost identical to the game Flappy bird expect this one acually goes on infinitly.

3. what are the main features

    Main features are just it works and break rarely. It has bad score tracker that i want to improve by making in-game counter for it to be nicer.

## How to install

_to be implemented later_

## How to Play

Game is simple and almost identical to the game Flappy bird. The game is played with just spacebar for now you can either click or you can hold the spacebar.

## Planned features

1. Textures

    Make so each thing in game has its own drawn sprite and not just a brick.

2. Score counter in game

    A counter that will let the player know how much points does he have.

3. Menu

    Menu in the beginning of the game. It should have settings play button. In setting just make it so you can turn on SFX and music.

4. Speed control

    Speed will increase by the amount of score.

5. Death screen

    When the player dies it will show a menu that will have few different features like "menu" button and "retry" button and more.

6. Spacebar can't be held

    Make so spacebar can't be held and make people break their spacebar.

7. Moving pipes

    At some threshold of points pipes will begin to move up and down.

8. Leaderboard (prob won't happen)

    Leaderboard would be nice doubt much players will be on there but it would be nice to see how is at the top. (seems hard tho)

9. MVC design

    Have no idea what this means but it sounds cool.

10. custom music

    maybe trying to add my own melody that i will play.

## Game parts
  1. Menu
      
    Menu is simple and has just Start button and quit button and that all for now.
    Menu is currently mostly finished it could look nicer in the future but now it's enough. Setting in menu will be worked on after i add sound effects and music because probably that will the only thing in settings.

  2. Gameplay
      
      1. Bird

            Bird works simply with the help of spaceba. Spacebar can either be held or just pressed quickly. It has my try of making it more like the real game but the holding doesn't really help it.
            Bird is kinda in the work right now i want to make it so u cant hold the space bar. Also want to make him some animations se he can like flap his wings when you press space bar.

      2. pipes

            Pipes are both seperate so we have 2 classes upper pipe and lower pipe both spawn at the same time so it look like a 1 big sprite. It probably could be as 1 big sprite, but i fear the gap where the player goes trough, it would kill the player and for now it works so i wont change it. The pipes spawn at random highs with the help of a module "random". 
            Currently pipes are preatty much done they arent buggy so that's nice the only thing planned for the pipes is that they will move up and down after some score.
      
      3. Score system
        
            Score counter works based on collision of the Bird and a pointwall in game pointwall spawn at the same exact time as pipes and it streches from the top to the bottom of the screen. The highest achived score is now also works. At every death the player's the code check if his score is higher than the score he managed to get before. If yes it over-writes the old score in the .txt file named Highest score.
            Score system is now done prob will just make some adjustments for example other sprites like pipes and clouds won't cover the score, but that is a just minor bug. Score system works as it should. It has a bug that i have in mind that i want to fix but it isn't anything game breaking.

  3. Restart mechanism and death screen

    Death screen has only a few things and i probably won't add anything else. It has 2 buttons as the menu. 1st button is menu and 2nd retry, which are kinda self-explainitory. Also it has a text above which says the highest achived score ever.
