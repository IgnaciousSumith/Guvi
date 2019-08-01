#include <bits/stdc++.h> 
using namespace std; 
  
string LexicographicalMaxString(string str) 
{ 
   
    string mx = ""; 
    for (int i = 0; i < str.length(); ++i) 
        mx = max(mx, str.substr(i)); 
  
    return mx; 
} 
int main() 
{ 
    string str = "string"; 
    cout << LexicographicalMaxString(str); 
    return 0; 
} 
