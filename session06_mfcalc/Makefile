run : a.out
	./a.out
clean : 
	rm *.o mfcalc.tab.h mfcalc.tab.c a.out lex.yy.c

lex.yy.c : mfcalc.l mfcalc.tab.h
	flex mfcalc.l
mfcalc.tab.c : mfcalc.y
	bison -d mfcalc.y

mfcalc.tab.h: mfcalc.y
	bison -d mfcalc.y

tabla.o : tabla.c
	gcc -c tabla.c

lex.yy.o : lex.yy.c
	gcc -c lex.yy.c
	
mfcalc.tab.o : mfcalc.tab.c
	gcc -c mfcalc.tab.c

main.o: main.c
	gcc -c main.c

a.out : lex.yy.o mfcalc.tab.o tabla.o 
	gcc mfcalc.tab.o lex.yy.o tabla.o  -lm -ll