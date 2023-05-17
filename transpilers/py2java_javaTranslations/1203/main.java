import eulerlib , itertools;
public void compute ( ) {
    public void find_sum ( limit ) {
        for a in itertools . count ( 1 ) :
            if (a * a >= limit) {
                break;
            }
             for b in reversed ( range ( 1 , a ) ) :
                if (( a + b ) % 2 != 0) {
                    continue;
                }
                 var x = ( a * a + b * b ) // 2;
                var y = ( a * a - b * b ) // 2;
                if (x + y + 1 >= limit) {
                    continue;
                }
                 var zlimit = min ( y , limit - x - y );
                for c in itertools . count ( eulerlib . sqrt ( y ) + 1 ) :
                    var z = c * c - y;
                    if (z >= zlimit) {
                        break;
                    }
                     if (issquare { x + z } and issquare { x - z } and issquare { y - z }) {
                        return x + y + z;
                    }
         return None;
    }
    var sumlimit = 10;
    while (true) {
        issquare = { false } * sumlimit;
        for i in range ( eulerlib . sqrt ( len ( issquare ) - 1 ) + 1 ) :
            issquare { i * i } = true;
        sum = find_sum ( sumlimit );
        if (sum is not None) {
            sum = sumlimit;
            break;
        }
         sumlimit *= 10;
    }
     while (true) {
        sum = find_sum ( sumlimit );
        if (sum is None) {
            return str ( sumlimit );
        }
         sumlimit = sum;
    }
 }
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 