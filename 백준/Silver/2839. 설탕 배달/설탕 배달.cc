#include <iostream>
#include <list>

using namespace std;

int main() {
	int n = 0;
	cin >> n;
	for (int i = 0; i <= n / 5; i++) {
		if ((n - 5 * (n / 5 - i)) % 3 == 0) {
			cout << n / 5 - i + (n - 5 * (n / 5 - i)) / 3;
			break;
		}
		if (i == n / 5) {
			cout << -1;
		}
	}

}