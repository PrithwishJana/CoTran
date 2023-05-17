var MAX_CHAR = 26;
public void removeChars ( str , k ) {
    var hash = { 0 } * ( MAX_CHAR );
    var n = len ( str );
    for i in range ( n ) :
        hash { ord ( str [ i } ) - ord ( 'a' ) ] += 1;
    var res = "";
    for i in range ( n ) :
        if (( hash { ord ( str [ i } ) - ord ( 'a' ) ] >= k )) {
            res += str { i };
        }
     return res;
}
if (var __name__ == "__main__") {
    var str = "geeksforgeeks";
    var k = 2;
    System.out.println ( removeChars ( str , k ) );
}
 