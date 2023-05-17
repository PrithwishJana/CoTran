var n = int ( input ( ) );
var t = { 0 } + list ( map ( int , input ( ) . split ( ) ) );
a = { 0 } + list ( map ( int , input ( ) . split ( ) ) );
ans , cnt = {} , { 0 for i in range ( n + 1 ) };
for (int i = 0; i < a.length; i++){
    cnt { i } += 1;
}
for i in range ( 1 , n + 1 ) :
    if (t { i } == 1) {
        crt = { i };
        var x = a { i };
        while (cnt { x } == 1) {
            crt . append ( x );
            x = a { x };
        }
         if (len ( crt ) > len ( ans )) {
            var ans = crt { : };
         }
     }
 ans . reverse ( );
System.out.println ( len ( ans ) );
System.out.println ( ' ' . join ( map ( str , ans ) ) );
