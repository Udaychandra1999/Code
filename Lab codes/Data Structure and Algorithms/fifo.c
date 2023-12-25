#include<stdio.h>
#include<stdlib.h>

#define MAX_SIZE 100
int main()
{
    int at[MAX_SIZE],bt[MAX_SIZE],tat[MAX_SIZE],ct[MAX_SIZE],pid[MAX_SIZE],wt[MAX_SIZE];
    int n,i,j,temp,crt=0;
    float awt=0.0,atat=0.0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        pid[i] = i+1;
        scanf("%d%d",&at[i],&bt[i]);
    }
    //First in first out sorting it out
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(at[i]<at[j])
            {
               temp = at[i];
               at[i] = at[j];
               at[j] = temp;
               temp = bt[i];
               bt[i] = bt[j];
               bt[j] = temp;
               temp = pid[i];
               pid[i] = pid[j];
               pid[j] = temp; 
            }
        }
    }
    if(crt<=at[0])
    {
        crt = at[0];
    }
    for(i=0;i<n;i++)
    {
        ct[i] = crt + bt[i];
        crt = ct[i];
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];
        atat = atat + tat[i];
        awt = awt + wt[i];
    }
    atat = atat/n;
    awt = awt/n;
    for(i=0;i<n;i++)
    {
        printf("P%d ",pid[i]);
    }
    printf("\n");
    // To display the elements the process need to be sorted order

    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(pid[i]>pid[j])
            {
                temp = pid[i];
                pid[i] = pid[j];
                pid[j] = temp;
                temp = tat[i];
                tat[i] = tat[j];
                tat[j] = temp;
                temp = wt[i];
                wt[i] = wt[j];
                wt[j] = temp;
                temp = at[i];
                at[i] = at[j];
                at[j] = temp;
                temp = bt[i];
                bt[i]= bt[j];
                bt[j] = temp;
                temp = ct[i];
                ct[i] = ct[j];
                ct[j] = temp;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        printf("P%d %d %d\n",pid[i],tat[i],wt[i]);
    }
    printf("%1.1f %1.0f",atat,awt);
  return 0;
}