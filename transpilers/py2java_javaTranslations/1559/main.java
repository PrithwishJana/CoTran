public void isHeterogram ( s , n ) {
    var hash = { 0 } * 26;
    for i in range ( n ) :
        if (s { i } != ' ') {
            if (hash { ord ( s [ i } ) - ord ( 'a' ) ] == 0) {
                hash { ord ( s [ i } ) - ord ( 'a' ) ] = 1;
            }
             else{
                return false;
            }
        }
     return true;
}
var s = "the big dwarf only jumps";
var n = len ( s );
System.out.println ( "YES" if isHeterogram ( s , n ) else "NO" );
