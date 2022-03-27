#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int X[9][9];
bool fix[9][9];

// mark?[?][v]
bool markR[9][10];
bool markC[9][10];
bool markS[3][3][10];

void solution () {
	for(int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			printf("%d  ", X[i][j]);
		}
		printf("\n");
	}
	printf("----------------------\n");
}

bool check (int v, int r, int c) {
	if(markR[r][v]) return false;
	if(markC[c][v]) return false;
	if(markS[r/3][c/3][v]) return false;
	return true;
}

void Try (int r, int c) {

	if(fix[r][c]) {
		if(r == 8 && c == 8) solution();
		else {
			if(c == 8) Try(r+1, 0);
			else {
				// printf("@@ %d %d\n", r, c+1 );
				Try(r, c+1);
			}
		}
		return;
	}

	// printf("%d %d\n", r, c);
	for (int i = 1; i <= 9; i++) {
		if(check(i, r, c)) {
			// printf("running %d %d\n", r, c);
				X[r][c] = i;
				markR[r][i] = true;
				markC[c][i] = true;
				markS[r/3][c/3][i] = true;

			if(r == 8 && c == 8) solution();
			else {
				if(c == 8) Try(r+1, 0);
				else {
					// printf("@@ %d %d\n", r, c+1 );
					Try(r, c+1);
				}
			}

				markR[r][i] = false;
				markC[c][i] = false;
				markS[r/3][c/3][i] = false;

		}
	}
}

void add_default_value (int v, int r, int c) {
	X[r][c] = v;
	markC[c][v] = true;
	markR[r][v] = true;
	markS[r/3][c/3][v] = true;
	fix[r][c] = true;
}

int main () {
	for(int i = 0; i < 9; i++) {
		for(int j = 0; j < 10; j++) {
			markR[i][j] = false;
			markC[i][j] = false;
		}
	}
	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++) {
			for(int k = 0; k < 10; k++) {
				markS[i][j][k] = false;
			}
		}
	}
	for(int i = 0; i < 9; i++)
		for(int j = 0; j < 9; j++){
			// X[i][j] = 0;
			// printf("%d", X[i][j]);
		}
	// X[1][2] = 100;
	// printf("\n%d", X[1][2]);

	add_default_value(1, 8, 8);
	add_default_value(2, 2, 1);
	add_default_value(3, 3, 1);
	add_default_value(4, 4, 1);
	add_default_value(5, 5, 1);
	add_default_value(6, 3, 2);
	add_default_value(7, 4, 7);
	add_default_value(8, 8, 7);
	add_default_value(9, 7, 8);
	add_default_value(9, 6, 2);
	add_default_value(6, 7, 6);
	// add_default_value(3, 8, 6);
	// add_default_value(9, 5, 7);




	Try(0, 0);

	return 0;
}