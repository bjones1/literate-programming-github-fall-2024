// # <u>Coding with reflexion<u></u></u>
//
// <u><u>

// <h2>Power of Thor</h2>



// <h3>Pre writting</h3>


// <p>Firstly, I had to understand the problem. To do that, I always write what information I have and what information I want in the output. In this case, I have to help Thor reach his light with 2-dimensional coordinates. Then, with that in front of my eyes, I search for what I need here it's a comparison tool with "if" and "else if" to adjust the coordinates with the right conditions. To allow that, I first create a basic pseudocode, and then ideas become more precise to form the final pseudocode, such as storing the initial coordinates in other variables or using pointers to assign the direction. Then, I write with a high-level language here it's C and I test the code. Most of the time it doesn’t work on the first try, so I read the error message, and it said that my letters for the direction weren’t in the right order because I printed the X before the Y. The first two tests worked because it was just a straight line but not the diagonal ones. So I just had to reverse that, and the code was okay for all the tests.</p><p>ROA: The pre-writing section is clear, explaining the problem and the approach. However, I didn't understand the type of error concerning the coordinates order. Perhaps next time you could put a screenshot of this error along side the code generating it.</p>
// <p><strong>The goal of the program here is to allow at the end of each iteration, that thor approaches the light using its coordinates</strong></p><p><img src="pseudocode.jpg" alt="pre writting"></p><p>ROA: This is a good resume of the problem. I would suggest drawing a two dimensional graph to get a better image of how Thor should move.</p><h3>Pseudocode</h3>

//thorX ← initialTX
//thorY ← initialTY
//while(infinit loop) 
	
//	directionX ← E, W
//	directionY ← S,N
//	if (thorY > lightY)
//		directionY ← N
//		thorY --
//	else if (thorY > lightY) 
//		directionY ← S
//		thorY ++
//	
//	if (thorX > lightX) 
//		directionX ← W
//		thorX --
//	else if (thorX < lightX) 
//		directionX ← E
//		thorX ++
	
//	print the direction ( , )
// <p>ROA: The pseudocode is clear and complete, providing a step-by-step guide to solving the problem.</p>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>    // the X position of the light of power


int main()
{

    // <p>the Y position of the light of power</p>
    int light_x;
    // <p>Thor's starting X position</p>
    int light_y;

    // <p>ROA: I think there has been a typo, you labeled the variable light_x with "Y position" and same for light_y and initial_tx. Maybe this why you had a problem in your coordinates order.</p><p>Thor's starting Y position</p>
    int initial_tx;

    int initial_ty;
    scanf("%d%d%d%d", &light_x, &light_y, &initial_tx, &initial_ty);
    
    //w init position of thor 
    int ThorX = initial_tx;
    int ThorY = initial_ty;    // game loop 

   // <p>The remaining amount of turns Thor can move. ROA: I think this comment was meant to be directly above the remaining_turns variable.</p><p>ROA: Overall, the variable names are clear and descriptive, and the input is correctly parsed. However, I see that a lot of them are not correctly labeled or their label isn't in the correct place. Same goes for game loop, we think that the comment //game loop is for the variable ThorY and not announcing the start of the game loop.</p>
   while (1) 
    {

        int remaining_turns;
        scanf("%d", &remaining_turns);
        char *directionX = "";
        char *directionY = "";

        if (ThorY < light_y)
        {
            directionY = "S";
            ThorY ++;
        }

        else if (ThorY > light_y)
        {
            directionY = "N";
            ThorY --;      
        }

        if (ThorX < light_x)
        {
            directionX = "E";    
            ThorX ++;
        }
        
        else if (ThorX > light_x)
        {
            directionX = "W";     
            ThorX --;      
        
          
        }
        // <p><strong>ROA</strong>: The code is understandable. I suggest adding more comments describing Thor's movement in every condition and how his position is updated (is he moving south, north, west or east?).</p><p>A single line providing the move to be made: N NE E SE S SW W or NW</p>
        printf("%s%s\n", directionY, directionX);
    }

    return 0;
    // <p><em>here his a link to CodinGame to use this solution :</em> <a href="https://www.codingame.com/">CodinGame</a></p><p>ROA : I would recommand putting the link above.</p></u></u>
}