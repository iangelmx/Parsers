run : a.out
	./a.out
clean : 
	rm *.o *.c *.h a.out

lex.yy.c : infix_calc.l infix_calc.tab.c
	flex infix_calc.l
infix_calc.tab.c : infix_calc.y
	bison -d infix_calc.y
lex.yy.o : lex.yy.c
	gcc -c lex.yy.c
infix_calc.tab.o : infix_calc.tab.c
	gcc -c infix_calc.tab.c
a.out : lex.yy.o infix_calc.tab.o
	gcc infix_calc.tab.o lex.yy.o -lm -ll