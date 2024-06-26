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
	LDR R1,=DST
	LDR R2,[R1]
	MOV R3,#10
LOOP	LDR R4,[R0],#4
		ADD R2,R2,R4
		SUBS R3,R3,#1
		TEQ R3,#0
		BNE LOOP
	STR R2,[R1]
STOP
	B STOP
SRC DCD 1,2,3,4,5,6,7,8,9,10; SRC location in code segment
	AREA DATASEG, DATA, READWRITE
DST DCD 0
	END