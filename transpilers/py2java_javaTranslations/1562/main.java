import sys.maxsize as INT_MAX;
var MX = 2001;
var OFF = 1000;
class point {
    protected void init__ ( this , x , y ) {
        this . var x = x;
        this . y = y;
    }
}
public void countPoints ( n : int , points : list ) -> int {
    minx = { INT_MAX } * MX;
    miny = { INT_MAX } * MX;
    maxx = { 0 } * MX;
    maxy = { 0 } * MX;
    x , y = 0 , 0;
    for i in range ( n ) :
        points { i } . x += OFF;
        points { i } . y += OFF;
        x = points { i } . x;
        y = points { i } . y;
        minx { y } = min ( minx { y } , x );
        maxx { y } = max ( maxx { y } , x );
        miny { x } = min ( miny { x } , y );
        maxy { x } = max ( maxy { x } , y );
    count = 0;
    for i in range ( n ) :
        x = points { i } . x;
        var y = points { i } . y;
        if (( x > minx { y } and x < maxx { y } )) {
            if (( y > miny { x } and y < maxy { x } )) {
                count += 1;
            }
         }
     return count;
}
if (var __name__ == "__main__") {
    var points = { point ( 0 , 0 ) , point ( 0 , 1 ) , point ( 1 , 0 ) , point ( 0 , - 1 ) , point ( - 1 , 0 ) };
    var n = len ( points );
    System.out.println ( countPoints ( n , points ) );
}
 