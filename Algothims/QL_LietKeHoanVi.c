#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_N 20

// Liet ke hoan vi

int n;
int x[MAX_N];
bool visited[MAX_N];

void solution () {
	for (int i = 1; i <= n; i++) printf("%d", x[i]);
	printf("\n");
}

bool check (int v, int k) {
	return visited[v] == false;
}

void Try (int k) {
	for(int v = 1; v <= n; v++ ) {
		if(check(v, k)) {
		// printf("%d", v);
			x[k] = v;
			visited[v] = true;

			if(k == n) solution();
			else Try(k+1);

			visited[v] = false;
		}

	}
}

int main () {

	n = 6;
	for(int i = 0; i < MAX_N; i++) visited[i] = false;
	Try(1);

	return 0;
}
