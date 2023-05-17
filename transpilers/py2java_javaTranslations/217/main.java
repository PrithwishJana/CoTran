public void addToArrayForm ( A , K ) {
    v , var ans = {} , {};
    rem , i = 0 , 0;
    for i in range ( len ( A ) - 1 , - 1 , - 1 ) :
        my = A { i } + ( K % 10 ) + rem;
        if (my > 9) {
            rem = 1;
            v . append ( my % 10 );
        }
         else{
            v . append ( my );
            rem = 0;
        }
        K = K // 10;
    while (K > 0) {
        my = ( K % 10 ) + rem;
        v . append ( my % 10 );
        if (my // 10 > 0) {
            rem = 1;
        }
         else{
            rem = 0;
        }
        K = K // 10;
    }
     if (rem > 0) {
        v . append ( rem );
     }
     for i in range ( len ( v ) - 1 , - 1 , - 1 ) :
        ans . append ( v { i } );
    return ans;
}
if (__name__ == "__main__") {
    A = { 2 , 7 , 4 };
    K = 181;
    ans = addToArrayForm ( A , K );
    for i in range ( 0 , len ( ans ) ) :
        System.out.println ( ans { i } , var end = "" );
}
 