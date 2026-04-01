#include <stdio.h>
#include <stdbool.h>

#define N 7      
#define COLORS 3 

char *states[] = {"WA", "NT", "SA", "QLD", "NSW", "V", "T"};

int graph[N][N] = {
    // WA NT SA QLD NSW V  T
    {0, 1, 1, 0, 0, 0, 0}, // WA
    {1, 0, 1, 1, 0, 0, 0}, // NT
    {1, 1, 0, 1, 1, 1, 0}, // SA
    {0, 1, 1, 0, 1, 0, 0}, // QLD
    {0, 0, 1, 1, 0, 1, 0}, // NSW
    {0, 0, 1, 0, 1, 0, 0}, // V
    {0, 0, 0, 0, 0, 0, 0}  // T 
};

char *colorNames[] = {"Red", "Green", "Blue"};

bool isSafe(int node, int color[], int c) {
    for (int i = 0; i < N; i++) {
        if (graph[node][i] && color[i] == c)
            return false;
    }
    return true;
}

bool solve(int node, int color[]) {
    if (node == N)
        return true;

    for (int c = 0; c < COLORS; c++) {
        if (isSafe(node, color, c)) {
            color[node] = c;

            if (solve(node + 1, color))
                return true;

            color[node] = -1; // backtrack
        }
    }
    return false;
}

int main() {
    int color[N];
    for (int i = 0; i < N; i++)
        color[i] = -1;

    if (solve(0, color)) {
        printf("Solution:\n");
        for (int i = 0; i < N; i++) {
            printf("%s -> %s\n", states[i], colorNames[color[i]]);
        }
    } else {
        printf("No solution exists.\n");
    }

    return 0;
}
