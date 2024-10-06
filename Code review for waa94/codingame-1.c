// # Coding with reflexion

// ## Power of Thor

// _here his a link to CodinGame to use this solution :_
// [CodinGame](https://www.codingame.com/)

// **Here is the second version of my code following the review :** I have added
// the link above, revised the paragraphs for a clearer explanation of my
// errors, included a two-dimensional image of Thor's movement, corrected the
// labeling issue, and added comments to better explain the conditions and
// Thor's movement at each iteration.

// ### Pre writting


// Firstly, I had to understand the problem. To do that, I always write what
// information I have and what information I want in the output. In this case, I
// have to help Thor reach his light with 2-dimensional coordinates. Then, with
// that in front of my eyes, I search for what I need here it's a comparison
// tool with "if" and "else if" to adjust the coordinates with the right
// conditions. To allow that, I first create a basic pseudocode, and then ideas
// become more precise to form the final pseudocode, such as storing the initial
// coordinates in other variables or using pointers to assign the direction.
// Then, I write with a high-level language here it's C and I test the code.
// Most of the time my codes doesn’t work on the first try. Here had an error
// with the direction printing instruction. In fact I wrote the coordinates in
// the wrong order, because I printed the X before the Y. The first two tests
// worked because it was just a straight line but not the diagonal ones. So I
// just had to reverse that, and the code was okay for all the tests.

// **The goal of the program here is to allow at the end of each iteration, that
// thor approaches the light using its coordinates**
//
// ![pre writting](pseudocode.jpg)<img style="caret-color: initial;" src="direction_Thor_game.jpg" alt="pre writting" width="205" height="273">

// ### Pseudocode
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
//print the direction ( , ) 




#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>    



int main()
{


    // the X position of the light of power 
    int light_x;

      
    // the Y position of the light of power
    int light_y;

    // Thor's starting X position
    int initial_tx;
    // Thor's starting Y position
    int initial_ty;
    scanf("%d%d%d%d", &light_x, &light_y, &initial_tx, &initial_ty);
    
    //w init position of thor 
    int ThorX = initial_tx;
    int ThorY = initial_ty;      
   

    // game loop
   while (1) 
    {
        // The remaining amount of turns Thor can move.
        int remaining_turns;
        scanf("%d", &remaining_turns);
        char *directionX = "";
        char *directionY = "";

        if (ThorY < light_y) // If Thor position is less far in Y (in South) than light position
        {
            directionY = "S"; // Thor must move to South
            ThorY ++;
        }

        else if (ThorY > light_y)  // If Thor position is far in Y (in North) than light position
        {
            directionY = "N"; // Thor must move to North
            ThorY --;      
        }

        if (ThorX < light_x)  // If Thor position is less far in X (in Est) than light position
        {
            directionX = "E"; // Thor must move to Est  
            ThorX ++;
        }
        
        else if (ThorX > light_x)  // If Thor position is far in X (in West) than light position
        {
            directionX = "W"; // Thor is must move to West    
            ThorX --;      
        
             
        //
        // A single line providing the move to be made: N NE E SE S SW W or NW
    
        }

        printf("%s%s\n", directionY, directionX); // regarding the condition, Thor is going to move N NE E SE S SW W or NW
    }
    
    

    return 0;

}