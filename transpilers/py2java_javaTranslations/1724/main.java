public void isVowel ( c ) {
    if (( var c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' )) {
        return true;
    }
     return false;
}
public void isVowelPrime ( Str , n ) {
    var prime = { true for i in range ( n ) };
    prime { 0 } = false;
    prime { 1 } = false;
    for p in range ( 2 , n ) :
        if (p * p > n) {
            break;
        }
         if (( prime { p } == true )) {
            for i in range ( 2 * p , n , p ) :
                prime { i } = false;
        }
     for i in range ( n ) :
        if (( isVowel ( Str { i } ) and prime { i } == false )) {
            return false;
        }
     return true;
}
var Str = "geeksforgeeks" ;;
var n = len ( Str );
if (( isVowelPrime ( Str , n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
