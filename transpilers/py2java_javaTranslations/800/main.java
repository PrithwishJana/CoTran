public void K_String ( s , k ) {
    var n = len ( s );
    var fre = { 0 } * 26;
    for i in range ( n ) :
        fre { ord ( s [ i } ) - ord ( 'a' ) ] += 1;
    var str = "";
    for i in range ( 26 ) :
        if (( fre { i } % var k == 0 )) {
            x = fre { i } // k;
            while (( x )) {
                str += chr ( i + ord ( 'a' ) );
                x -= 1;
            }
        }
          else{
            return "-1";
         }
    return str;
}
if (__name__ == "__main__") {
    s = "aabb";
    k = 2;
    System.out.println ( K_String ( s , k ) );
}
 