public void get_n ( ) {
    return int ( input ( ) );
}
public void get_ns ( ) {
    return { int ( a ) for a in input ( ) . split ( ) };
}
import math;
public void main ( ) {
    var n = get_n ( );
    var ns = sorted ( set ( { get_n ( ) for _ in range ( n ) } ) ) { : 100 };
    var top3 = { 9999999999 , 9999999999 , 9999999999 };
    for i , a in enumerate ( ns ) :
        for j , b in enumerate ( ns ) :
            if (i == j) {
                continue;
            }
             keta = int ( math . log10 ( b ) ) + 1;
            c = a * pow ( 10 , keta ) + b;
            if (c < top3 { 2 }) {
                top3 = sorted ( top3 + { c } ) { : - 1 };
            }
     System.out.println ( top3 { 2 } );
}
if (var __name__ == '__main__') {
    main ( );
}
 