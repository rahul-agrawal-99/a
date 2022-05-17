#include <bits/stdc++.h>

#include <iostream>

using namespace std;

const int N=1e3+10;

bool vis[N];

void printvector(vector <int> v){
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    
}

int main(int argc, char const *argv[])
{
    vector <pair<int,int>> vp;
    vector<int> v;
    cout<<"Enter length of job"<<endl;
    int n;
    cin>>n;
    cout<<"Please enter Profit-Deadline Pair in Descending order"<<endl;
    for (int i = 0; i < n; i++)
    {
        int p,t;
        cin>>p>>t;
        vp.push_back({p,t});
    }
    
//    printvec(vp);

    for (int i = 0; i < vp.size(); i++)
    {   
        if(!vis[vp[i].second]){
        v.push_back(vp[i].first);
        vis[vp[i].second]=true;
        }
    }
    cout<<accumulate(v.begin(),v.end(),0);


    return 0;
}
