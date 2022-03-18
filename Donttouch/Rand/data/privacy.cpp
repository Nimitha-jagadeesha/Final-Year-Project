#include <bits/stdc++.h>

using namespace std;
long long int edges[2016][2016];
int main()
{
    ifstream fin("fbedges.txt");
    ofstream fout("fbprivacy.txt");

    for(int i=0;i<2016;i++)
    {
        for(int j=0;j<2016;j++)
            {
                fin>>edges[i][j];

            }
    }
    float m,n,w;
     for(int i=0;i<2016;i++)
     {
        for(int j=0;j<2016;j++)
            {
               m = edges[i][j];
                n=0;
                w=0;
                if(m==1)
                    {
                        for(int k=0;k<10;k++)
                        {
                            n += edges[i][k]&&edges[j][k];
                            w += edges[i][k]||edges[j][k];
                        }
                    }
                if(w)
                fout<<(n/w)<<" ";
                else
                    fout<<0<<" ";
            }
            fout<<endl;
     }
     return 0;
}


