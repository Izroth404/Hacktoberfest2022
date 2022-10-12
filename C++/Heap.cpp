#include<bits/stdc++.h>
using namespace std;
void swap(int *x,int *y)
{
    int t=*x;
    *x=*y;
    *y=t;
}
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int h[n];
    int i=0;
    while(i<n)
    {
        h[i]=a[i];
        int j=i;
        int p=(j-1)/2;
        while(p>=0 && h[p]>h[j])
        {
            swap(&h[p],&h[j]);
            j=j-1/2;
            p=(j-1)/2;
        }
        i++;
    }
     for(int i=0;i<n;i++)
    {
        cout<<h[i];
    }
}
