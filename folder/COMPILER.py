import re

def COMPILER(code: str):
    code = code.split('\n')
    for i in range(len(code)):
        if code[i][-1] == ';' and code[i][-3] in '+-*/' and code[i][-2].isdigit():
            code[i] = f"{code[i][:-5:]}{code[i][-3]}{code[i][-3]};"
    print('\n'.join(code))


code = """#include <stdio.h>
int main()
{
   int a=5;
   a=a+1;
   int b=a*a;
   b=b+1;
   printf(“a=%d\tb=%d\n”,a,b);
   return 0;
}"""

print(COMPILER(code))