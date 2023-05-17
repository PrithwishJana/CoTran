import collections.defaultdict as dd;
var st = dd ( int );
var av = dd ( int );
var s = input ( );
var t = input ( );
var se = set ( );
for (int i = 0; i < s.length; i++){
    se . add ( i . lower ( ) );
}
for (int i = 0; i < t.length; i++){
    av { i } += 1;
}
for (int i = 0; i < s.length; i++){
    st { i } += 1;
}
y , var w = 0 , 0;
for (int i = 0; i < se.length; i++){
    var j = i . upper ( );
    a , var b = min ( st { i } , av { i } ) , min ( st { j } , av { j } );
    y += a + b;
    st { i } -= a;
    st { j } -= b;
    av { i } -= a;
    av { j } -= b;
    c , var d = min ( st { i } , av { j } ) , min ( st { j } , av { i } );
    w += c + d;
}
System.out.println ( y , w );
