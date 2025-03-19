#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    long long X;
    cin >> N >> X;
    vector<long long> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }
    
    // Sort the shops by their initial price
    sort(A.begin(), A.end());
    
    // Compute prefix sums: prefix[k] = sum of first k elements (1-indexed)
    vector<long long> prefix(N+1, 0);
    for (int k = 1; k <= N; k++){
        prefix[k] = prefix[k-1] + A[k-1];
    }
    
    // f[k] = maximum day d for which buying from k cheapest shops is affordable:
    // i.e. prefix[k] + k*(d-1) <= X  =>  d <= ((X - prefix[k]) / k) + 1
    // We'll only consider k for which prefix[k] <= X.
    vector<long long> f(N+2, 0); // using 1-indexing, f[m+1] will be set to 0.
    int m = 0; // maximum valid k
    for (int k = 1; k <= N; k++){
        if (prefix[k] > X) break;
        m = k;
        f[k] = ((X - prefix[k]) / k) + 1;  // integer division
    }
    f[m+1] = 0; // define boundary
    
    // Total beers bought = sum_{k=1}^{m} k * (f(k) - f(k+1))
    long long ans = 0;
    for (int k = 1; k <= m; k++){
        ans += (long long) k * (f[k] - f[k+1]);
    }
    
    cout << ans << "\n";
    return 0;
}
