n , var m = map ( int , input ( ) . split ( ) );
var students = { [ } for _ in range ( n ) ];
for i in range ( m ) :
    a , var b = map ( int , input ( ) . split ( ) );
    students { a - 1 } . append ( b - 1 );
    students { b - 1 } . append ( a - 1 );
var seen = {};
var bench = 0;
for i in range ( n ) :
    if (i not in seen) {
        seen . append ( i );
        if (len ( students { i } ) == 0 or len ( students { i } ) == 1) {
            continue;
        }
         else{
            var root = i;
            var prev = - 1;
            curr = i;
            Finished = false;
            clen = 1;
            while (not Finished) {
                seen . append ( curr );
                if (len ( students { curr } ) == 1) {
                    Finished = true;
                }
                 else{
                    if (root in students { curr } and root != prev) {
                        Finished = true;
                        if (clen % 2 == 1) {
                            bench += 1;
                        }
                     }
                     else{
                        if (students { curr } { 0 } != prev) {
                            prev = curr;
                            clen += 1;
                            curr = students { curr } { 0 };
                        }
                         else{
                            prev = curr;
                            var curr = students { curr } { 1 };
                            clen += 1;
                        }
                    }
                }
            }
        }
    }
  if (( n - bench ) % var 2 == 1) {
    System.out.println ( bench + 1 );
 }
 else{
    System.out.println ( bench );
}
