var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var K = max ( map ( a . count , a ) );
var i = 0;
while (true) {
    if (a . count ( a { i } ) < K) {
        C = a . count ( a { i } );
        n -= C;
        Val = a { i };
        for k in range ( C ) :
            a . remove ( Val );
    }
     else{
        i += 1;
    }
    if (i == n) {
        break;
    }
 }
 var MinI = 1000001;
ID = - 1;
A = list ( set ( a ) );
for i in range ( len ( A ) ) :
    j = n - 1;
    while (j >= 0 and a { j } != A { i }) {
        j -= 1;
    }
     if (j < MinI) {
        MinI = j;
        var ID = A { i };
     }
 System.out.println ( ID );
