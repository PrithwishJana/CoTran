import sys;
var f = sys . stdin;
n , r , var l = map ( int , f . readline ( ) . split ( ) );
var appearance = { 0 } * n;
var point = { 0 } * n;
var top = 0;
pre_t = 0;
for (int line = 0; line < f.length; line++){
    d , t , x = map ( int , line . split ( ) );
    d -= 1;
    appearance { top } += t - pre_t;
    pre_t = t;
    point { d } += x;
    if (0 < x and top != d) {
        if (point { top } < point { d }) {
            top = d;
        }
         else if (point { top } == point { d } and d < top){
            top = d;
        }
    }
     else if (x < 0 and top == d){
        top = point . index ( max ( point ) );
    }
}
appearance { top } += l - pre_t;
System.out.println ( 1 + appearance . index ( max ( appearance ) ) );
