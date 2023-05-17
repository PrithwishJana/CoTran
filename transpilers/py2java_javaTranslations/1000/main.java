var isPrime = { 1 } * 100005;
public void sieveOfEratostheneses ( ) {
    isPrime { 1 } = false;
    var i = 2;
    while (i * i < 100005) {
        if (( isPrime { i } )) {
            var j = 2 * i;
            while (j < 100005) {
                isPrime { j } = false;
                j += i;
            }
        }
          i += 1;
    }
     return;
}
public void findPrime ( n ) {
    var num = n + 1;
    while (( num )) {
        if (isPrime { num }) {
            return num;
        }
         num += 1;
    }
     return 0;
}
public void minNumber ( arr ) {
    sieveOfEratostheneses ( );
    s = 0;
    for i in range ( 0 , len ( arr ) ) :
        s += arr { i };
    if (isPrime { s } == true) {
        return 0;
    }
     num = findPrime ( s );
    return num - s;
}
var arr = { 2 , 4 , 6 , 8 , 12 };
System.out.println ( minNumber ( arr ) );
