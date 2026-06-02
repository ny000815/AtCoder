#include <bits/stdc++.h>
using namespace std;

int J[1001][1001];
int O[1001][1001];
int I[1001][1001];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N, K;
    cin >> M >> N;
    cin >> K;

    vector<string> info(M);
    for (int i = 0; i < M; i++) {
        cin >> info[i];
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            J[i+1][j+1] = J[i][j+1] + J[i+1][j] - J[i][j];
            O[i+1][j+1] = O[i][j+1] + O[i+1][j] - O[i][j];
            I[i+1][j+1] = I[i][j+1] + I[i+1][j] - I[i][j];

            if (info[i][j] == 'J') J[i+1][j+1]++;
            else if (info[i][j] == 'O') O[i+1][j+1]++;
            else I[i+1][j+1]++;
        }
    }

    for (int q = 0; q < K; q++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        int ansJ = J[c][d] + J[a-1][b-1] - J[a-1][d] - J[c][b-1];
        int ansO = O[c][d] + O[a-1][b-1] - O[a-1][d] - O[c][b-1];
        int ansI = I[c][d] + I[a-1][b-1] - I[a-1][d] - I[c][b-1];

        cout << ansJ << ' ' << ansO << ' ' << ansI << '\n';
    }

    return 0;
}