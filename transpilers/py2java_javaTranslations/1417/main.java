public void distinctSubstring ( P , Q , K , N ) {
    var S = set ( );
    for i in range ( 0 , N ) :
        var sum = 0 ;;
        s = '';
        for j in range ( i , N ) :
            pos = ord ( P { j } ) - 97;
            sum = sum + ord ( Q { pos } ) - 48;
            s += P { j };
            if (( sum <= K )) {
                S . add ( s );
            }
             else{
                break;
            }
    return len ( S );
}
var P = "abcde";
var Q = "12345678912345678912345678";
var K = 5;
var N = len ( P );
System.out.println ( distinctSubstring ( P , Q , K , N ) );
