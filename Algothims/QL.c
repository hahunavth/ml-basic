#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Liet ke sau do dai n khong chua 2 bit 1 lien tiep

int x[100];
int n;

void solution () {
	for (int i = 1; i <= n; i++) {
		printf("%d", x[i]);
	}
	printf("\n");
}

bool check(int v, int k) {
	if(k == 1) {
		return true;
	}
	// printf("%d", x[k-1] + v <= 1);
	return x[k-1] + v <= 1;
}

void Try (int k) {
	// printf("Try %d: ", k);
	for( int v = 0; v <= 1; v++ ) {
		if(check(v, k)) {
			x[k] = v;
			if(k == n) {
				solution();
			} else {
				// printf("\n");
				Try(k+1);
			}
		}
	}
}

void main () {
	n = 3; Try(1);
}