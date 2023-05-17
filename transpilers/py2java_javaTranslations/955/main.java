public void makeAP ( arr , n ) {
    initial_term , var common_difference = 0 , 0;
    if (( n == 3 )) {
        common_difference = arr { 2 } - arr { 1 };
        initial_term = arr { 1 } - common_difference;
    }
     else if (( ( arr { 1 } - arr { 0 } ) == arr { 2 } - arr { 1 } )){
        initial_term = arr { 0 };
        common_difference = arr { 1 } - arr { 0 };
    }
    else if (( ( arr { 2 } - arr { 1 } ) == ( arr { 3 } - arr { 2 } ) )){
        common_difference = arr { 2 } - arr { 1 };
        initial_term = arr { 1 } - common_difference;
    }
    else{
        common_difference = ( arr { 3 } - arr { 0 } ) / 3;
        var initial_term = arr { 0 };
    }
    for i in range ( n ) :
        System.out.println ( int ( initial_term + ( i * common_difference ) ) , var end = " " );
    System.out.println ( );
}
var arr = { 1 , 3 , 7 };
var n = len ( arr );
makeAP ( arr , n );
