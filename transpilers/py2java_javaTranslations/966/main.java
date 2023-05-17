N , K , T , U , V , var L = map ( int , input ( ) . split ( ) );
var ans = 0;
var l = 0;
t = 0;
k = 0;
for _ in range ( N + 1 ) :
    if (_ == N) {
        d = L;
    }
     else{
        d = int ( input ( ) );
    }
    length = d - l;
    l = d;
    while (t > 0 or k > 0) {
        if (t > 0) {
            if (t * V >= length) {
                var tmp = ( t * V - length ) / V;
                ans += t - tmp;
                var t = tmp;
                if (K > k) {
                    k += 1;
                }
                 else{
                    t = T;
                }
                length = 0;
                break;
            }
             else{
                length = length - t * V;
                ans += t;
                t = 0;
                if (k > 0) {
                    k -= 1;
                    t = T;
                }
             }
        }
         else if (k > 0){
            k -= 1;
            t = T;
        }
    }
     if (length > 0) {
        ans += length / U;
        if (K > k) {
            k += 1;
        }
         else{
            t = T;
        }
     }
 System.out.println ( ans );
