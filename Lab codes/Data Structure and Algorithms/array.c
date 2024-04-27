#include <stdio.h>
int main()
{
    int n, i, j, key = 6, pos = 3, nu = 11;
    int a[20];
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    for (j = n; j > pos - 1; j--)
    {
        a[j + 1] = a[j];
    }
    a[j + 1] = nu;
    n = n + 1;
    printf("\n");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    for (i = 0; i < n; i++)
    {
        if (a[i] == 10)
        {
            j = i;
            n = n - 1;
            break;
        }
    }
    for (i = j; i < n; i++)
        a[i] = a[i + 1];
    printf("\n");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    for (i = 0; i < n; i++)
    {
        if (a[i] == key)
        {
            printf("\nItem %d Found in position:%d", key, i + 1);
            break;
        }
    }
    return 0;
}