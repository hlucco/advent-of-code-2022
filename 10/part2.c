#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {

    char buffer[5000];
    FILE *file = fopen("./data.txt", "r");

    int cycle = 0;
    int stopcycle = 20;
    int x = 1;
    int total = 0;
    while((fgets (buffer, 5000, file)) != NULL) {
        int ticks = 1;

        if (cycle > 217) {
            printf("%s\n", buffer);
            printf("NEW CYCLE\n");
            printf("cycle: %d\n", cycle);
            printf("%d\n", stopcycle);
            printf("%d\n", x);
        }

        char linecopy[strlen(buffer)];
        strcpy(linecopy, buffer);

        char *token = strtok(linecopy, " ");

        if (strcmp(token, "addx") == 0) {
            char *number = strtok(NULL, " ");
            // printf("%d\n", atoi(number));

            if (cycle + 1 == stopcycle || cycle + 2 == stopcycle) {
                printf("THERE\n");
                printf("cycle * x: %d\n", (stopcycle) * x);
                total = total + (stopcycle * x);
                stopcycle = stopcycle + 40;
            }

            x = x + atoi(number);

            ticks = 2;
        } else {
            if (cycle == stopcycle) {
                printf("cycle * x: %d\n", stopcycle * x);
                total = total + (stopcycle * x);
                stopcycle = stopcycle + 40;
            }
        }

        // printf("total: %d\n", total);
        cycle = cycle + ticks;
    }

    printf("total: %d\n", total);

    fclose(file);
}