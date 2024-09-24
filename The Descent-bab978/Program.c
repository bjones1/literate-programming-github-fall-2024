// # Program.c This program is to solve a programming puzzle called the Descent

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/

int main()
{
    // These 2 int statement declare the variables we are using 
    // the highest mountain and the current mountain
    int highest;
    int currentMount;
    // game loop below
    while (1) {
        highest = 0;
        currentMount = 0;
        for (int i = 0; i < 8; i++) {
            // int below holds the height of the mountains
            int mountain_h;
            // the cin below enters the mountain numbers and heights
            cin >> mountain_h; cin.ignore();

            // if statement to check for and save the largest mountain
            if(mountain_h > highest){
                highest = mountain_h;
                currentMount = i;
            }
            
        }
            // the statement below outputs a number which causes the ship
            // in the game to shoot the mountain with the matching number
        cout << currentMount << endl;
    }
}