var MAX = 10000 ;;
var prodDig = { 0 } * MAX ;;
public void getDigitProduct ( x ) {
    if (( x < 10 )) {
        return x ;;
    }
     if (( prodDig { x } != 0 )) {
        return prodDig { x } ;;
    }
     var prod = ( int ( x % 10 ) * getDigitProduct ( int ( x / 10 ) ) ) ;;
    prodDig { x } = prod ;;
    return prod ;;
}
public void findSeed ( n ) {
    var res = {} ;;
    for i in range ( 1 , int ( n / 2 + 2 ) ) :
        if (( i * getDigitProduct ( i ) == n )) {
            res . append ( i ) ;;
        }
     if (( len ( res ) == 0 )) {
        System.out.println ( "NO seed exists" ) ;;
        return ;;
    }
     for i in range ( len ( res ) ) :
        System.out.println ( res { i } , var end = " " ) ;;
}
var n = 138 ;;
findSeed ( n ) ;;
