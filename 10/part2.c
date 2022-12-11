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

        int comp = x + (40 * crow);
        crow = update(comp, cycle, crow, pixel);
        cycle = cycle + 1;
        pixel = pixel + 1;

        if (strcmp(token, "addx") == 0) {
            char *number = strtok(NULL, " ");

            comp = x + (40 * crow);
            crow = update(comp, cycle, crow, pixel);
            cycle = cycle + 1;
            pixel = pixel + 1;

            x = x + atoi(number);
        }
    }

    fclose(file);
}