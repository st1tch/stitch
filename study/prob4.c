#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static int i1 = 0x1234 ; 
int i2 = 10 ;
char* s1 = "test1test2test3test4" ;

void func1(int v1, int *v2, int v3){
	*v2 = v1 + v3 + i1 + i2 + strlen(s1) ;
}

int main(int argc, char**argv){
	char b2[128]  ; 
	int *b3 ;
	size_t size ; 
	int i ;
	size_t len = 0 ;
	int sum = 0 ;
	int tmp1, tmp2 ;
	int v3 = 0 ; 

	if (argc != 7) {
		printf("[!]Error!!, argc = 7!\n") ;
		exit(1) ;
	}
	
	printf("Stage1!!\n") ;
	printf("input number! -> ") ;
	tmp2 = strlen(argv[0]) ;
	scanf("%d", &tmp1) ;
	if (tmp2 != tmp1){
		printf("Wrong answer!\n") ;
		exit(1) ;
	}
	printf("Stage1 Clear!!\n\n") ;
		
	size = 10 ;
	b3 = (int *)malloc(sizeof(int) * size) ;

	for(i = 0 ; i < size ; i++){
		b3[i] = rand() % 100 + 1 ;
		sum += b3[i] ;
	}
	
	printf("Stage2!!\n") ;
	printf("input number less than argc -> ") ;
	scanf("%d", &tmp1) ;
	if (atoi(argv[tmp1]) != sum){
		printf("Wrong answer!\n") ;
		exit(1) ;
	}
	printf("Stage2 Clear!!\n\n") ;

	printf("Stage3!!\n") ;
	printf("Check Argv!!\n") ;
	sleep(2) ;
	if ( strcmp(argv[3], argv[5])){
		printf("Wrong answer!\n") ;
		exit(1) ;
	}
	printf("Stage3 Clear!!\n\n") ;

	for(i = 0 ; i < argc ; i++)
		len += strlen(*(argv+i)) ;
	
	func1(len, &v3, 10) ;
	
	printf("Stage4!!\n") ;
	printf("Enter Last Answer! -> ") ;
	scanf("%d", &tmp1) ;
	if(v3 != tmp1){
		printf("Wrong answer!\n") ;
		exit(1) ;
	}

	printf("Good Day!") ;
	return 0 ;
}

