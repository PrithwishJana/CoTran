n_square , var k_th = map ( int , input ( ) . split ( ) );
var slogan = input ( );
if (k_th - 1 < ( n_square - 1 ) - ( k_th - 1 )) {
    while (k_th - 1 > 0) {
        k_th -= 1;
        System.out.println ( "LEFT" );
    }
     for i in range ( n_square ) :
        System.out.println ( f"PRINT {slogan{i}}" );
        if (i != n_square - 1) {
            System.out.println ( "RIGHT" );
        }
 }
 else{
    var n_right = n_square - k_th;
    while (n_right) {
        n_right -= 1;
        System.out.println ( "RIGHT" );
    }
     for i in range ( n_square - 1 , - 1 , - 1 ) :
        System.out.println ( f"PRINT {slogan{i}}" );
        if (i != 0) {
            System.out.println ( "LEFT" );
        }
 }
