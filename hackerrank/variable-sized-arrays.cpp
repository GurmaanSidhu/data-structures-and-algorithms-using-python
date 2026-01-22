#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a, b;
    cin >> a >> b;
    vector<vector<int>> vec(a);
    
    for (int i = 0; i < a; i++) {
        int size;
        cin >> size;
        vec[i].resize(size);
        for (int j = 0; j < size; j++) {
            cin >> vec[i][j];
        }
    }
    for (int i = 0; i < b; i++) {
        int x, y;
        cin >> x >> y;
        cout << vec[x][y] << endl; 
    }
    
    return 0;
}