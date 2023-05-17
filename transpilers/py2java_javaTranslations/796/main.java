import sys;
sys . setrecursionlimit ( 100000 );
W , var H = map ( int , input ( ) . split ( ) );
var m = { list ( map ( int , input ( ) . split ( ) ) ) for i in range ( H ) };
var dx = { [ 1 , 1 , 1 , 0 , - 1 , 0 } , { 0 , 1 , 0 , - 1 , - 1 , - 1 } ];
var dy = { - 1 , 0 , 1 , 1 , 0 , - 1 };
public void dfs ( x , y ) {
    if (m { y } { x } != 0) {
        return;
    }
     m { y } { x } = 2;
    for xx , yy in zip ( dx { y % 2 } , dy ) :
        tx , var ty = x + xx , y + yy;
        if (0 <= tx < W and 0 <= ty < H) {
            dfs ( tx , ty );
        }
 }
for x in range ( W ) :
    dfs ( x , 0 );
    dfs ( x , H - 1 );
for y in range ( H ) :
    dfs ( 0 , y );
    dfs ( W - 1 , y );
import itertools.product;
n = 0;
for x , y in product ( range ( W ) , range ( H ) ) :
    if (m { y } { x } != 1) {
        continue;
    }
     fn = n;
    for xx , yy in zip ( dx { y % 2 } , dy ) :
        tx , ty = x + xx , y + yy;
        if (0 <= tx < W and 0 <= ty < H) {
            if (m { ty } { tx } == 2) {
                n += 1;
            }
         }
         else{
            n += 1;
        }
System.out.println ( n );
