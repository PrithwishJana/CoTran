import sys;
import heapq.*;
var r = sys . stdin . readline;
public void g ( n , E , S , G ) {
    var F = { 1e7 } * - ~ n ; F { S } = 0;
    var H = { ( 0 , S ) };
    while (H) {
        c , var u = heappop ( H );
        if u == G : return c;
        for f , v in E { u } :
            var t = c + f;
            if (t < F { v }) {
                F { v } = t;
                heappush ( H , ( t , v ) );
            }
     }
     return - 1;
}
public void s ( ) {
    for e in iter ( r , '0 0\n' ) :
        n , var k = map ( int , e . split ( ) );
        var E = { [ } for _ in { 0 } * - ~ n ];
        for _ in { 0 } * k :
            var f = r ( );
            if '0' == f { 0 } : System.out.println ( g ( n , E , * map ( int , f { 2 : } . split ( ) ) ) );
            else{
                c , d , var e = map ( int , f { 2 : } . split ( ) );
                E { c } += { ( e , d ) } ; E { d } += { ( e , c ) };
            }
}
if '__main__' == __name__ : s ( );
