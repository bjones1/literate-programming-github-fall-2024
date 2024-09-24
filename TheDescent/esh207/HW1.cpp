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
 * Resources: https://en.cppreference.com/w/cpp/container/vector
 * :https://en.cppreference.com/w/cpp/algorithm/max_element
 **/

int main()
{
    vector<int> Mount_H = {0,0,0,0,0,0,0,0} ; //Vector of Mountain Heights
    vector<int>::iterator max_Mount;
    int target; //target to shoot at, should be the index of target, not height
    // game loop
    while (1) {
        for (int i = 0; i < 8; i++) {
            int mountain_h; // represents the height of one mountain.
            cin >> mountain_h; cin.ignore();
            Mount_H[i] = mountain_h; // Fills a vector of mountain heights
            //cerr << "Debug: " << i <<":" << Mount_H[i]<< endl; // debug message
        }

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        max_Mount = max_element(Mount_H.begin(),Mount_H.end());// gets max element
        target =  distance(Mount_H.begin(), max_Mount); // gets index of max element for target
        // cerr << "Target: " << target << endl; // Debug message
        // cerr << "size: " << Mount_H.size() << endl; // Debug message
        Mount_H[target] = 0;
        cout << target << endl; // The index of the mountain to fire on.
    }
}
