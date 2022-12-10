#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {

    char buffer[5000];
    FILE *file = fopen("./test.txt", "r");

    int cycle = 0;
    int stopcycle = 20;
    int x = 1;
    int total = 0;
    while((fgets (buffer, 5000, file)) != NULL) {
        int ticks = 1;

        char linecopy[strlen(buffer)];
        strcpy(linecopy, buffer);

        char *token = strtok(linecopy, " ");

        printf("%d, %d\n", cycle, x);

        if (strcmp(token, "addx") == 0) {
            char *number = strtok(NULL, " ");

            if (cycle + 1 == stopcycle || cycle + 2 == stopcycle) {
                total = total + (stopcycle * x);
                stopcycle = stopcycle + 40;
            }

            x = x + atoi(number);

            ticks = 2;
        } else {
            if (cycle == stopcycle) {
                total = total + (stopcycle * x);
                stopcycle = stopcycle + 40;
            }
        }

        cycle = cycle + ticks;
    }

    printf("total: %d\n", total);

    fclose(file);
}