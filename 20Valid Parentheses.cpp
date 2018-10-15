class Solution {
public:
    bool isValid(string s) {
    string fir = "";
    for (char& c:s) {
        if (c == '(' || c == '[' || c == '{') {
            fir.push_back(c);
        }else{
            if (abs((int)fir[fir.size()-1] - (int)c) <=2) fir.pop_back();
            else return false;
        }
    }
    return fir.size() == 0;
    }
};