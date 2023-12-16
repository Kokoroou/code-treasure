#include<string>
#include<iostream>
using namespace std;

string encrypt(char c) {
    c = toupper(c);
    switch (c) {
        case 'A': return "604";
        case 'B': return "9236";
        case 'C': return "1874";
        case 'D': return "9632";
        case 'E': return "1964";
        case 'F': return "196";
        case 'G': return "18743";
        case 'H': return "9821";
        case 'I': return "05";
        case 'J': return "056";
        case 'K': return "187";
        case 'L': return "964";
        case 'M': return "69514";
        case 'N': return "94";
        case 'O': return "9641";
        case 'P': return "296";
        case 'Q': return "19643";
        case 'R': return "9274";
        case 'S': return "1836";
        case 'T': return "905";
        case 'U': return "9514";
        case 'V': return "951";
        case 'W': return "86042";
        case 'X': return "9416";
        case 'Y': return "9815";
        case 'Z': return "9164";
        case '.': return ".";
        case ',': return ",";
        case ' ': return ";";
    }
}

int main() {
    string sentence;
    cout << "Nhap cau can ma hoa: ";
    getline(cin, sentence);

    cout << "Ket qua sau khi ma hoa:" << endl;
    for (int i = 0; i < sentence.size(); i++) {
        cout << encrypt(sentence[i]);

        if (i == sentence.size()-1) continue;
        if (sentence[i] == ' ' || sentence[i] == '.' || sentence[i] == ',') {
            cout << " ";
            continue;
        }

        if (sentence[i+1] == ' ' || sentence[i+1] == '.' || sentence[i+1] == ',') continue;
        cout << ", ";
    }
    cout << endl << endl;
    system("pause");
}
