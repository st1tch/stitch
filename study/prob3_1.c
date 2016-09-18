#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int first(int *arr, int size){
    int tmp = arr[size-4] ;
    tmp = tmp << 3 ;
    tmp += arr[2] ;
    return tmp ;
}

void final(int *arr, int size){
    int i ;
    int tmp ;
    for(i = 0 ; i < size/2; i+=2){
        tmp = arr[i] ;
        arr[i] = arr[i+1] ;
        arr[i+1] = tmp ;
    }
}

int main(int argc, char **argv){
    int *arr ;
    char *strstr ;
    int i ;
    int tmp ;
    int *tmparr ;
    int size ;
    char *str = argv[0] ;
    srand(time(NULL)) ;

    if(argc != 2){
        printf("exec format -> ./exec number\n") ;
        exit(1) ;
    }
    if(atoi(argv[1]) < 5){
        printf("please number > 5 !!\n") ;
        exit(1) ;
    }

    size = atoi(argv[1]) ;
    arr = malloc(sizeof(int) * size) ;

    for(i = 0 ; i < size ; i++){
        arr[i] = rand() % 80 + 10 ;
        printf("%d ",arr[i]) ;
    }
    printf("\n") ;

    printf("\nFirst answer -> ") ;
    scanf("%d", &tmp) ;
    if(tmp != first(arr, size)){
        printf("wrong answer!") ;
        exit(1) ;
    }

    printf("\nSecond answer -> ") ;
    scanf("%s", strstr) ;
    if(strcmp(str, strstr)){
        printf("wrong answer!") ;
        exit(1) ;
    }

    tmparr = malloc(sizeof(int) * size) ;
    printf("\nFinal answer %d number)\n-> ", size) ;
    for(i = 0 ; i < size ;i++)
        scanf("%d", &tmparr[i]) ;

    final(arr, size) ;

    for(i = 0 ; i < size ; i++){
        if(tmparr[i] != arr[i]){
            printf("wrong answer!") ;
            exit(1) ;
        }
    }

    printf("Good!!!!!!!!!!!\n") ;
    return 0 ;
}
