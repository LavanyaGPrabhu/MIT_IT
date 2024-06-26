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
	LDRB R3,[R0] ; load hex number into register R1
	AND R4,R3,#0x0F ; mask upper 4 bits
	AND R5,R3,#0xF0
	LSR R5,#4
	MOV R6,#0xA
	MLA R7,R5,R6,R4
	STR R7,[R1]
STOP 
	B STOP
NUM DCD 0x64
	AREA data, DATA, READWRITE
RES DCD 0
	END