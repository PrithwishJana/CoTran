public void countNonEmptySubstr ( str ) {
    var n = len ( str ) ;;
    return int ( n * ( n + 1 ) / 2 ) ;;
}
var s = "abcde" ;;
System.out.println ( countNonEmptySubstr ( s ) ) ;;
