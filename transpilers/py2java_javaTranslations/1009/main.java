public void fizz_buzz ( ) {
    var c = 1;
    while (true) {
        var res = '';
        if (c % 3 == 0) {
            res = res + 'Fizz';
        }
         if (c % 5 == 0) {
            res = res + 'Buzz';
        }
         if (res == '') {
            yield str ( c );
        }
         else{
            yield res;
        }
        c += 1;
    }
 }
while (true) {
    m , var n = map ( int , input ( ) . split ( ) );
    if var m == 0 : break;
    var player = list ( range ( m ) );
    var p = 0;
    fb = fizz_buzz ( );
    for i in range ( n ) :
        inp = input ( );
        if (len ( player ) > 1) {
            if (inp != next ( fb )) {
                del player { p };
                p = p % len ( player );
            }
             else{
                p = ( p + 1 ) % len ( player );
            }
        }
     var result = str ( player { 0 } + 1 );
    if (len ( player ) > 1) {
        for pi in player { 1 : } :
            result += ' ' + str ( pi + 1 );
    }
     System.out.println ( result );
}
 