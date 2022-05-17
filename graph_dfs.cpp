#include <bits/stdc++.h>
using namespace std;

const int N=1e3+10;

vector <int> g[N];
bool vis[N];

void dfs(int vertex){
    cout<<vertex<<"\n";
    vis[vertex]=true;
    for(auto child:g[vertex]){
        // cout<<"parent"<<vertex<<" ,child"<<child<<"\n";
        if(vis[child]) continue;
        dfs(child);
    }
}

int main(int argc, char const *argv[])
{
    int n,m;
    cin>>n>>m;
    int v1,v2;
    for (int i = 0; i < m; i++)
    {
        
        cin>>v1>>v2;
        g[v1].push_back(v2);
        g[v2].push_back(v1);
    }
    dfs(2);
    return 0;
}

// input:
// 6 8
// 1 3
// 1 5
// 3 4
// 3 5
// 3 6
// 3 2
// 5 6
// 4 6

// output: 
// 4
// 3
// 1
// 5
// 6
// 2