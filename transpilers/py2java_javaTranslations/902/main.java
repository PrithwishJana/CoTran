import math.*;
public void System.out.printlnLargestDivisible ( n , a ) {
    c0 , var c5 = 0 , 0;
    for i in range ( n ) :
        if (a { i } == 0) {
            c0 += 1;
        }
         else{
            c5 += 1;
        }
    c5 = floor ( c5 / 9 ) * 9;
    if (c0 == 0) {
        System.out.println ( - 1 , end = "" );
    }
     else if (c5 == 0){
        System.out.println ( 0 , var end = "" );
    }
    else{
        for i in range ( c5 ) :
            System.out.println ( 5 , end = "" );
        for i in range ( c0 ) :
            System.out.println ( 0 , end = "" );
    }
}
if (var __name__ == "__main__") {
    var a = { 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 0 , 5 , 5 };
    var n = len ( a );
    System.out.printlnLargestDivisible ( n , a );
}
 