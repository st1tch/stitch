#include <stdio.h>
#include <stdlib.h>

int main(){
	int fd = open("/dev/urandom", 0); 
	void *buf ;
	buf = malloc(20) ;
	read(fd, buf, 20) ;
	printf("%s\n", buf) ;
	read(fd, buf, 20) ;
	printf("%s\n", buf) ;
	return 0 ;
}
