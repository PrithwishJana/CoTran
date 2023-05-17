while (true) {
    T , D , var L = map ( int , input ( ) . split ( ) );
    if var T == 0 : break;
    var a = {};
    for i in range ( T ) :
        var x = int ( input ( ) );
        if x >= L : a . append ( i );
    T , ans = T - 1 , 0;
    for i in range ( 1 , len ( a ) ) :
        x = D;
        if T - a { i - 1 } < D : x = T - a { i - 1 };
        if a { i } - a { i - 1 } < x : ans += a { i } - a { i - 1 };
        else : ans += x;
    if a : ans += T - a { - 1 } if a { - 1 } + D > T else D;
    System.out.println ( ans );
}
 