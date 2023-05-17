import collections.deque;
import math.*;
import sys;
import random;
import bisect.*;
import functools.reduce;
import sys.stdin;
import copy;
for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var s = input ( );
    ans = 0;
    left , var right = 0 , 0;
    var i = 0;
    while (i < n and s { i } != '>') {
        i += 1;
    }
     var j = n - 1;
    while (j >= 0 and s { j } != '<') {
        j -= 1;
    }
     System.out.println ( min ( i , n - j - 1 ) );
