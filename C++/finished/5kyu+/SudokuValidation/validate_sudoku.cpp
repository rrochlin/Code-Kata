#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool checkForDuplicates(vector<vector<unsigned int>> &matrix){
    for (vector<unsigned int> row : matrix) {
        sort(row.begin(),row.end());
        if(adjacent_find(row.begin(), row.end()) != row.end()) return true;
    }
    return false;
}

bool validSolution(unsigned int board[9][9]){
    // read info into a vector for its built in methods
    vector<vector<unsigned int>> rows_vector(9, vector<unsigned int>(9));
    vector<vector<unsigned int>> cols_vector(9, vector<unsigned int>(9));
    vector<vector<unsigned int>> grid_vector(9, vector<unsigned int>(9));

    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            rows_vector[i][j] = board[i][j];
            cols_vector[j][i] = board[i][j];
            int x = ((int)i/3)*3 + ((int)j/3);
            int y = (i%3)*3+j%3;
            grid_vector[x][y] = board[i][j];
        }
    }

    if (checkForDuplicates(rows_vector)) return false;
    if (checkForDuplicates(cols_vector)) return false;
    if (checkForDuplicates(grid_vector)) return false;

    return true;
}


int main(){
unsigned int example1[9][9] = {{5, 3, 4, 6, 7, 8, 9, 1, 2}, 
                             {6, 7, 2, 1, 9, 5, 3, 4, 8},
                             {1, 9, 8, 3, 4, 2, 5, 6, 7},
                             {8, 5, 9, 7, 6, 1, 4, 2, 3},
                             {4, 2, 6, 8, 5, 3, 7, 9, 1},
                             {7, 1, 3, 9, 2, 4, 8, 5, 6},
                             {9, 6, 1, 5, 3, 7, 2, 8, 4},
                             {2, 8, 7, 4, 1, 9, 6, 3, 5},
                             {3, 4, 5, 2, 8, 6, 1, 7, 9}}; 
                             
unsigned int example2[9][9] = {{5, 3, 4, 6, 7, 8, 9, 1, 2}, 
                              {6, 7, 2, 1, 9, 0, 3, 4, 8},
                              {1, 0, 0, 3, 4, 2, 5, 6, 0},
                              {8, 5, 9, 7, 6, 1, 0, 2, 0},
                              {4, 2, 6, 8, 5, 3, 7, 9, 1},
                              {7, 1, 3, 9, 2, 4, 8, 5, 6},
                              {9, 0, 1, 5, 3, 7, 2, 1, 4},
                              {2, 8, 7, 4, 1, 9, 6, 3, 5},
                              {3, 0, 0, 4, 8, 1, 1, 7, 9}};
      
    cout << validSolution(example1) << endl;
    cout << validSolution(example2) << endl;
    return 0;
}