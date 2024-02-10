	AREA RESET, DATA, READONLY
	EXPORT __Vectors
 
__Vectors 
	DCD 0x10001000 ; stack pointer value when stack is empty
	DCD Reset_Handler ; reset vector
 
	ALIGN
	AREA mycode, CODE, READONLY
	ENTRY
	EXPORT Reset_Handler
Reset_Handler
	LDR R0,=SRC
	LDR R1,=DST+(9*4)
	MOV R2,#10
LOOP	LDR R3,[R0],#4
		STR R3,[R1],#-4
		SUBS R2,#1
		TEQ R2,#0
		BNE LOOP	
STOP
	B STOP
SRC DCD 1,2,3,4,5,6,7,8,9,10; SRC location in code segment
	AREA DATASEG, DATA, READWRITE
DST DCD 0,0,0,0,0,0,0,0,0,0
	END