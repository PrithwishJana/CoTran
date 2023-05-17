import sys;
import collections.deque;
var input = sys . stdin . buffer . readline;
var N = int ( input ( ) );
var adj = { [ } for _ in range ( N + 1 ) ];
for _ in range ( N - 1 ) :
    a , var b = map ( int , input ( ) . split ( ) );
    adj { a } . append ( b );
    adj { b } . append ( a );
var que = deque ( );
que . append ( 1 );
var seen = { 0 } * ( N + 1 );
seen { 1 } = 1;
var par = { 0 } * ( N + 1 );
var child_num = { 0 } * ( N + 1 );
while (que) {
    var v = que . popleft ( );
    for u in adj { v } :
        if (seen { u } == 0) {
            seen { u } = 1;
            par { u } = v;
            child_num { v } += 1;
            que . append ( u );
        }
 }
 var seq = deque ( );
for i in range ( 1 , N + 1 ) :
    if (child_num { i } == 0) {
        seq . append ( i );
    }
 while (seq) {
    var c = seq . pop ( );
    seen { c } = 0;
    if (seen { par [ c } ] == 0) {
        System.out.println ( 'First' );
        exit ( );
    }
     seen { par [ c } ] = 0;
    child_num { par [ par [ c } ] ] -= 1;
    if (child_num { par [ par [ c } ] ] == 0) {
        seq . append ( par { par [ c } ] );
    }
 }
 System.out.println ( 'Second' );
