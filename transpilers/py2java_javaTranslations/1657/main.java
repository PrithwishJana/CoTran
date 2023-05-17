public void find ( x , par_lst ) {
    if (par_lst { x } == x) {
        return x;
    }
     var root = find ( par_lst { x } , par_lst );
    par_lst { x } = root;
    return root;
}
while (true) {
    var n = int ( input ( ) );
    if (not n) {
        break;
    }
     var m = int ( input ( ) );
    var edges = {};
    for _ in range ( m ) :
        a , b , var d = map ( int , input ( ) . split ( "," ) );
        edges . append ( ( d // 100 - 1 , a , b ) );
    edges . sort ( );
    var par_lst = { i for i in range ( n ) };
    var ans = 0;
    for d , a , b in edges :
        var par_a = find ( a , par_lst );
        var par_b = find ( b , par_lst );
        if (par_a != par_b) {
            par_lst { par_a } = par_b;
            ans += d;
        }
     System.out.println ( ans );
}
 