#include <iostream>

using namespace std;


int moveCount = 0;

void four_three_pegs(int i, int j, char a, char b, char c, char d)
{
    int m = j - i + 1;
    int k = sqrt(2 * m);
    cout << "**Here we  will start by moving first smallest k disks within the 4 pegs( A, B , C , D ) \n";
    four_pegs(m - k, a, d, b, c);
    cout << "**rest of disks will move within the 3 pegs( A , B , C ) excluding the peg 'D'\n";
    three_pegs(k, a, b, c);
    cout << "**then returning the first moved disks on top of the remaining disks \n";
    four_pegs(m - k, d, b, a, c);
}


void four_pegs(int n, char  p, char q, char r, char s)
{
    if (n == 0)
        return;

    if (n == 1)
    {
        cout << "Move disk 1 from rod " << p << " to rod " << q << endl;
        moveCount++;
        return;
    }

    four_pegs(n - 2, p, r, s, q);


    cout << "Move disk " << n - 1 << " from rod " << p << " to rod " << s << endl;
    cout << "Move disk " << n << " from rod " << p << " to rod " << q << endl;
    cout << "Move disk " << n - 1 << " from rod " << s << " to rod " << q << endl;
    moveCount += 3; 

    four_pegs(n - 2, r, q, p, s);
}

void three_pegs(int m, char p, char q, char r)
{
    if (m == 1)
    {
        cout << "Move disk 1 from rod " << p << " to rod " << q << endl;
        moveCount++;
        return;
    }
    three_pegs(m - 1, p, r, q);
    cout << "Move disk " << m << " from rod " << p << " to rod " << q << endl;
    moveCount++;
    three_pegs(m - 1, r, q, p);
}

int main()
{
    int n;
    cout << "Enter the number of disks: ";
    cin >> n;
    cout << endl;
    four_three_pegs(1, n, 'A', 'B', 'C', 'D');
    cout << "Total moves: " << moveCount << endl; 
    return 0;
}
