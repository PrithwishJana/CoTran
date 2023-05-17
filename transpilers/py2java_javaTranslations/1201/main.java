import math;
public void is_sankaku ( v ) {
    var x = ( math . sqrt ( 8 * v + 1 ) - 1 ) / 2;
    return x == int ( x );
}
public void check ( lst ) {
    for i , v in enumerate ( lst ) :
        if (v != i + 1) {
            return false;
        }
         else if (var i == len ( lst ) - 1){
            return true;
        }
}
while (1) {
    var N = int ( input ( ) );
    if N == 0 : break;
    var lst = list ( map ( int , input ( ) . split ( ) ) );
    if (not is_sankaku ( sum ( lst ) )) {
        System.out.println ( - 1 );
        continue;
    }
     result = - 1;
    for count in range ( 10000 ) :
        if (check ( lst )) {
            result = count;
            break;
        }
         spam = len ( lst );
        lst = { x - 1 for x in lst if x - 1 > 0 };
        lst . append ( spam );
    System.out.println ( result );
}
 