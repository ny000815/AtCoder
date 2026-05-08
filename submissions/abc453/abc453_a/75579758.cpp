#include <iostream>
using namespace std;

int main() 
{
    int N;
    string S;
    cin >> N;
    cin >> S;
    int i = 0;
    while (i < N && S[i] == 'o') i++;
    cout << S.substr(i);
}