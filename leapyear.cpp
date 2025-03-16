#include<iostream>
using namespace std;
int main(){
  int year;
  cout<<"Enter the year:";
  cin>>year;
  bool leap=false;
  if(year%100==0){
    if(year%400==0){
      leap=true;
    }
  }
  else{
    if(year%4==0){
      leap=true;
    }
  }
  leap?cout<<year<<" is a leap year";:cout<<year<<" is not a leap year";
  return 0;
}

    
