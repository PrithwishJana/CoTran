try{
    N , var d = map ( int , input ( ) . split ( ) );
    var nums = list ( map ( int , input ( ) . split ( ) ) );
    nums . sort ( );
    var ans = 0;
    for i in range ( N ) :
        for j in range ( N - 1 , i - 1 , - 1 ) :
            if (abs ( nums { i } - nums { j } ) <= d) {
                ans = max ( ans , j - i + 1 );
                break;
            }
     System.out.println ( N - ans );
}
except Exception as e :
    System.out.println ( e );
