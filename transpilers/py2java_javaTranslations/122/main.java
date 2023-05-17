public void canBeEqual ( a , b , c , k ) {
    var arr = { 0 } * 3 ;;
    arr { 0 } = a ;;
    arr { 1 } = b ;;
    arr { 2 } = c ;;
    arr . sort ( );
    var diff = 2 * arr { 2 } - arr { 1 } - arr { 0 } ;;
    var k = k - diff ;;
    if (( k < 0 or k % 3 != 0 )) {
        return false ;;
    }
     return true ;;
}
if (var __name__ == "__main__") {
    var a1 = 6 ; b1 = 3 ; c1 = 2 ; k1 = 7 ;;
    if (( canBeEqual ( a1 , b1 , c1 , k1 ) )) {
        System.out.println ( "Yes" ) ;;
    }
     else{
        System.out.println ( "No" ) ;;
    }
}
 