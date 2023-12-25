void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int ar[],int low,int high)
{
    int i,pivot,j;
    i=low;
    pivot = ar[low];
    j = high -1;
    while(i<j && j>0)
    {
        while(i<high-1 && pivot>=ar[i])
            i++;
        while(pivot<ar[j])
            j--;
        if(i<j)
            swap(&ar[i],&ar[j]);
        swap(&ar[low],&ar[j]);
    }
    return j;
}

void quicksort(int ar[],int low,int high)
{
    if(low<high)
    {
        int j = partition(ar,low,high);
        quicksort(ar,low,j);
        quicksort(ar,j+1,high);
    }
}

int main()
{
    int n,i;
    int ar[10];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&ar[i]);
    quicksort(ar,0,n);
    for(i=0;i<n;i++)
        printf("%d ",ar[i]);
    printf("\n");
    return 0;
}