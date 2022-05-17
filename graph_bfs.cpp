#include <bits/stdc++.h>
using namespace std;

const int N=1e3+10;

vector <int> g[N];
bool vis[N];

void bfs(int source){
	queue <int> q;
    q.push(source);
    vis[source]=true;
    
    while(!q.empty()){
        int cur_v=q.front();
        q.pop();
        cout<<cur_v<<" ";
        for (auto child : g[cur_v])
        {
            if(!vis[child]){
                q.push(child);
                vis[child]=true;
            }
            

        }
        
    }
}

int main()
{
	int n,m;
	cin>>n;
	int v1,v2;
	for (int i = 0; i < n-1; i++)
	{
		cin>>v1>>v2;
		g[v1].push_back(v2);
		g[v2].push_back(v1);
	}
	bfs(1);

	return 0;
	
}

