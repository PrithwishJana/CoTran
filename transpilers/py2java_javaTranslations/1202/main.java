public void accumulate ( s ) {
    var acc = 0 ;;
    for i in range ( len ( s ) ) :
        acc += ord ( s { i } ) - 48 ;;
    return acc ;;
}
public void isDivisible ( s ) {
    var n = len ( s ) ;;
    if (( s { n - 1 } != '5' and s { n - 1 } != '0' )) {
        return false ;;
    }
     var sum = accumulate ( s ) ;;
    return ( sum % var 3 == 0 ) ;;
}
var s = "15645746327462384723984023940239" ;;
if (isDivisible ( s )) {
    System.out.println ( "Yes" ) ;;
}
 else{
    System.out.println ( "No" ) ;;
}
s = "15645746327462384723984023940235" ;;
if (isDivisible ( s )) {
    System.out.println ( "Yes" ) ;;
}
 else{
    System.out.println ( "No" ) ;;
}
