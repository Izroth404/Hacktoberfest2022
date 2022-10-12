#include<bits/stdc++.h>
using namespace std;
struct node{
int a,b,c;
};
typedef struct node * nptr;
bool cmp(nptr a,nptr b)
{
    return a->a<b->a;
}
int find(int x,int s[])
{
    if(s[x]==-1)
        return x;
    else
        return find(s[x],s);
}
void u(int x,int y,int s[])
{
    if(s[y]==-1)
    {
        s[y]=x;
    }
    else if(s[x]==-1)
    {
        s[x]=y;
    }
    else
    {
        s[find(y,s)]=find(x,s);
    }
}
void kruskal(nptr w[],int n)
{
    int s[8];
    for(int i=0;i<8;i++){s[i]=-1;}
    int cnt=0;
    cout<<w[0]->b<<" "<<w[0]->c<<endl;
    int sum=w[0]->a;
    u(w[0]->b,w[0]->c,s);
    for(int i=1;i<12;i++)
    {
        if(find(w[i]->b,s)!=find(w[i]->c,s))
        {
            sum+=w[i]->a;
            u(w[i]->b,w[i]->c,s);
            cout<<w[i]->b<<" "<<w[i]->c<<endl;
            cnt++;
        }
        if(cnt==n-2){break;}
    }
cout<<sum<<endl;
}


int main()
{
    int n=8;
    int e=12;

    vector<vector<int>> g(n+1 , vector<int> (n+1, 0));
    int u[]={1,6,1,3,2,1,4,3,5,4,4,2};
	int v[]={4,7,2,4,4,3,7,6,7,5,6,5};
	int w[]={1,1,2,2,3,4,4,5,6,7,8,10};
	nptr ew[12];
	for(int i=0;i<12;i++)
    {
        ew[i]=new(node);
    }
    for(int i=0;i<e;i++)
    {
        g[u[i]][v[i]]=w[i];
        g[v[i]][u[i]]=w[i];
        ew[i]->a=w[i];
        ew[i]->b=u[i];
        ew[i]->c=v[i];
    }
    sort(ew,ew+12,cmp);
    kruskal(ew,n-1);
}






