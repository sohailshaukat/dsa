#include <stdio.h>

int length(int arr[], int idx)
{
    if (arr[idx] == '\0')
    {
        return 0;
    }

    return 1 + length(arr, idx + 1);
}

int main()
{
    int a[] = {1, 2, 3, 4, 5};

    int result = length(a, 0);

    printf("Length:%d\n", result);
    return 0;
}