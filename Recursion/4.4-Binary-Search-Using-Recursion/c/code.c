#include <stdio.h>

int search(int arr[], int element, int length)
{
    int low = 0;
    int high = length - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        int guess = arr[mid];

        if (guess == element)
        {
            return mid;
        }
        if (element < guess)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return -1;
}

int main()
{
    int arr[10];

    for (int i = 0; i < 10; i++)
    {
        arr[i] = i + 1;
    }

    int result = search(arr, 5, 10);

    printf("Element found at: %d\n", result);

    return 0;
}