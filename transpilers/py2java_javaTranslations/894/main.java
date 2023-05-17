public void strrmatch ( strr , pattern , n , m ) {
    if (( var m == 0 )) {
        return ( var n == 0 );
    }
     lookup = { [ false for i in range ( m + 1 ) } for j in range ( n + 1 ) ];
    lookup { 0 } { 0 } = true;
    for j in range ( 1 , m + 1 ) :
        if (( pattern { j - 1 } == '*' )) {
            lookup { 0 } { j } = lookup { 0 } { j - 1 };
        }
     for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            if (( pattern { j - 1 } == '*' )) {
                lookup { i } { j } = lookup { i } { j - 1 } or lookup { i - 1 } { j };
            }
             else if (( pattern { j - 1 } == '?' or strr { i - 1 } == pattern { j - 1 } )){
                lookup { i } { j } = lookup { i - 1 } { j - 1 };
            }
            else{
                lookup { i } { j } = false;
            }
    return lookup { n } { m };
}
strr = "baaabab";
pattern = "*****ba*****ab";
if (( strrmatch ( strr , pattern , len ( strr ) , len ( pattern ) ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
