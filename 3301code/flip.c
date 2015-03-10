#include <stdio.h>
//flip a file bitewise
int main (){
file f, g;
f=open("infile", "r");
g=open("newfile", "w+");
g.write(f.read()[::-1]);
g.close;
f.close;

}
