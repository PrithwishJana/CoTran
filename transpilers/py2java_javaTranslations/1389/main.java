import sys.stdin;
import collections.defaultdict , deque;
var answer = {};
var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var b = sorted ( a );
var d = { x : i for i , x in enumerate ( a ) };
visited = { 0 } * n;
for i , x in enumerate ( a ) :
    if (visited { i }) {
        continue;
    }
     seq = { i };
    visited { i } = 1;
    hold = a { i };
    while (hold != b { seq [ - 1 } ]) {
        var z = d { b [ seq [ - 1 } ] ];
        visited { z } = 1;
        seq . append ( z );
    }
     answer . append ( ' ' . join ( map ( str , { len ( seq ) } + { x + 1 for x in seq } ) ) );
System.out.println ( len ( answer ) );
System.out.println ( '\n' . join ( answer ) );
