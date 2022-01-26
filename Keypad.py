


GPIO_KeyCol=[False,False,False,False,False]
GPIO_KeyRow=[False,False,False,False]
Keypad_Key=['previous','next','reset','silence','ack','up','down','left','right','enter','1','2','3','4','5','6','7','8','9','0','*','#' ]


Key_cols=0xFE
Key_rows=0xFF
for i in GPIO_KeyCol:
 print(bin(Key_cols))
 Key_cols=((Key_cols<<1)&0xFF)|0x01




def GPIO_Col_Values(GPIO_col0,GPIO_col1,GPIO_col2,GPIO_col3,GPIO_col4):
 cols=0
 if GPIO_col0==True:
  cols=cols|0b00000001
 else:
  cols=cols&0b11111110
 if GPIO_col1==True:
  cols=cols|0b00000010
 else:
  cols=cols&0b11111101
 if GPIO_col2==True:
  cols=cols|0b00000100
 else:
  cols=cols&0b11111011
 if GPIO_col3==True:
  cols=cols|0b00001000
 else:
  cols=cols&0b11110111
 if GPIO_col4==True:
  cols=cols|0b00010000
 else:
  cols=cols&0b11101111
 print(bin(cols))
 return cols
