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
;N EQU 10
;OL EQU 2
	LDR R0, =SRC + (9)*4
	LDR R1, =SRC + (11)*4
	MOV R2,#10 
LOOP	LDR R3,[R0],#-4
		STR R3,[R1],#-4
		SUBS R2,#1
		TEQ R2,#0
		BNE LOOP
	;MOV R6,#0
	;LDR R7,=SRC
	;STR R6,[R7],#4
	;STR R6,[R7]
	
STOP
	B STOP

	AREA DATASEG, DATA, READWRITE
SRC DCD 1,2,3,4,5,6,7,8,9,10; SRC location in data segment
	END