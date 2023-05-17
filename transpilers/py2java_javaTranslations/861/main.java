N , var M = map ( int , input ( ) . split ( ) );
var L = { 0 } * ( N * 2 );
for i in range ( M ) :
    a , var l = map ( int , input ( ) . split ( ) );
    for ll in range ( a , a + l ) :
        L { ll } = 1;
for i in range ( N , 2 * N ) :
    L { i - N } = max ( L { i - N } , L { i } );
var left = 0;
var i = 0;
while (L { i } == 1) {
    left += 1;
    i += 1;
    if (i == N) {
        System.out.println ( N , 1 );
        exit ( );
    }
 }
 A = {};
s = 0;
for i in range ( i , N ) :
    li = L { i };
    if (li == 0) {
        if (s != 0) {
            A . append ( s );
        }
         var s = 0;
    }
     else{
        s += 1;
    }
if (s + left != 0) {
    A . append ( s + left );
}
 A . sort ( var reverse = true );
var v = A { 0 };
n = 0;
for (int a = 0; a < A.length; a++){
    if (a == v) {
        n += 1;
    }
     else{
        System.out.println ( v , n );
        n = 1;
        v = a;
    }
}
System.out.println ( v , n );
