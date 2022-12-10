#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int update(int comp, int cycle, int crow, int pixel) {
    if ((comp == cycle) || (cycle == (comp - 1)) || (cycle == (comp + 1))) {
        printf("█");
    } else {
        printf(".");
    }

    if (pixel % 40 == 0) {
        printf("\n");
        crow = crow + 1;
    }

    return crow;
}

int main(int argc, char **argv) {

    char buffer[5000];
    FILE *file = fopen("./data.txt", "r");

    int x = 1;
    int cycle = 0;
    int pixel = 1;
    int crow = 0;

    while((fgets (buffer, 5000, file)) != NULL) {
        char linecopy[strlen(buffer)];
        strcpy(linecopy, buffer);

        char *token = strtok(linecopy, " ");

        if (strcmp(token, "addx") == 0) {
            char *number = strtok(NULL, " ");

            int compa = x + (40 * crow);
            crow = update(compa, cycle, crow, pixel);
            cycle = cycle + 1;
            pixel = pixel + 1;

            int compb = x + (40 * crow);
            crow = update(compb, cycle, crow, pixel);
            cycle = cycle + 1;
            pixel = pixel + 1;

            x = x + atoi(number);
        } else {
            int compc = x + (40 * crow);
            crow = update(compc, cycle, crow, pixel);
            cycle = cycle + 1;
            pixel = pixel + 1;
        }
    }

    fclose(file);
}