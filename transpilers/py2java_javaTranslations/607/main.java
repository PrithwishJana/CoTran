private void popcnt32 ( number ) {
    var counter = 0;
    while (( number > 0 )) {
        if (( number % 2 == 1 )) {
            counter = counter + 1;
        }
         var number = int ( number / 2 );
    }
     return counter;
}
public void maximize ( a ) {
    var n = _popcnt32 ( a );
    var res = 0;
    for i in range ( 1 , n + 1 ) :
        res = int ( res | ( 1 << ( 32 - i ) ) );
    return abs ( res );
}
var a = 1;
System.out.println ( maximize ( a ) );
