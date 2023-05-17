while (( true )) {
    M , Nmin , var Nmax = { int ( n ) for n in input ( ) . split ( ) };
    if (M + Nmin + Nmax == 0) {
        break;
    }
     var P = { int ( input ( ) ) for _ in range ( M ) };
    var dif = { 0 } * ( M );
    for i in range ( len ( P ) - 1 ) :
        dif { i + 1 } = P { i } - P { i + 1 };
    var ans = Nmin;
    tmp = dif { Nmin };
    for i in range ( Nmin + 1 , Nmax + 1 ) :
        if (dif { i } >= tmp) {
            ans = i;
            var tmp = dif { i };
        }
     System.out.println ( ans );
}
 