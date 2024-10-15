// # <u>Coding with reflexion<u>

// ## Power of Thor  



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
// Most of the time it doesn’t work on the first try, so I read the error
// message, and it said that my letters for the direction weren’t in the right
// order because I printed the X before the Y. The first two tests worked
// because it was just a straight line but not the diagonal ones. So I just had
// to reverse that, and the code was okay for all the tests.

// **The goal of the program here is to allow at the end of each iteration, that
// thor approaches the light using its coordinates**


// ![pre writting](pseudocode.jpg)



// ### Peudocode

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





#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>    // the X position of the light of power


int main()
{

    // the Y position of the light of power
    int light_x;
    // Thor's starting X position
    int light_y;

    // Thor's starting Y position
    int initial_tx;

    int initial_ty;
    scanf("%d%d%d%d", &light_x, &light_y, &initial_tx, &initial_ty);
    
    //w init position of thor 
    int ThorX = initial_tx;
    int ThorY = initial_ty;    // game loop

    

   // The remaining amount of turns Thor can move.
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

    




        // A single line providing the move to be made: N NE E SE S SW W or NW
        printf("%s%s\n", directionY, directionX);
    }

    return 0;
    // *here his a link to CodinGame to use this solution :*
    // [CodinGame](https://www.codingame.com/)
}