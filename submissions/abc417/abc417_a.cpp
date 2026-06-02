#include <iostream>
using namespace std;

int main() 
{
    int N, A, B;
    string S;
    cin >> N >> A >> B;
    cin >> S;
    cout << S.substr(A, N - A - B);
}