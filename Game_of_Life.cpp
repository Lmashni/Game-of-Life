#include <stdio.h>
#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;
using namespace std::chrono;

void nn(int* pxi , int* pni , int d){
  int d2 = d*d;
 for(int i=0 ; i < d2 ; i++){

      *(pni ) = *(pxi  - 1) + *(pxi + 1)
		+ *(pxi + d- 1) + *(pxi + d) + *(pxi+d + 1)
		+ *(pxi -d - 1) + *(pxi -d) + *(pxi-d + 1);
		pxi++;
		pni++;	}
					}

void nnb(int* px , int* pn , int d){
  int d2 = d*d;
 for(int i=0 ; i < d2 ; i++){

      *(pn+i%d2 ) = *(px+(i  - 1)%d2) + *(px+(i + 1)%d2)
		+ *(px+(i + d- 1)%d2) + *(px+(i + d)%d2) + *(px+(i+d + 1)%d2)
		+ *(px+(i -d - 1)%d2) + *(px+(i -d)%d2) + *(px+(i-d + 1)%d2);
		
			}
					}

void imgp(int* pxi  , int d){
	int d2 =d *d;	
	for(int i=0; i < d2 ; i++){
		if(i%d ==0 ){
			if(*(pxi+i) ==0){cout << "." << endl;}
			else{cout << "O" << endl;}
				}
		else{if(*(pxi+i) ==0){cout << ".";}
			else{cout << "O";}}
				    }
			   
		cout << "dis" << endl;			}

void img(int* pxi  , int d){
	int d2 =d *d;	
	for(int i=0; i < d2 ; i++){
		if(i%d ==0 ){cout << *(pxi+i) << endl; }
		else{cout << *(pxi+i);}
				    }
			   
		cout << "dis" << endl;			}

void swt(int* pxi , int* pni , int d){
	int d2 = d*d;
	for(int i=0; i < d2 ; i++){
		if(*pni != 2){
                	if(*pni ==3){*pxi=1;}
			else{*pxi = 0;}
				}
		pxi++; pni++;		    }
	
					}


void ins(int* pxi , int* pyi , int d, int l){
	int d2 = d*d;
	int l2 = l*l;
        pyi += l2 /2 - d2/2;
	for(int i=0; i < d2 ; i++){
		if(i % d == 0){pyi = pyi + l -d;}
		*pyi = *pxi;
		pyi++;pxi++;
		
				   }

					       }

void zeros(int* pxi  , int d){
	int d2 = d*d;
	for(int i=0; i < d2 ; i++){*pxi = 0;pxi++;}
				}

int main(){ 

int l = 64;
int l2 = l*l;

int y[l2];

zeros(&y[0],l);

int d = 12;
int d2 = d*d;

int x[d2] = {0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,1,0,0,0,0,0,0,0,
	     0,0,0,1,1,1,0,0,0,0,0,0,
	     0,0,0,0,0,1,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,};
/*
int x[d2] = {0,0,0,0,0,1,0,0,0,0,0,0,
	     0,0,0,0,1,1,1,0,0,0,0,0,
	     0,0,0,1,1,1,1,1,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,0,0,0,0,0,0,0,0,0,
	     0,0,0,1,1,1,1,1,0,0,0,0,
	     0,0,0,0,1,1,1,0,0,0,0,0,
	     0,0,0,0,0,1,0,0,0,0,0,0,};
*/
int n[l2];

//img(&y[0], l);

ins(&x[0],&y[0],d,l);

int T = 1000;
//nn(&x[0],&n[0],d);
auto start = high_resolution_clock::now(); 
for(int i=0; i < T ; i++){ 

	nnb(&y[0],&n[0],l);
	swt(&y[0],&n[0],l);
	imgp(&y[0], l);
	struct timespec ts = {0, 100000000L };

	nanosleep (&ts, NULL);

	system("clear");

 			     }
auto stop = high_resolution_clock::now();
auto duration = duration_cast<milliseconds>(stop - start);
cout << duration.count() << endl;
//imgp(&x[0], d);
  return 0;
}

