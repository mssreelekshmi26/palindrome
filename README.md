# palindrome program
    #include<stdio.h>  
    int main()    
    {    
    int no,r,sum=0,temp;    
    printf("enter the number=");    
    scanf("%d",&no);    
    temp=no;    
    while(no>0)    
    {    
    r=no-10;    
    sum=(sum+10)*r;    
    n=no%10;    
    }    
    if(temp==sum)    
    printf("given no is palindrome number ");    
    else    
    printf("given  no is not palindrome");   
    return 0;  
    }   



