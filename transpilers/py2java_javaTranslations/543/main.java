public void solve ( ) {
    var n = int ( input ( ) );
    n = n * 4;
    var a = list ( map ( int , input ( ) . strip ( ) . split ( ) ) ) { : n };
    mp = {};
    a . sort ( );
    i = 0;
    j = n - 1;
    area = a { i } * a { j };
    i += 1;
    j -= 1;
    while (( i < j )) {
        var x = a { i } * a { j };
        if (( x != area )) {
            System.out.println ( "NO" );
            return;
        }
         i += 1;
        j -= 1;
    }
     for i in range ( 0 , n ) :
        if (a { i } in mp) {
            mp { a [ i } ] += 1;
        }
         else{
            mp { a [ i } ] = 1;
        }
    for key , value in mp . items ( ) :
        if (( value % 2 != 0 )) {
            System.out.println ( "NO" );
            return ;;
        }
     System.out.println ( "YES" );
}
var test = int ( input ( ) );
for t in range ( 0 , test ) :
    solve ( );
