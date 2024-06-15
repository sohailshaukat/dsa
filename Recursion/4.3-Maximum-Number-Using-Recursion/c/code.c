#include <stdio.h>

int max(int arr[], int idx, int length)
{

    if (idx == length - 1)
    {
        return arr[idx - 1];
    }

    int current = arr[idx];

    int other = max(arr, idx + 1, length);

    int result = (current > other) ? current : other;

    return result;
}

int main()
{

    int arr[] = {1, 10, 2, 3, 2, 9};

    int length = sizeof(arr) / sizeof(arr[0]);
    int maximum = max(arr, 0, length);

    printf("Maximum: %d\n", maximum);

    return 0;
}