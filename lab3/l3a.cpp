#include <bits/stdc++.h>
using namespace std;

int32_t main() {
    vector<double> x(4);
    for (int i = 0; i < 4; i++) {
        x[i] = i;
    }
    
    vector<double> f(4);
    for (int i = 0; i < 4; i++) {
        cin >> f[i];
    }
    
    double sxf = 0;
    for (int i = 0; i < 4; i++) {
        sxf += x[i] * f[i];
    }
    
    double p = sxf / (100 * 3);
    cout << p << endl;
    
    vector<double> F(4);
    
    
  
    
    F[0] = 100 *pow(0.7,3);
    cout << F[0] << " ";
    
    for (int i = 1; i < 4; i++) {
        F[i] = ((3- x[i]) / (x[i] + 1)) * (0.3/0.7) * F[i - 1];
        cout <<F[i] << " ";
    
    }
    return 0;
}
