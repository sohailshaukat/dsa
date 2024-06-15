#include <stdio.h>

int sum(int arr[], int idx, int length)
{
    if (idx == length)
    {
        return 0;
    }
    return arr[idx] + sum(arr, idx + 1, length);
}

int main()
{
    int a[] = {1, 2, 3, 4};

    size_t n = sizeof(a) / sizeof(a[0]);

    int result = sum(a, 0, n);

    printf("Sum: %d", result);
    return 0;
}