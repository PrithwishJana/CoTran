public void nextZero ( i , occurrences ) {
    while (i < 26) {
        if (occurrences { i } == 0) {
            return i;
        }
         i += 1;
    }
     return - 1;
}
public void getModifiedString ( str ) {
    var n = len ( str );
    if (n > 26) {
        return "-1";
    }
     var ch = str;
    ch = list ( ch );
    occurrences = { 0 } * 26;
    for i in range ( n ) :
        occurrences { ord ( ch [ i } ) - ord ( 'a' ) ] += 1;
    index = nextZero ( 0 , occurrences );
    for i in range ( n ) :
        if (occurrences { ord ( ch [ i } ) - ord ( 'a' ) ] > 1) {
            occurrences { ord ( ch [ i } ) - ord ( 'a' ) ] -= 1;
            ch { i } = chr ( ord ( 'a' ) + index );
            occurrences { index } = 1;
            index = nextZero ( index + 1 , occurrences );
        }
     ch = '' . join ( ch );
    System.out.println ( ch );
}
if (var __name__ == "__main__") {
    var str = "geeksforgeeks";
    getModifiedString ( str );
}
 