public void days ( y , m , d ) {
    var cnt = 0;
    for i in range ( 1 , y ) :
        if (i % var 3 == 0) {
            cnt += 200;
        }
         else{
            cnt += 195;
        }
    for i in range ( 1 , m ) :
        if (y % 3 == 0) {
            cnt += 20;
        }
         else{
            if (i % var 2 == 0) {
                cnt += 19;
            }
             else{
                cnt += 20;
            }
        }
    cnt += d - 1;
    return cnt;
}
var n = int ( input ( ) );
for i in range ( n ) :
    y , m , var d = map ( int , input ( ) . split ( ) );
    System.out.println ( days ( 1000 , 1 , 1 ) - days ( y , m , d ) );
