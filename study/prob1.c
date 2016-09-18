#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hhhhh(int v1, int v2, int v3){
	int tmp = 7 ;
	tmp += v1 ;
	tmp *= v2 ;
	tmp += v3 ;
	return tmp ;
}

int good(int v1, int v2, int v3, int v4){
	int tmp = 10 ;
	tmp *= v1 ;
	tmp += v3 ;
	tmp *= v2 ;
	tmp += v4 ;
	return tmp ;
}

int main(int argc, char**argv){
	int a[10] = {0, } ;
	int i ;
	size_t len ;
	int sum = 0 ;
	for(i = 0 ; i < 10 ; i++)
		scanf("%d", &a[i]) ;

	sum = hhhhh(argc, atoi(argv[1]), a[6]) ;
	printf("First Stage : %d\n", sum) ;
	sum = good(sum, atoi(argv[2]), a[2], a[7]) ;
	printf("Second Stage : %d\n", sum) ;
	len = strlen(argv[0]) + 77 ;
	printf("Final Stage : %zu\n", len) ;
	return 0 ;
}
