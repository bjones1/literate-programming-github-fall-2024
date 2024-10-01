// # The Power of Thor: Literate Code

// Game [here](https://www.codingame.com/ide/puzzle/power-of-thor-episode-1)

// ## Overview
//
// <span style="background-color: yellow;">GLW:</span> Fixed typos, punctuation
//
// This program was made for the codingame: The Power of Thor (Linked above).
// The game has a beacon where the character, Thor, must move to. Only the
// position of the beacon is given in light_x and light_y. Thor only has so many
// moves he can take to get to the beacon, so the most direct path must be
// found. Additionally, he can fall off the map, ending his quest and failing
// the game.
//
// <span style="background-color: yellow;">GLW:</span> I suggest elaborating on
// what _light_\[XY\]\_ represents first\
//            Additionaly, those variable names do not show up in your code\
// <span style="background-color: yellow;">GLW:</span> More typo fixes
//
// To accomplish this, I used an if-else check for each value, _light_y_ and
// _light_x_ respectively. A flow chart of this logic can be found below. I made
// it so that Thor's position was updated with each change of X and Y, making it
// possible to keep track of him so he dosen't 'fall off' the map. Once the
// if-else is finished, the X and Y values are added together to make a smooth,
// and in some cases, diagonal line to the goal. This had to be done because a
// limited about of 'moves' were given and simply changing the X and Y
// seperatly, one at a time, would take up all the moves.
//
// <span style="background-color: yellow;">GLW:</span> It might just be me, but
// I cannot find your image in the repo\
//            The image does not display\
// ![Flow chart](IMG_0896.png)

// ## Nessasary Includes

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{

// ## Keeping Track of Values
//
// <span style="background-color: yellow;">GLW:</span> In the first paragraph,
// you call it a beacon, yet these comments refer to it as "the power of light";
// be consistent
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();
    int ThorX = initial_tx;
    int ThorY = initial_ty;

// ## Game Loop
    while (1) {
        // <span style="background-color: yellow;">GLW:</span> Explain why it
        // can't be removed; nowhere else in your code is it ever used beside
        // the two lines below.\
        //            Just say it's a meaningless input required to be read by
        // the test cases instead just "Do not remove."
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        string X = "";
        string Y = "";

// ## Finding Position
//
// See flow chart at the top of the file for detailed logic


// ### Find Y position
        if(ThorY > light_y){
            Y = "N";
            ThorY -= 1;
        }
        else if(ThorY < light_y){
            Y = "S";
            ThorY += 1;
        }

// <span style="background-color: yellow;">GLW:</span> Fixed formatting
// inconsistencies
//
// ### Find X position
        if(ThorX > light_x){
            X = "W";
            ThorX -= 1;
        }
        else if (ThorX < light_x){
            X = "E";
            ThorX += 1;
        }

// ### Output Position
//
// #### Note: Outputing tells the character where to move, it is not just text in a box
       cout << Y << X << endl;        

    }
}