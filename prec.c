#include <stdio.h>

void inputValues(int arr[], int maxSize, int *actualSize) {
    int value;
    *actualSize = 0; // Tracks the number of elements entered
    
    printf("Enter up to %d integers (enter -1 to stop):\n", maxSize);
    for (int i = 0; i < maxSize; i++) {
        printf("Value %d: ", i + 1);
        scanf("%d", &value);
        
        if (value == -1) { // Sentinel value to stop input
            break;
        }
        
        arr[i] = value;
        (*actualSize)++;
    }
}

// Example usage with max value of 3
int main() {
    int arr[3]; // Array with maximum capacity of 3
    int size;   // Actual number of elements entered
    
    inputValues(arr, 3, &size);
    
    printf("You entered %d values:\n", size);
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}