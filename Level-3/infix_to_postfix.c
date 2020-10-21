/*
 * Date: 2020-10-21
 *
 * Description:
 * Convert Infix expression into postfix.
 *
 * Approach:
 * INFIX -> Input String.
 * S -> Stack of characters.
 * R_POLISH -> output String.
 * next -> iterator for INFIX
 * 
 * 1. PUSH "(" into the S and concat ")" into INFIX
 * 2. Until precedence of next is less then top of S POP elements from the stack
 *    and concat in R_POLISH.
 * 3. If next and top of the S are not same then PUSH next into S.
 * 
 * 
 * Complexity:
 * Time - O(n^2), space: O(n)
 * 
 * Precedence Table:
*      |    Symbol    | Input precedence  |  Stack precedence |  Rank  | 
*      |     +,-      |         1         |         2         |   -1   |
*      |     *,/      |         3         |         4         |   -1   |
*      |      ^       |         6         |         5         |   -1   |
*      |  Alphabets   |         7         |         8         |    1   |
*      |      (       |         9         |         0         |    -   |
*      |      )       |         0         |         -         |    -   |
 */


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>



// precedence of alphabets in input String and stack
#define INPUTALPHA 7
#define STACKALPHA 8

#define RANKALPHA 1
typedef struct PrecedenceTable
{
    char symbol;
    int precedence;
    int Rank;
} PrecedenceTable;

// IF operators are in input string then we are using this TABLE
PrecedenceTable INFIXOperators[] = {{'+' , 1, -1},
                         {'-' , 1, -1},
                         {'*' , 3, -1},
                         {'/' , 3, -1}, 
                         {'^' , 5, -1}, 
                         {'(' , 9},    //  Prenthesis doesn't have Rank 
                         {')' , 0}};

// IF operators are in STACK then we are using this TABLE
PrecedenceTable STACKOperators[] = {{'+' , 2, -1}, 
                         {'-' , 2, -1}, 
                         {'*' , 4, -1}, 
                         {'/' , 4, -1}, 
                         {'^' , 6, -1}, 
                         {'(' , 0},      //  Prenthesis doesn't have Rank
                         {')' , 0}};

int findrank(char a)
{
    for (int i = 0; i < 6; i++)
    {
        if (a == INFIXOperators[i].symbol)
            return INFIXOperators[i].Rank;
    }

    return RANKALPHA;
}

int isHigher(char input, char stack)
{
    int inputPrec=0, stackPrec=0;

    if(isalpha(input))
        inputPrec = INPUTALPHA;
    
    if(isalpha(stack))
        stackPrec = STACKALPHA;
    

    if(inputPrec != INPUTALPHA)
    {
        for (int i = 0; i < 7; i++)
        {
            if (input == INFIXOperators[i].symbol)
                inputPrec = INFIXOperators[i].precedence;
        }
    }

    if(stackPrec != STACKALPHA)
    {
        for (int i = 0; i < 7; i++)
        {
            if (stack == STACKOperators[i].symbol)
                stackPrec = STACKOperators[i].precedence;
        }
    }

    if (inputPrec < stackPrec)
    {
        return 1;
    }
    else if (inputPrec == stackPrec)
        return 0;
    else
        return -1;
}
typedef struct STACK
{
    char *data;
    int top;
} STACK;

void PUSH(STACK *s, char symbol)
{

    s->data = (char *)realloc(s->data, sizeof(char) * (s->top + 1));
    s->data[s->top] = symbol;
    s->top++;
}
char POP(STACK *s)
{
    char temp = s->data[s->top - 1];
    s->data[s->top - 1] = '\0';
    s->top--;
    return temp;
}

int main()
{
    char *INFIX, *R_POLISH, next;
    int  length = 0, RANK = 0, i = 0;
    STACK S;

    INFIX = (char *)malloc(sizeof(char) * 100);
    R_POLISH = (char *)malloc(sizeof(char) * 100);

    R_POLISH[length] = '\0';

    S.top = 0;
    S.data = NULL;
    PUSH(&S, '(');

    scanf("%s", INFIX);
    strcat(INFIX,")");

    i = 0;
    length = 0;
    next = INFIX[i++];

    while (next != '\0')
    {
        if (S.top < 1)
        {
            printf("INVALID INFIX EXPRESSION");
            exit(0);
        }

        while (isHigher(next, S.data[S.top - 1]) == 1)
        {
            char temp = POP(&S);
            R_POLISH[length++] = temp;

            RANK += findrank(temp);
            if (RANK < 1)
            {
                printf("INVALID INFIX EXPRESSION");
                exit(0);
            }
        }

        if (isHigher(next, S.data[S.top - 1]) != 0)
        {
            PUSH(&S, next);
        }
        else
            POP(&S);
        next = INFIX[i++];
    }

    R_POLISH[length] = '\0';
    puts(R_POLISH);
}
