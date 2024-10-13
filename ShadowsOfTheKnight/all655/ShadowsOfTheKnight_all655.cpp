// # Assignment: Introduction to the CodeChat Editor
//
// ### ECE 4793/6793 - Literate Programming in Software Development
//
// ### Name: Lael Lum
//
// ### NetID: all655
//
// ---
//
// ## The puzzle I chose was *<a title="Shadows of the Knight - Episode 1" href="https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1" target="_blank" rel="noopener">Shadows of the Knight - Episode 1</a>*
//
// ### How I went about solving this puzzle: 
//
// At first, I began by coding. I just read very carefully through the
// instructions that stated what the program was supposed to do. I then realized
// I would need if-statements for each possible direction that the bomb may be
// (Up, Down, Left, Right, Up-Left, Up-Right, Down-Left, DownRight). Note the
// direction of the bomb was given by a device that Batman was holding, which
// was given through the string variable bomb_dir. At this point I hit a mental
// block and ran out of time as I was not sure yet how I would configure each
// if-statement. Normally I would keep trying and experimenting until something
// concrete came to mind. At this point, which was about 15 minutes, I made some
// notes/drawings, which are shown at the end of this document.
//
// When I wrote out my ideas on paper as instructed in step 4 (see
// [Coding with Reflection assignment instructions](https://canvas.msstate.edu/courses/133359/assignments/1257462)),
// it became clear what I needed to do as well as helped me realize scenarios
// that I had not considered beforehand. I essentially solved the problem by
// using a box or four separate variables as boundaries, which encompassed the
// points that the bomb could be in, and points outside of the box’s boundaries
// were eliminated from the realm of possible points. For example, if the
// direction of the bomb is up-left (UL) of Batman, then I know that all points
// below Batman (DL, D, DR) and above as well as to the right of Batman (U, UR)
// are out of the realm of points to consider, so in this case, the bottom right
// corner of the box would be where Batman is currently positioned when informed
// that the bomb is UL. If the bomb was located DR (Down-Right) of Batman,
// Batman’s current position would be the top-left of the box (see **Figure
// 1**). I basically created a binary search but for **two** dimensions without
// using an array. Using an array might have been much cleaner and concise but
// doing it this way made more sense for me. In my code, I kept the box’s
// position updated, so it would essentially shrink any which way with each jump
// that Batman made. Whenever Batman jumped, he would jump to the center of the
// box every time until he discovered the bomb. Please see the code for more
// details as well as the following figures/notes.
//
// <img style="border-style: ridge;" title="fig1&amp;fig2.png" src="fig1&amp;fig2.png" alt="" width="700" height="275">
//
// ### Here are some notes/drawings I made:
//
// <img style="border-style: ridge;" title="notes1.jpg" src="notes1.jpg" alt="" width="700" height="1200">
// <img style="border-style: ridge;" title="notes2.jpg" src="notes2.jpg" alt="" width="700" height="1200">
// <img style="border-style: ridge;" title="notes3.jpg" src="notes3.jpg" alt="" width="700" height="700">
//
// In this sketch, I realized what the math would look like or involve to find
// the center of the “box”. This was the moment that I grasped it was just some
// simple algebra.
//
// ## The code is as follows:
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//
// Auto-generated code below aims at helping you parse
// the standard input according to the problem statement.
//

int main()
{
    int w; // width of the building.
    int h; // height of the building.
    cin >> w >> h; cin.ignore();
    int n; // maximum number of turns before game over.
    cin >> n; cin.ignore();
    int x0;
    int y0;
    cin >> x0 >> y0; cin.ignore();
    //
    // I was going to use a 2d array but decided not to as my way made more
    // sense to me. int array\[w\]\[h\] = {0};
    //
    // These were used to track of where Batman was as well as configure the
    // boundaries for the box, which is explained further below.
    int x = x0;
    int y = y0;
    //
    // To keep track of the area that the bomb could and could not be, I kept
    // track of a box that would contain all potential points that the bomb may be.
    // Any point outside of the box that would slowly shrink were considered
    // void or not a possibility of containing the bomb.
    // 
    int boxLeftSide = 0; // Left side of box
    int boxRightSide = w; // Right side of box
    int boxTopSide = 0; // Top side of box
    int boxBottomSide = h; // Bottom side of box

    // game loop
    while (1) {
        string bomb_dir; // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        cin >> bomb_dir; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl" To debug: cerr
        // << "Debug messages..." << endl;

        //if up, divide distance to box edge by 2
        if(bomb_dir == "U")
        {   
            boxBottomSide = y;
            cout << x << " " << (((y-boxTopSide)/2) + boxTopSide) << endl;
            y = (((y-boxTopSide)/2) + boxTopSide);
            x = x;
            
        }
        else if(bomb_dir == "UR")
        {
            boxBottomSide = y;
            boxLeftSide = x;
            cout << (((x-boxRightSide)/2) + boxRightSide) << " " << (((y-boxTopSide)/2) + boxTopSide) << endl;
            y = (((y-boxTopSide)/2) + boxTopSide);
            x = (((x-boxRightSide)/2) + boxRightSide);
        }
         else if(bomb_dir == "R")
        {
            boxLeftSide = x;
            cout << (((x-boxRightSide)/2) + boxRightSide) << " " << y << endl;
            x = (((x-boxRightSide)/2) + boxRightSide);
            y = y;
        }
         else if(bomb_dir == "DR")
        {
            boxLeftSide = x;
            boxTopSide = y;
            cout << (((x-boxRightSide)/2) + boxRightSide) << " " << (((boxBottomSide-y)/2) + boxTopSide) << endl;
            x = (((x-boxRightSide)/2) + boxRightSide);
            y = (((boxBottomSide-y)/2) + boxTopSide);
        }
         else if(bomb_dir == "D")
        {
            boxTopSide = y;
            cout << x << " " << (((boxBottomSide-y)/2) + boxTopSide) << endl;
            y = (((boxBottomSide-y)/2) + boxTopSide);
            x = x;
        }
         else if(bomb_dir == "DL")
        {
            boxTopSide = y;
            boxRightSide = x;
            cout << (((x-boxLeftSide)/2) + boxLeftSide) << " " << (((boxBottomSide-y)/2) + boxTopSide) << endl;
            y = (((boxBottomSide-y)/2) + boxTopSide);
            x = (((x-boxLeftSide)/2) + boxLeftSide);
        }
         else if(bomb_dir == "L")
        {
            boxRightSide = x;
            cout << (((x-boxLeftSide)/2) + boxLeftSide) << " " << y << endl;
            x = (((x-boxLeftSide)/2) + boxLeftSide);
            y = y;
        }
         else if(bomb_dir == "UL")
        {
            boxBottomSide = y;
            boxRightSide = x;
            cout << (((x-boxLeftSide)/2) + boxLeftSide) << " " << (((y-boxTopSide)/2) + boxTopSide) << endl;
            y = (((y-boxTopSide)/2) + boxTopSide);
            x = (((x-boxLeftSide)/2) + boxLeftSide);
        }

    }
} 
