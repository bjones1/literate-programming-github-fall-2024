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

/* Block Comment */

int main()
{
    int light_x; // the X p4osition of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    int thor_x = initial_tx;
    int thor_y = initial_ty;

    // game loop
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        vector<char> direction;

        // **North**
        if (light_y < thor_y) {
            direction.push_back('N');
            thor_y--;
        }
        // **South**
        else if (light_y > thor_y){
            direction.push_back('S');
            thor_y++;
        }
        // **West**
        if (light_x < thor_x) {
            direction.push_back('W');
            thor_x--;
        }
        // **East**
        else if (light_x > thor_x) {
            direction.push_back('E');
            thor_x++;
        }

        // Write an action using cout. DON'T FORGET THE "<< endl" To debug: cerr
        // << "Debug messages..." << endl;


        // A single line providing the move to be made: N NE E SE S SW W or NW
        for (int i=0; i<sizeof(direction); i++) {    
            cout << direction[i];
        }
        cout << endl;
    }
}