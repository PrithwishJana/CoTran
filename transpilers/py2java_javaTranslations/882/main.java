var N = int ( input ( ) );
var A = list ( map ( int , input ( ) . split ( ) ) );
var C = { 0 } * ( 10 ** 5 );
for (int ai = 0; ai < A.length; ai++){
    C { ai } += 1;
}
var ans = 0;
for i in range ( 10 ** 5 - 2 ) :
    ans = max ( C { i } + C { i + 1 } + C { i + 2 } , ans );
System.out.println ( ans );
