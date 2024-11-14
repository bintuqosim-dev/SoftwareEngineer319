#include <iostream>
#include <string>
using namespace std;

// Negation
bool negationP(bool p) {
    return !p;
}

bool negationQ(bool q) {
    return !q;
}

// Conjunction
bool conjunction(bool p, bool q) {
    return p && q;
}

// Disjunction
bool disjunction(bool p, bool q) {
    return p || q;
}

// Implication
bool implication(bool p, bool q) {
    return !p || q;
}

// Equivalence
bool equivalence(bool p, bool q) {
    return p == q;
}

// Exclusive OR (XOR)
bool exclusiveOr(bool p, bool q) {
    return p != q;
}

// Sheffer Stroke (NAND)
bool shefferStroke(bool p, bool q) {
    return !(p && q);
}

// Peirce's Arrow (NOR)
bool peircesArrow(bool p, bool q) {
    return !(p || q);
}

int main() {
    // Input p and q
    cout << "Enter the value of proposition P (0 or 1): ";
    bool p;
    cin >> p;

    cout << "Enter the value of proposition Q (0 or 1): ";
    bool q;
    cin >> q;

    // Logical operations
    cout << "Negation(P) : " << negationP(p) << endl;
    cout << "Negation(Q) : " << negationQ(q) << endl;
    cout << "Conjunction : " << conjunction(p, q) << endl;
    cout << "Disjunction : " << disjunction(p, q) << endl;
    cout << "Implication : " << implication(p, q) << endl;
    cout << "Equivalence : " << equivalence(p, q) << endl;
    cout << "Exclusive OR : " << exclusiveOr(p, q) << endl;
    cout << "Sheffer Stroke : " << shefferStroke(p, q) << endl;
    cout << "Peirce's Arrow : " << peircesArrow(p, q) << endl;

    return 0;
}


