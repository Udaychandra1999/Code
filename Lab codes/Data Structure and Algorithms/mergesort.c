#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int left, int mid, int right)
{
    int n1, n2, k, i, j;
    n1 = mid - left + 1;
    n2 = right - mid;
    int leftar[n1];
    int rightar[n2];

    for (i = 0; i < n1; i++)
        leftar[i] = arr[left + i];
    for (i = 0; i < n2; i++)
        rightar[i] = arr[mid + 1 + i];
    i = 0;
    j = 0;
    k = left;
    while (i < n1 && j < n2)
    {
        if (leftar[i] <= rightar[j])
        {
            arr[k] = leftar[i];
            i++;
        }
        else
        {
            arr[k] = rightar[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = leftar[i];
        i++;
        k++;
    }
    while (j < n2)
        {arr[k] = rightar[j];
            j++;
            k++;
        }
}

void mergesort(int arr[], int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        mergesort(arr, left, mid);
        mergesort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main()
{
    int n, i;
    scanf("%d", &n);
    int ar[10];
    for (i = 0; i < n; i++)
        scanf("%d", &ar[i]);
    mergesort(ar, 0, n - 1);
    for (i = 0; i < n; i++)
        printf("%d ", ar[i]);
    printf("\n");
    return 0;
}