// # _The Power of Thor_
//
// ---
//
// [CodinGame](https://www.codingame.com/training/easy/power-of-thor-episode-1)
// Here is the CodinGame this code is for.
//
// ## Problem
//
// When I first opened this assignment, I looked at the description of the
// project in order to understand what was being provided for me, and what I
// needed to do. The description tells us that Thor needs to go to The Light to
// receive its power. Thor and the Light are placed in two different coordinates
// in the x and y plane. The programmer needs to create a loop that will guide
// Thor to The Light. The programmer is given all the variables and code
// required, meaning the only worry is the loop, specifically the while loop.
//
// The solution that I came with after writing all the important information
// down was to create 8 if-else statements for each movement. Thor can only move
// in the North, East, South, West, Northeast, Northwest, Southeast, Southwest.
// Thor has a limited number of turns to reach The Light and he can only move
// one cell each turn. Each if-else statement has two conditions, one for the x
// coordinate and one for the y coordinate. When one of these coordinates is
// satisfied, Thor moves one cell in that direction and then the loop restarts
// This will go on until Thor has the reached The Light.

// ![alt](The-Power-of-Thor-Block-Diagram.jpg)
//
// ---
//
// ### _Provided Code_
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
* Auto-generated code below aims at helping you parse
* the standard input according to the problem statement.
* ---
* Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
**/

int main() { 
    // These are the four given variables.
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    // Here you are given a number of turns that thor can have to reach the
    // light. This while loop will continue until either the turns run out or
    // thor reaches the light.
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        //
        // ### _My Code_
        //
        // If Thor's x and y coordinates are greater than the light's x and y
        // coordinates, move Thor northwest by one.
        if (initial_tx > light_x && initial_ty > light_y) {
            initial_tx -= 1; // One cell west
            initial_ty -= 1; // One cell north
            cout << "NW" << endl;
        }

        // If Thor's x coordinate is smaller and thor's y coordinate is greater
        // than the light's x and y coordinates, move Thor northeast by one.
        else if (initial_tx < light_x && initial_ty > light_y) {
            initial_tx += 1; // One cell east
            initial_ty -= 1; // one cell north
            cout << "NE" << endl;
        }

        // If Thor's x coordinate is greater and thor's y coordinate is small
        // than the light's x and y coordinates, move Thor southwest by one.
        else if (initial_tx > light_x && initial_ty < light_y) {
            initial_tx -= 1; // One cell west
            initial_ty += 1; // One cell south
            cout << "SW" << endl;
        }

        // If Thor's x and y coordinates are smaller than the light's x and y
        // coordinates, move Thor southeast by one.
        else if (initial_tx < light_x && initial_ty < light_y) {
            initial_tx += 1; // One cell east
            initial_ty += 1; // One cell south
            cout << "SE" << endl;
        }
        
        // If only Thor's x coordinate is greater than the light's x coordinate,
        // move Thor west by one.
        else if (initial_tx > light_x && initial_ty == light_y) {
            initial_tx -= 1; // One cell west
            cout << "W" << endl;
        }
        
        // If only Thor's x coordinate is smaller than the light's x coordinate,
        // move Thor east by one.
        else if (initial_tx < light_x && initial_ty == light_y){
            initial_tx += 1; // One cell east
            cout << "E" << endl;
        }

        // If only Thor's y coordinate is greater than the light's y coordinate,
        // move Thor north by one.
        else if (initial_ty > light_y && initial_tx == light_x) {
            initial_ty -= 1; // One cell north
            cout << "N" << endl;
        }

        // If only Thor's y coordinate is smaller than the light's y coordinate,
        // move Thor south by one.
        else  if (initial_ty < light_y && initial_tx == light_x) {
            initial_ty += 1; // One cell south
            cout << "S" << endl;
        }

        else {

        }
    }
}

// Helpful Links
//
// * [C++ Cheat Sheet](https://www.codewithharry.com/blogpost/cpp-cheatsheet/) 
//
// * [Markdown Help](https://www.markdownguide.org/cheat-sheet/)
