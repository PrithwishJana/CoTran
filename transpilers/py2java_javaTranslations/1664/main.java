public void f ( a ) {
    for x in { 'b' , 'w' } :
        if a { 0 : : 4 } . count ( x ) == 3 or a { 2 : 7 : 2 } . count ( x ) == 3 : return x;
        for i in range ( 3 ) :
            if a { i * 3 : i * 3 + 3 } . count ( x ) == 3 or a { i : : 3 } . count ( x ) == 3 : return x;
    return 'NA';
}
while (1) {
    var a = list ( input ( ) );
    if len ( a ) == 1 : break;
    a += list ( input ( ) ) + list ( input ( ) );
    System.out.println ( f ( a ) );
}
 