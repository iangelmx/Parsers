run : a.out
	./a.out
clean : 
	rm *.o *.c *.h a.out

lex.yy.c : mfcalc.l mfcalc.tab.h
	flex mfcalc.l
mfcalc.tab.c : mfcalc.y
	bison -d mfcalc.y

mfcalc.tab.h: mfcalc.tab.c

tabla.o : tabla.c
	gcc tabla.c -c

lex.yy.o : lex.yy.c
	gcc -c lex.yy.c
mfcalc.tab.o : mfcalc.tab.c
	gcc -c mfcalc.tab.c

a.out : lex.yy.o mfcalc.tab.o tabla.o
	gcc mfcalc.tab.o lex.yy.o tabla.o -lm -ll