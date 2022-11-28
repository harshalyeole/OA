int xorMultiplication(int N, int A, int B)
{
    long long int mod = 1000000007;
    long long int a = A;
    long long int b = B;
    for(int i=0;i<N;i++)
    {
        long long int p = (1<<i);
        int tmp1 = p&a;
        int tmp2 = p&b;

        if(tmp1==0 && tmp2==0)
        {
            a^=p;
            b^=p;
        }
    }
    long long int ans = ((a%mod) * (b%mod))%mod;
    return (int)ans;

}