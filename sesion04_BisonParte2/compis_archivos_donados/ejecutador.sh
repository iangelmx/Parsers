bison rpcalc.y
bison rpcalc.y -d
flex rpcalc.l
gcc -c lex.yy.c
gcc -c rpcalc.tab.c 
gcc lex.yy.o rpcalc.tab.o  -ll -lm
./a.out