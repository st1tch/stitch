#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static int v1 = 0x777 ;

void func1(int **arr, int row, int col){
	int i, j ;
	for(i = 0 ; i < row ; i++){
		for(j = 0 ; j < col ;j++){
			printf("%d ", arr[i][j]) ;
		}
		printf("\n") ;
	}
}

int func2(int **arr, int num, int col){
	int i ;
	int sum = v1 ;
	for(i = 0 ; i < col ; i++)
		sum += arr[num][i] ;
	return sum ;
}

int main(int argc, char **argv){
	int col, row ;
	int **arr ;
	int i, j ;
	int tmp ;
	int sum = 0 ;

	if(argc != 3){
		printf("format -> ./exec num1 num2\n") ;
		exit(1) ;
	}

	srand( (unsigned)time(NULL)) ;
	col = atoi(argv[1]) + 3 ;
	row = atoi(argv[2]) + 5 ;

	arr = (int **)malloc(sizeof(int*) * row) ;
	for(i = 0 ; i < row ; i++)
		arr[i] = (int *)malloc(sizeof(int) * col) ;
	
	for(i = 0 ; i < row ; i++){
		for(j = 0 ; j < col ; j++){
			arr[i][j] = rand() % 100 + 1 ;
		}
	}

	func1(arr, row, col) ;	
	printf("input 1 ~ %d number -> ", row) ;
	scanf("%d", &tmp) ;
	sum = func2(arr, tmp-1, col) ;
	printf("result = %d\nbye!!!\n", sum) ;

	for(i = 0 ; i < row; i++)
		free(arr[i]) ;
	free(arr) ;

	return 0 ;
}
