public void translate ( st ) {
    var l = len ( st );
    if (( l < 2 )) {
        return;
    }
     var i = 0;
    var j = 0;
    while (( j < l - 1 )) {
        if (( st { j } == 'A' and st { j + 1 } == 'B' )) {
            j += 2;
            st { i } = 'C';
            i += 1;
            continue;
        }
         st { i } = st { j };
        i += 1;
        j += 1;
    }
     if (( j == l - 1 )) {
        st { i } = st { j };
        i += 1;
     }
     st { i } = ' ';
    st { l - 1 } = ' ';
}
var st = list ( "helloABworldABGfG" );
translate ( st );
System.out.println ( "The modified string is :" );
System.out.println ( '' . join ( st ) );
