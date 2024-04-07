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
	MOV R3,#0
	LDR R4,[R0]
	LDR R5,[R1]
LP	ADD R3,R3,R4
	SUB R5,R5,#1
	CMP R5,#0
	BNE LP
	STR R3,[R2]
STOP
	B STOP
SRC DCD 14,4; SRC location in code segment
	AREA DATASEG, DATA, READWRITE
DST DCD 0
	END