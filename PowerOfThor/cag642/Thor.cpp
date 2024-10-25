// # Thor Program

// ## Setup:
//
// <span style="background-color: #f1c40f;">DH </span> : I think you should keep
// your code together. Move this down to the rest of your code. Have it after
// you explain the problem. <mark>CG: </mark> I personally like the separation
// but I understand what you mean.

// **First we want to include our libraries:**
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// ## Program:
//
// <span style="background-color: #f1c40f;">DH </span> : Saying program again is
// very redundant. You could scrap that and replace the heading with "Problem."
// <mark>CG: </mark> I personally think the Program heading is broader than just
// the problem.

// ### Problem:

// We are shown the initial problem
// [here.](https://www.codingame.com/training/easy/power-of-thor-episode-1)


// ![Thor_Screenshot2](Thor_Screenshot2.jpg)

// In this final case, Thor begins at the top left corner of the screen with the
// light of power at the bottom right. We are challenged to get Thor to the
// light of power by giving him the following directions: **N, NE, E, SE, S, SW,
// W, NW**. The tricky part is that Thor only has so many steps before he runs
// out of energy. We are going to want to create a loop that keeps track of
// Thor's position and sends him in the appropriate direction until he is on the
// same line.

int main()
{

// ### Variables:

// We are given four variables in the problem:
//
// 1.  **light_x** - the _X_ position of the light of power
// 2.  **light_y** - the _Y_ position of the light of power
// 3.  **initial_tx** - Thor's starting _X_ position
// 4.  **initial_ty** - Thor's starting _Y_ position

// These are all integers and are given a value when the program starts based on
// where Thor and the light of power are.


    int light_x; 
    int light_y; 
    int initial_tx; 
    int initial_ty; 
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    // ### Main Loop:

    while (1) {


	    // This was given in the problem. It declares remaining_turns as a variable
	    // and keeps track of how many remaining turns are left.

        int remaining_turns; 
        cin >> remaining_turns; cin.ignore();


    // ### Algorithm:

	// In the first if statement we are checking to see if the light's position is
	// farther to the right than Thor's position. Assuming it is (which in this
	// last test case it is), Thor will go southeast one step. Afterwards we add 1
	// to Thor's initial position value in order to accurately keep track of his
	// placement. This loop will run continuously until Thor's Y position is equal
	// to the light's Y position.

        if (light_y > initial_ty) {
            cout << "SE" << endl;
            initial_ty = initial_ty + 1;
        }
    
	// Once Thor and the light both have the same Y position, the else if statement
	// checks the X position. If Thor has an initial X position lower than the
	// initial Y position (Which we know he does) then he will move right one step
	// and add 1 to his initial X position. This goes on until Thor reaches his
	// destination.


        else if (light_x > initial_tx){
            cout << "E" << endl;
            initial_tx = initial_tx + 1;
       }
        
        
    }

	// #### Helpful links:
	//
	// [Coding Games](https://www.codingame.com/start/)

	// [C++ Syntax](https://www.codewithharry.com/blogpost/cpp-cheatsheet/)

	// [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)


}