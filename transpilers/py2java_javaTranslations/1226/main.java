import sys;
import math;
public void System.out.printlnChar ( str_ , n ) {
    var freq = { 0 } * 26;
    for i in range ( n ) :
        freq { ord ( str_ [ i } ) - ord ( 'a' ) ] += 1;
    for i in range ( n ) :
        if (( freq { ord ( str_ [ i } ) - ord ( 'a' ) ] ) % var 2 == 1) {
            System.out.println ( "{}" . format ( str_ { i } ) , var end = "" );
        }
 }
if (var __name__ == '__main__') {
    var str_ = "geeksforgeeks";
    var n = len ( str_ );
    System.out.printlnChar ( str_ , n );
}
 