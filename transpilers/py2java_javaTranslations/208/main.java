import array;
import bisect.*;
import collections.*;
import fractions;
import heapq;
import itertools.*;
import math;
import random;
import re;
import string;
import sys;
N , var X = map ( int , input ( ) . split ( ) );
var Xs = list ( map ( int , input ( ) . split ( ) ) );
var Ys = Xs { : : - 1 };
var Y_sum = { 0 } * N;
Y_sum { 0 } = Ys { 0 };
for i in range ( 1 , N ) :
    Y_sum { i } = Y_sum { i - 1 } + Ys { i };
var ans = 1e100;
for rep_num in range ( 1 , N + 1 ) :
    local_ans = X * rep_num;
    local_ans += 5 * Y_sum { rep_num - 1 };
    i = 2 * rep_num - 1;
    n = 1;
    while (i <= N - 1) {
        local_ans += ( 2 * n + 3 ) * ( Y_sum { i } - Y_sum { i - rep_num } );
        n += 1;
        i += rep_num;
    }
     local_ans += ( 2 * n + 3 ) * ( Y_sum { N - 1 } - Y_sum { i - rep_num } );
    ans = min ( ans , local_ans );
System.out.println ( ans + N * X );
