#include <stdio.h> 
#include <netdb.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 

#define PORT_NO 50001 
#define BUF_MAX 64

static struct sockaddr_in sv_addr; 
static struct hostent  *sv_ip;
static int sid;
static char buf[BUF_MAX];

int main(argc, argv)
int argc;
char *argv[];
{
    int rtn;

    sid = socket(AF_INET,SOCK_STREAM,0);
    if (sid < 0){
        perror("cl:socket");
        exit(1);
    }

    sv_ip = gethostbyname(argv[1]);
    if (sv_ip == NULL){
        perror("cl:gethostbyname");
        close(sid);
        exit(1);
    }

    bzero((char *)&sv_addr, sizeof(sv_addr));
    sv_addr.sin_family = AF_INET;
    sv_addr.sin_port = htons(PORT_NO);
    memcpy((char *)&sv_addr.sin_addr, (char *)sv_ip->h_addr, sv_ip->h_length);
    rtn = connect(sid, (struct sockaddr *)&sv_addr, sizeof(sv_addr));
    if (rtn <0) {
        perror("cl:connect");
        close(sid);
        exit(1);
    }

    rtn = shutdown(sid ,2);
    if (rtn <0) perror("cl:shutdown");
    close(sid);
    exit(0);
}