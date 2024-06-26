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
	LDR R0, =SRC; Load address of SRC into R0
	LDR R2, =DST
	MOV R3,#10 ; Store data from R3 into the address pointed by R1
LOOP	LDR R4,[R0],#4
		STR R4,[R2],#4
		SUBS R3,#1
		TEQ R3,#0
		BNE LOOP
STOP
	B STOP
SRC DCD 1,2,3,4,5,6,7,8,9,10; SRC location in code segment
	AREA DATASEG, DATA, READWRITE
DST DCD 0,0,0,0,0,0,0,0,0,0 ;DST location in Data segment
	END