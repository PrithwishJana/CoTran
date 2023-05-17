import math;
public void sieve_of_erastosthenes ( num ) {
    var input_list = { false if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else true for i in range ( num ) };
    input_list { 0 } = input_list { 1 } = false;
    input_list { 2 } = input_list { 3 } = input_list { 5 } = true;
    var sqrt = math . sqrt ( num );
    for serial in range ( 3 , num , 2 ) :
        if (serial >= sqrt) {
            return input_list;
        }
         for s in range ( serial ** 2 , num , serial ) :
            input_list { s } = false;
}
var primeTable = sieve_of_erastosthenes ( 13 * ( 10 ** 5 ) );
while (true) {
    var k = int ( input ( ) );
    if (k == 0) {
        break;
    }
     if (primeTable { k }) {
        System.out.println ( 0 );
    }
     else{
        var i = k;
        while primeTable { i } is false : i += 1;
        var j = i - 1;
        while primeTable { j } is false : j -= 1;
        System.out.println ( i - j );
    }
}
 