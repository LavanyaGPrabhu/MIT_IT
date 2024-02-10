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
	LDR R0,=SRC			;points to the LSB of the 1st 128 bit number
	LDR R1,=SRC+(4*4)	;points to the LSB of the 2nd 128 bit number
	LDR R2,=DST			;points to the address of DST
	MOV R3,#3			;counter
	LDR R4,[R0],#4
	LDR R5,[R1],#4
	ADDS R6,R4,R5
	STR R6,[R2],#4
LOOP	ADDS R7,R4,R5
		LDR R4,[R0],#4
		LDR R5,[R1],#4
		ADC R6,R4,R5
		;ADDS R7,R4,R5
		STR R6,[R2],#4
		SUBS R3,R3,#1
		CMP R3,#0
		;ADDS R7,R4,R5
		BNE LOOP
STOP
	B STOP
SRC DCD 0x11111111,0x11111111,0x11111111,0x11111111,0x22222222,0xF2222222,0x22222222,0x22222222; SRC location in code segment
	AREA DATASEG, DATA, READWRITE
DST DCD 0,0,0,0
	END