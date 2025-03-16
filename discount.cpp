#include<iostream.h>
using namespace std;
int main(){
  float amount;
  cout<<"Enter the Bill Amount"<<endl;
  cint>>amount;
  float discount=0.0;
  if(amount>=100 && amount<500){
    discount=amount-(amount*0.1);
  }
  else if(amount>=500){
    discount=amount-(amount*0.2);
  }
  cout<<"Bill Amount is: "<<amount<<endl;
  cout<<"Discounted Bill Amount is: "<<discount;
}

  
