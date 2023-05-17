public void leftRotate ( arr , n , k ) {
    for i in range ( k , k + n ) :
        System.out.println ( str ( arr { i % n } ) , var end = " " );
}
var arr = { 1 , 3 , 5 , 7 , 9 };
var n = len ( arr );
var k = 2 ;;
leftRotate ( arr , n , k );
System.out.println ( );
k = 3 ;;
leftRotate ( arr , n , k );
System.out.println ( );
k = 4;
leftRotate ( arr , n , k );
System.out.println ( );
