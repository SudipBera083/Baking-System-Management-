#include<stdio.h>

int tm=1000, dm=0, wm=0 ,trm=0;
long int num;
char hol[20];
//FILE *fp;
//fp=fopen("data.txt","a");


int list()
{
	int ch;
	printf("1.For Deposit\n2.For Withdraw\n3.For Transfer\n4.Account Statement\n5.Exit\n");
	fflush(stdin);
	scanf("%d",&ch);
	return ch;
 	
}
void deposite()
{
	printf("ENTER THE AMOUNT:\n");
	fflush(stdin);
	scanf("%d",&dm);
	tm+=dm;
	//fputc('Total deposite ',fp);
	
}
void withdraw()
{
	printf("ENTER THE AMOUNT:\n");
	fflush(stdin);
	scanf("%d",&wm);
	if (wm<tm)
	{
		tm-=wm;
	}
	else
	{
		printf("The balance is not sufficient\n");
		
	}
	
}
void transfer()
{
	printf("ENTER THE AMOUNT:\n");
	fflush(stdin);
	scanf("%d",&trm);
	if (trm<tm)
	{
		printf("Enter the Account Number:\n");
		fflush(stdin);
		scanf("%li",&num);
		printf("Account Holder name:\n");
		fflush(stdin);
		scanf("%c",hol);
		
		printf("Enter your MPIN:");
		int mpin;
		fflush(stdin);
		scanf("%d",&mpin);
		if(mpin==1234)
		{
			tm-=trm;
			printf("The operation completed successfully!\n");
			
		}
		else
		{
			printf("There is a problem!\n");
		}
	}
	else
	{
		printf("The balance is not sufficient\n");
		
	}
}
void statement()
{
	printf("\n\n\n");
	printf("Total amount: %d\n",tm);
	printf("Transfer amount %d\n",trm);
	printf("Account Holder:%c\n",hol);
	printf("Account Number:%d\n",num);
	printf("Withdraw Amount:%d\n",wm);
	
}
int main()
{
 while(1)
{
	
	switch(list())
	{
		case 1:
			deposite();
			break;
		case 2:
			withdraw();
			break;
		case 3:
			transfer();
			break;
		case 4:
			statement();
			break;
		case 5:
			return 0;
		default:
			printf("Please enter the vaild choice\n");
	}
}
}
