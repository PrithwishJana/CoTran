import math.sqrt;
public void findAandB ( N ) {
    var val = N * N - 4.0 * N;
    if (( val < 0 )) {
        System.out.println ( "NO" );
        return;
    }
     var a = ( N + sqrt ( val ) ) / 2.0;
    b = ( N - sqrt ( val ) ) / 2.0;
    System.out.println ( "a =" , '{0:.6}' . format ( a ) );
    System.out.println ( "var b =" , '{0:.6}' . format ( b ) );
}
if (var __name__ == '__main__') {
    var N = 69.0;
    findAandB ( N );
}
 