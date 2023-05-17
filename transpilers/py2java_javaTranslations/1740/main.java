public void binary_conversion ( s , m ) {
    while (( m )) {
        var temp = m % 2;
        s += str ( temp );
        var m = m // 2;
    }
     return s { : : - 1 };
}
public void find_character ( n , m , i ) {
    var s = "";
    s = binary_conversion ( s , m );
    s1 = "";
    for x in range ( n ) :
        for j in range ( len ( s ) ) :
            if (s { j } == "1") {
                s1 += "10";
            }
             else{
                s1 += "01";
            }
        s = s1;
        var s1 = "";
    var e = ord ( s { i } );
    var r = ord ( '0' );
    return e - r;
}
m , n , var i = 5 , 2 , 8;
System.out.println ( find_character ( n , m , i ) );
