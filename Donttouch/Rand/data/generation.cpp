#include <bits/stdc++.h>

using namespace std;
int main()
{
    int nn = 2015;
    int mm = 2015;
    ifstream fin("fbsecrets.txt");
     ofstream fout("fbthershold.txt");
     float m,n;
     for(int i=0;i<nn;i++)
     {
        for(int j=0;j<mm;j++)
            {
                fin>>m;
                n=0;
                if(m==1)
                    n = ((rand()%99)+1.0)/100.0;
                fout<<n<<" ";

            }
            fout<<endl;
     }
     return 0;
}

