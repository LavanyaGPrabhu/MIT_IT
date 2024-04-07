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
	LDR R1,=SRC+4
	LDR R2,=DST
	LDR R3,[R0]
	LDR R4,[R1]
	MUL R5,R3,R4
	MOV R6,#0
LP	CMP R3,R4
	BHI UP
	BCC DN
	BNE LP
LCM SUB R5,R5,R4
	ADD R6,R6,#1
	CMP R5,R4
	BCC LAST
	B LCM
LAST    STR R6,[R2]
UP	SUB R3,R3,R4
	B LP
DN	SUB R4,R4,R3
	B LP
STOP
	B STOP
SRC DCD 17,21; SRC location in code segment
	AREA DATASEG, DATA, READWRITE
DST DCD 0
	END