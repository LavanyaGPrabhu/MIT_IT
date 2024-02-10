	AREA RESET, DATA, READONLY
	EXPORT __Vectors
__Vectors
	DCD 0x40001000 ; stack pointer value when stack is empty
	DCD Reset_Handler ; reset vector
	
	ALIGN
	
	AREA mycode, CODE, READONLY
	ENTRY
	EXPORT Reset_Handler
Reset_Handler
	LDR R0,=NUM
	LDR R1,=RES
	LDRB R2,[R0]
	MOV	R3,#0
	MOV	R9,#0
	CMP R2,#100
	BCC DIV
DIP SUBS R2,R2,#100
	ADD R9,R9,#1
	CMP R2,#100
	BCS DIP
DIV CMP R2,#10
	BCS LP
	BCC OUT
LP	SUBS R2,R2,#10
	ADD R3,R3,#1
	CMP R2,#10
	BCS LP
OUT	MOV R5,#0x10
	MLA R9,R9,R5,R3
	MLA R9,R9,R5,R2
	STR R9,[R1]
STOP 
	B STOP
NUM DCD 0xFF
	AREA data, DATA, READWRITE
RES DCD 0
	END