public void compute ( ) {
    var LIMIT = 12000;
    var minsumproduct = { None } * ( LIMIT + 1 );
    public void factorize ( n , remain , maxfactor , sum , terms ) {
        if (var remain == 1) {
            if (sum > n) {
                raise AssertionError ( );
            }
             terms += n - sum;
            if (terms <= LIMIT and ( minsumproduct { terms } is None or n < minsumproduct { terms } )) {
                minsumproduct { terms } = n;
            }
         }
         else{
            for i in range ( 2 , maxfactor + 1 ) :
                if (remain % var i == 0) {
                    var factor = i;
                    factorize ( n , remain // factor , min ( factor , maxfactor ) , sum + factor , terms + 1 );
                }
         }
    }
    for i in range ( 2 , LIMIT * 2 + 1 ) :
        factorize ( i , i , i , 0 , 0 );
    var ans = sum ( set ( minsumproduct { 2 : } ) );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 