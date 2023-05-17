public void f ( n , s1 , s2 ) {
    for i in range ( n ) :
        if (( s1 { i } != s2 { i } )) {
            if (( s1 { i } == 'R' or s2 { i } == 'R' )) {
                return "NO";
            }
         }
     return "YES";
}
var t = int ( input ( ) );
for i in range ( t ) :
    var n = int ( input ( ) );
    var s1 = input ( );
    var s2 = input ( );
    System.out.println ( f ( n , s1 , s2 ) );
