#include<stdio.h>





int fib(int n)  // store n on the stack--> r0 is free
{
  if((n-2)>0)
  {
    return fib(n-1)+fib(n-2);
  }
  else return 1;
}




//  LAST
//  r0=1;              //set return value
//  pop {r7,pc}        // pop r7  and set pc=lr



//  FIB
//
//  push  {r7, lr}     //r7 holds frame pointer
//  cmp r0 #2
//  blt  LAST          //if n==2 retun 1
//  sub sp, sp, #12    //make space for 1 integer
//  add r7, sp, #0     //r7 = sp-12
//  str r0, [r7, #4]   //store value of r0
//  sub r0, r0, #1     // r0=n-1
//  FIB                // fib(n-1)
//  str r0, [r7, #8]   // store fib(n-1)
//  ldr r0, [r7, #4]   // r0=n
//  sub r0, r0, #2     // r0=n-2
//  FIB                // fib(n-2)
//  ldr r1, [r7, #8]   // r1 = fib(n-1)
//  add r0, r0, r1     // r0=fib(n-1) + fib(n-2)
//  add sp, sp, #12    // restore the stack pointer
//  pop {r7,pc}        // pop r7  and set pc=lr



int main()
{
  int  one=fib(13);
  printf("result: %d\n",one);
  return 0;
}
