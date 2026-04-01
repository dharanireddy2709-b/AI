#include <stdio.h>
#include <stdbool.h>

int S,E,N,D,M,O,R,Y;

bool isUnique(int used[]) {
    for(int i=0;i<10;i++){
        if(used[i] > 1)
            return false;
    }
    return true;
}

int main() {

    int used[10];

    for (S = 1; S <= 9; S++)       // S ≠ 0
    for (E = 0; E <= 9; E++)
    for (N = 0; N <= 9; N++)
    for (D = 0; D <= 9; D++)
    for (M = 1; M <= 9; M++)       // M ≠ 0
    for (O = 0; O <= 9; O++)
    for (R = 0; R <= 9; R++)
    for (Y = 0; Y <= 9; Y++) {

        // Reset used array
        for(int i=0;i<10;i++) used[i]=0;

        // Count usage
        used[S]++; used[E]++; used[N]++; used[D]++;
        used[M]++; used[O]++; used[R]++; used[Y]++;

        // Check uniqueness
        if (!isUnique(used))
            continue;

        int send  = 1000*S + 100*E + 10*N + D;
        int more  = 1000*M + 100*O + 10*R + E;
        int money = 10000*M + 1000*O + 100*N + 10*E + Y;

        if (send + more == money) {
            printf("Solution:\n");
            printf("S=%d E=%d N=%d D=%d\n", S,E,N,D);
            printf("M=%d O=%d R=%d Y=%d\n\n", M,O,R,Y);

            printf("%d + %d = %d\n", send, more, money);
            return 0;
        }
    }

    printf("No solution found\n");
    return 0;
}
