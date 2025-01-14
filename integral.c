# include <math.h>
# include <stdio.h>


int main() {
    const double a = 3.14159;
    const int n = 10; 
    const double dx= a/(double)n ; 
    double integral= 0.0 ; 

    for (int i=0; i < n; i++) {
    const double xip12 = dx*((double)i+0.5) ;
    const double dI=fabs(sin(xip12)) * dx ;
    integral += dI ;
    }
    printf("Integral result: %.10f\n", integral);
    return 0;
}