// # **_Power of Thor - Episode 1_**
// ECE4793 - Introduction to GitHub Assignment Written in c++ \
// Name: Drake Robertson \
// NetID: dsr209
// 
// ---
//
// ## **About the Game**
//
// This game involves Thor, a red lightning bolt, the light, and the map. It is **won** 
// by _moving Thor one space at a time towards the light until he reaches the 
// space occupied by the light_. The map, Image 1, is a coordinate grid beginning 
// at (0,0) and goes to (39,17) with **positive X direction to the East** and 
// **positive Y direction to the South**. Thor is directed in cardinal directions 
// using the character output (cout) function in c++. Below is a list of the 
// characters output and their corresponding direction.
//
// - "N" for _north_
// - "NE" for _northeast_
// - "E" for _east_
// - "SE" for _southeast_
// - "S" for _south_
// - "SW" for _southwest_
// - "W" for _west_
// - "NW" for _northwest_

// **_Image 1: Thor Game Map_**\
// ![Thor_map](thor_map.png)\
// This image was obtained from
// [codingame.com](https://www.codingame.com/ide/puzzle/power-of-thor-episode-1)
//
// ## My Approach
//
// For the problem of getting Thor to the light my solution is simple, compare
// the light's position with Thor's and determine the correct direction to move.
// The game gives the X and Y position of the light as well as the X and Y
// position of Thor. Knowing that the X values increase to the east and the Y
// values increase to the south, the direction Thor needs to go can be
// determined from the light's position. Listed below are the scenarios and the
// directon Thor will go.
//
// ### Conditions
//
// - Light X > Thor X: **East**
// - Light X < Thor X: **West**
// - Light Y > Thor Y: **South**
// - Light Y < Thor Y: **North**
//
// If there is a combination of the X _and_ Y differing, Thor will move in a
// combination of the cardinal directions. After moving Thor, his position will
// need to be updated based on the direction he was moved.
//
// I also found it beneficial to see the map a little differently so I drew it
// out with the the directions in the middle. It can be seen in Image 2 below.
// This allowed me to visualize better the direction Thor would need to go by
// seeing the compass in the middle of the map. It also helped me by seeing the
// furthest coordinate point with the x and y axises to conceptualize updating
// Thor's position.
//
// **Image 2: Map Sketch**
//
// ![Map Sketch](map_sketch.png)
//
// ### _Beginning of auto generated code by the game_
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    // ### **Variable Names and Assignments**
    //
    // This section initializes and assigns the light's and Thor's x and y
    // position with _light_x_, _light_y_, _thor_x_, and _thor_y_.
    int light_x;
    int light_y;
    int thor_x;
    int thor_y;
    cin >> light_x >> light_y >> thor_x >> thor_y; cin.ignore();

    // ### **Game Loop**
    while (1) {
        // The remaining amount of turns Thor can move. Do not remove this line.
        int remaining_turns; 
        cin >> remaining_turns; cin.ignore();        
        // ## **Beginning of User Created Code**
        //
        // The code I wrote to solve this game begins after this. It is
        // broken into four sections. They each follow similar but _different_
        // logic to compare Thor's position with the light and then move him
        // in the correct direction.
        
// ---
        // ## Straight Line Movement
        //
        // When either Thor's X or Y value matches one of the X or Y values of
        // the light, Thor needs to move in a straight line towards the light.
        // These two sections are split into the logic to find North or South
        // movement and then East or West movement.
        //
        // ### North/South
        //
        // If thors X position is the same as the light's, the only necessary
        // movement will be North or South (the Y axis). This if statement
        // checks for the X axis being the same, then it compares the y
        // positions of Thor and the light. If the light is greater it outputs
        // "S" to have Thor move south then it increases Thor's Y position. If
        // it fails that but it is already in this _if_ statement, then Thor's
        // direction can be determined to be north without the need to do any
        // more comparisons. Thor's y position is then decreased to account for
        // Thor moving one space North.
        if (light_x == thor_x) {
            if (light_y > thor_y) {
                cout << "S" << endl;
                thor_y++;
            }
            else {
                cout << "N" << endl;
                thor_y--;
            }
        }
        // ### East/West
        //
        // This if statement checks for the light's Y value matching Thor's Y
        // value. If this is the case, Thor will need to move either East or
        // West. Once in the statement, the light's x value is compared to see
        // if it is greater than Thor's. If this is the case, Thor will need to
        // move to the East and his X value will be increased. If it fails that
        // check, it means Thor's x value would have to be greater than the
        // light's causing Thor to need to move to the West and have his X value
        // decreased by one.
        else if (light_y == thor_y) {
            if (light_x > thor_x) {
                cout << "E" << endl;
                thor_x++;
            }
            else {
                cout << "W" << endl;
                thor_x--;
            }
        }

        // ## Combinational Direction Movement
        //
        // Combinational direction movement is needed when there is a difference
        // between both X and Y values between Thor and the light. Combinational
        // movement moves Thor in a diagonal line from his current position
        // instead of a straight line. This requires the Thor's position to be
        // updated in both the X and Y values after every move. My logic for
        // this section involves first comparing the X values and then the Y
        // values. This allowed me to keep the Y logic the same in that it will
        // check for the north and south component in the same way.
        //
        // ### Southeast/Northeast
        //
        // This section checks to see if the light's X value is greater than
        // Thor's which corresponds to an East movement. To find the second part
        // of the combinational movement, the Y values are compared. If the
        // light's y value is greater than Thor's, it will move Thor to the
        // southeast and then increase Thor's X and Y because he is moving to
        // the left and down. If it fails that check it can be assumed based on
        // being in this statement that the only other option would be to move
        // Thor to the northeast, and then increase Thor's X value and decrease
        // Thor's Y value becaue he is now moving up.
        else if (light_x > thor_x) {
            if (light_y > thor_y) {
                cout << "SE" << endl;
                thor_x++;
                thor_y++;
            }
            else {
                cout << "NE" << endl;
                thor_x++;
                thor_y--;
            }
        }

        // ### Southwest/Northwest
        //
        // This last section contains the logic needed to move Thor in the
        // southwest or northwest direction. Like the above section it begins by
        // comparing the X values but this time it looks to see if the light's X
        // value is less than Thor's. This denotes a west movement. For the
        // second part, the Y values are compared the same way the previous step
        // did, if the light's Y is greater, move Thor to the southwest and
        // decrease Thor's X value and increase his Y. If not move Thor to the
        // southwest and decrease both his X and Y value.
        else if (light_x < thor_x) {
            if (light_y > thor_y) {
                cout << "SW" << endl;
                thor_x--;
                thor_y++;
            }
            else {
                cout << "NW" << endl;
                thor_x--;
                thor_y--;
            }
        }
    
    }
}