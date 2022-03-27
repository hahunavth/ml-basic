#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_N 20

// Liet ke nghiem nguyen duong cua pt tuyen tinh
// x1 + x2 ... xn = M

int n;
int x[MAX_N];
int M = 0;
int T;

bool check (int v, int k) {
	if(k < n) return true;
	return T + v == M; 
}

void solution () {
	for (int i = 1; i <= n; i++)
	{
		printf ("%d ", x[i]);
	}
	printf("\n");
}

void Try (int k) {
	for (int i = 1; i <= M - T - (n - k) ; i++)
	{
		if(check(i, k)) {
			x[k] = i;
			T = T + x[k];

			if(k == n) solution();
			else Try(k+1);

			T = T - x[k];
		}
	}
}


int main () {

	n = 3;
	M = 5;
	T = 0;
	Try(1);

	return 0;
}