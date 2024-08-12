'''*********************************************************************************************************************************
 * Name                 : script.py
 * Creation Date        : 25-05-2022
 * Last Modified        : 06-06-2022
----------------------------------------------------------------------------------------------------------------------------------
 * Author               : Badam Mayur Krishna
 * Author's Email       : mayurkrishna.b@alpha-numero.tech
----------------------------------------------------------------------------------------------------------------------------------
* Description           : dictionary for systemverilog
**********************************************************************************************************************************'''
myDict=dict()
#for,if,in,is,input,while...
#Adding items to the dictionary
myDict['info']= "This dictionary has descriptions and examples of various system verilog concepts"

myDict['for']= "keyword: for loop \nDescription: this is basically for loop...\nExample: \nfor i in range...."

myDict['if']= "keyword: if cond \nDescription: this is basically simple condition...\nExample:\nif(n==1):...."

myDict['fork']= "keyword: fork join \nDescription: fork join allows threading in SV...\nExample:\nfork \n  process1;\n  process2;\n  process3;\njoin"

myDict['reg']= "Keyword: reg \nDescription: 4-state value. single-bit datatype \nExample: reg r; "

myDict['bit']= "Keyword: reg \nDescription: 2-state value. single-bit datatype \nExample: bit b; "

myDict['integer']= "Keyword: integer \nDescription: 4-state value. 32-bit datatype \nExample: integer i; "

myDict['logic']= "Keyword: logic \nDescription: 4-state value. 0 or 1 or x or z  \nExample: logic l; "

myDict['byte']= "Keyword: byte \nDescription: 2-state value. 8 bit signed integer \nExample: byte b; "

myDict['int']= "Keyword: int \nDescription: 2-state value, 32-bit signed integer. \nExample: int i; "

myDict['shortint']= "Keyword: shortint \nDescription: 2-state value, 16-bit signed integer. \nExample: shortint s; "

myDict['longint']= "Keyword: longint \nDescription: 2-state value, 64-bit signed integer. \nExample: longint l; "

myDict['typedef']= "Keyword: typedef \nDescription: for defining user-defined datatypes. \nExample: typedef struct { bit [7:0] opcode; bit [23:0] addr;} instruction;"

myDict['class']= "Keyword: class \nDescription: A blueprint for a house Program element containing related group of features and functionality. \nExample: \nclass ABC;\n  int a; \n  int b;\n  print();\nendclass"

myDict['constructor']="Keyword: new() \nDescription: Used for creating memory for an object of a class\nExample: \nfunction new(input int a); \n  cmd = IDLE; \n  status = a;\nendfunction"

myDict['extends']="Keyword: extends \nDescription: inheritance. Subclass inherits properties and methods from parent subclass, can redefine methods explicitly\nExample: \nclass ErrPkt extends Packet; \n  bit[3:0] err; \n  function bit[3:0] show_err();\n  endfunction\nendclass"

myDict['event']="Keyword: event \nDescription: Synchronization for arbitration of shared resources, keys. Mutual Exclusivity control.\nExample: \nevent ev1,ev2;" 

myDict['semaphore']="Keyword: semaphore \nDescription: Synchronization for arbitration of shared resources, keys. Mutual Exclusivity control. \nExample:\nsemaphore shrdBus =new;\n shrdBus.get ();\n shrdBus.put();"

myDict['interface']="Keyword: interface \nDescription: An Interface Provides a hierarchical structure that encapsulates communication.\nExample: \ninterface intf;\n  int i;\n  wire [7:0] a;\nendinterface" 

myDict['assertion']="Keyword: assertion \nDescription: A concise description of desired / undesired behavior.\nExample: \nassert\n(expression)\n  action_block;" 

myDict['cast']="Keyword: cast\nDescription: A data type can be changed by using a cast operation. \nExample: \nint'(2.0 * 3.0);" 

myDict['size']= "Size of this dictionary: " + str(len(myDict))


#Takes input keyword and gives description
while(1):
    n=input("Enter a keyword\n Press 0 to exit: ")
    if n=='0':
        print("\nClosing...")
        break
    print("\n"+myDict[n]+ "\n")

#OUTPUT:
# Enter a keyword
#  Press 0 to exit: fork
# 
# keyword: fork join 
# Description: fork join allows threading in SV...
# Example:
# fork 
#   process1;
#   process2;
#   process3;
# join
# 
# Enter a keyword
#  Press 0 to exit: 0
# 
# Closing...

