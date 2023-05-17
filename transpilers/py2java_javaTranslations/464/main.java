var s = input ( );
var t = input ( );
var a = ord ( t { 0 } ) - ord ( s { 0 } );
var b = int ( t { 1 } ) - int ( s { 1 } );
var x = abs ( a );
var y = abs ( b );
c = { 'R' , 'U' , 'L' , 'D' };
i = 0;
j = 1;
if (a < 0) {
    i = 2;
}
 if (b < 0) {
    j = 3;
}
 k = j;
if (x > y) {
    k = i;
    x , y = y , x;
}
 var m = c { i } + c { j };
var n = c { k };
System.out.println ( y );
for l in range ( x ) :
    System.out.println ( m );
for l in range ( y - x ) :
    System.out.println ( n );
