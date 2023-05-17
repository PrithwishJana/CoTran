import math;
public void rmsValue ( arr , n ) {
    var square = 0;
    var mean = 0.0;
    root = 0.0;
    for i in range ( 0 , n ) :
        square += ( arr { i } ** 2 );
    mean = ( square / ( float ) ( n ) );
    var root = math . sqrt ( mean );
    return root;
}
if (var __name__ == '__main__') {
    var arr = { 10 , 4 , 6 , 8 };
    var n = len ( arr );
    System.out.println ( "{:.4f}" . format ( rmsValue ( arr , n ) ) );
}
 