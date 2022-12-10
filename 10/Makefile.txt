CC=gcc
EXEC=part1 part2

.PHONY: all clean

all: $(EXEC)

part1: part1.c
	$(CC) $< -o $@

part2: part2.c
	$(CC) $< -o $@

clean:
	rm -rf $(EXEC)