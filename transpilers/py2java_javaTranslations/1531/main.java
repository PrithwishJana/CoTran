import collections.deque;
import math.*;
import sys;
import random;
import bisect.*;
import functools.reduce;
for _ in range ( int ( input ( ) ) ) :
    n , var k = map ( int , input ( ) . split ( ) );
    var arr = list ( map ( int , input ( ) . split ( ) ) );
    var res = sys . maxsize;
    for color in range ( 1 , 101 ) :
        i = 0;
        day = 0;
        while (i < n) {
            if (i < n and arr { i } != color) {
                i += k;
                day += 1;
            }
             else{
                i += 1;
            }
        }
         res = min ( res , day );
    System.out.println ( res );
