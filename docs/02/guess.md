# C: Guessing Game Solution

```c
#include <stdio.h>
#include <stdlib.h> // for rand() and srand()
#include <time.h> // for time()

// the user can only guess 3 times

int main() {
    srand(time(NULL)); // seed the random number generator
    int number = rand() % 10 + 1; // generate a random number between 1 and 10
    int guess;
    for (int i = 0; i < 3; i++) {
        printf("Enter a number: ");
        scanf("%d", &guess);
        if (guess == number) {
            printf("You guessed the correct number!\n");
            break;
        } else if (guess < number) {
            printf("Too low\n");
        } else {
            printf("Too high\n");
        }
    }
}
```
[Back](./#guessing-game)