import sys;
import math.*;
import bisect.*;
public void read_input ( var input_path = None ) {
    if (input_path is None) {
        f = sys . stdin;
    }
     else{
        f = open ( input_path , 'r' );
    }
    n , m , a , d = map ( int , f . readline ( ) . split ( ) );
    t = list ( map ( int , f . readline ( ) . split ( ) ) );
    return n , m , a , d , t;
}
public void sol ( n1 , m , a , d , t ) {
    insort ( t , a * n1 );
    pred = 0;
    k = 0;
    n = 0;
    step = d // a + 1;
    answer = 0;
    fl = 0;
    for (int i = 0; i < t.length; i++){
        if (i > pred) {
            if (fl == 0) {
                n = ( i - pred + ( pred % a ) ) // a;
                if (n != 0) {
                    k += ( n // step ) * step - step * ( n % step == 0 ) + 1;
                    if (k > n1) {
                        k = n1;
                        fl = 1;
                    }
                 }
                 if (( k * a + d >= i ) and ( n != 0 )) {
                    pred = k * a + d;
                }
                 else{
                    pred = i + d;
                    k = floor ( pred // a );
                    answer += 1;
                }
                k = min ( floor ( pred // a ) , n1 );
                answer += n // step + ( n % step != 0 );
            }
             else{
                answer += 1;
                pred = i + d;
            }
        }
         if (i == a * n1) {
            fl = 1;
        }
    }
     return { f"{answer}" };
}
public void solve ( input_path = None ) {
    return sol ( * read_input ( input_path ) );
}
public void main ( ) {
    for line in sol ( * read_input ( ) ) :
        System.out.println ( f"{line}" );
}
if (var __name__ == '__main__') {
    main ( );
}
 