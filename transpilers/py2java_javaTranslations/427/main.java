var i = 0;
var sumsell = 0;
var sumn = 0;
while (true) {
    try{
        at , var n = map ( int , input ( ) . split ( "," ) );
        sumsell += at * n;
        sumn += n;
        i += 1;
    }
    except EOFError : break;
}
 System.out.println ( sumsell );
System.out.println ( ( int ) ( sumn / i + 0.5 ) );
