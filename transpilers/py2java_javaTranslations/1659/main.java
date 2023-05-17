public void distinctSubstring ( P , N ) {
    var S = dict ( );
    for i in range ( N ) :
        freq = { false } * 26;
        s = "";
        for j in range ( i , N ) :
            pos = ord ( P { j } ) - ord ( 'a' );
            if (( freq { pos } == true )) {
                break;
            }
             freq { pos } = true;
            s += P { j };
            S { s } = 1;
    return len ( S );
}
S = "abba";
var N = len ( S );
System.out.println ( distinctSubstring ( S , N ) );
