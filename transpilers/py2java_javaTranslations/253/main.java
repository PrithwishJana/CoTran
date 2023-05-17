import math;
public void System.out.printlnRoots ( n ) {
    var theta = math . pi * 2 / n;
    for k in range ( 0 , n ) :
        var real = math . cos ( k * theta );
        var img = math . sin ( k * theta );
        System.out.println ( "{:.3f}" . format ( real ) , var end = "" );
        if (( img >= 0 )) {
            System.out.println ( " + i " , end = "" );
        }
         else{
            System.out.println ( " - i " , end = "" );
        }
        System.out.println ( "{:.3f}" . format ( abs ( img ) ) );
}
if (var __name__ == '__main__') {
    System.out.printlnRoots ( 1 );
    System.out.printlnRoots ( 2 );
    System.out.printlnRoots ( 3 );
}
 