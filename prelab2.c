#include<stdio.h>
#include<string.h>


void morse_decode(int value_in)
{
// 1 is a long and 0 is a short
  char *zero=   "11111";
  char *one=    "01111";
  char *two=    "00111";
  char *three=  "00011";
  char *four=   "00001";
  char *five=   "00000";
  char *six=    "10000";
  char *seven=  "11000";
  char *eight=  "11100";
  char *nine=   "11110";

  switch(value_in)
  {
    case 0:
      {
        printf("the morse code representation is: %s\n", zero);
      }
      break;
    case 1:
      {
        printf("the morse code representation is: %s\n", one);
      }
      break;

    case 2:
      {
        printf("the morse code representation is: %s\n", two);
      }
      break;

    case 3:
      {
        printf("the morse code representation is: %s\n", three);
      }
      break;

    case 4:
      {
        printf("the morse code representation is: %s\n", four);
      }
      break;

    case 5:
      {
        printf("the morse code representation is: %s\n", five);
      }
      break;

    case 6:
      {
        printf("the morse code representation is: %s\n", six);
      }
      break;

    case 7:
      {
        printf("the morse code representation is: %s\n", seven);
      }
      break;

    case 8:
      {
        printf("the morse code representation is: %s\n", eight);
      }
      break;

    case 9:
      {
        printf("the morse code representation is: %s\n", nine);
      }
      break;

    default:
      {
        return;
      }
  }
}



int main ()
{
    char user_in[1];
  while(1)
  {
    printf("enter a value 0-9:\n");
    fgets( user_in,5,stdin);
    printf("user entered: %s",user_in);
    if(strcmp(user_in, "0\n")==0)
    {
      morse_decode(0);
    }
    if(strcmp(user_in, "q\n")==0)
    {
      break;
    }
    int i=0;
    for(i=1; i<10; i++)
    {
      if(atoi(user_in)==i)
      {
      morse_decode(atoi(user_in));
      break;
      }
    }
  }
  return 0;
}
