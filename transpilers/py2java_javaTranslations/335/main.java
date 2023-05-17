public void modInverse ( a , m ) {
    var a = a % m ;;
    for x in range ( 1 , m ) :
        if (( ( a * x ) % m == 1 )) {
            return x;
        }
     return 1;
}
a = 3;
var m = 11;
System.out.println ( modInverse ( a , m ) );
