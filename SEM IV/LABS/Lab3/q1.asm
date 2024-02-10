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
	LDR R0,=DST
	LDR R1,[R0]
	MOV R2,#0
	MOV R3,#1
	MOV R4,#1
LOOP	CMP R1,#1
		BCC OUT
		MLA R2,R2,R3,R4
		ADD R4,R4,#1
		SUB R1,R1,#1
		BNE LOOP
OUT	STR R2,[R0]
STOP
	B STOP
	AREA DATASEG, DATA, READWRITE
DST DCD 0
	END