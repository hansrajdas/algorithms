#include "stdio.h"

int sum(int stackI[], int p, int n)
{
    int j=n-1;
    int sumOfTopElement=0;
    while(p)
    {
        sumOfTopElement += stackI[j--];
        p--;
    }
}
void solution(int stack[][],int K)
{
    int dp[stack.size()][K+1];
    memset(dp, 0, sizeof dp);
    int i = 0;
    for(int k=1;k<=K;k++)
    {
        if(stack[0].size()>=k)
            dp[i][k]=sum(stack[0],k,stack[0].size());
    }
    for(int i=1;i<n;i++)
    {
        for(int k=1;k<=K;k++)
        {
            dp[i][k]=dp[i-1][k];
            for(int j=1;j<=k;j++)
            {
                if(stack[i].size()>=j)
                    dp[i][k]=max(dp[i][k],dp[i-1][k-j]+sum(stack[i],j,stack[i].size()));
            }
        }
    }
    printf("%d", dp[stack.size()][K + 1])
}

int main() {
    solution([[1,1,100,3],[2000,2,3,1],[10,1,4]], 3)
}
