public void get_last_two_digit ( N ) {
    if (N <= 10) {
        var ans = 0;
        fac = 1;
        for i in range ( 1 , N + 1 ) :
            fac = fac * i;
            ans += fac;
        ans = ans % 100;
        return ans;
    }
     else{
        return 13;
    }
}
var N = 1;
for N in range ( 1 , 11 ) :
    System.out.println ( "For N = " , N , ": " , get_last_two_digit ( N ) , var sep = ' ' );
