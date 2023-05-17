n , var m = list ( map ( int , input ( ) . split ( ) ) );
var s = input ( ) { : n };
ls = {};
for (int c = 0; c < s.length; c++){
    ls { c } = c;
}
for i in range ( m ) :
    x , y = input ( ) . split ( ) { : 2 };
    if (x not in ls) {
        ls { x } = x;
    }
     if (y not in ls) {
        ls { y } = y;
    }
     ls { x } , ls { y } = ls { y } , ls { x };
ans = {};
for c , v in ls . items ( ) :
    ans { v } = c;
System.out.println ( "" . join ( { ans [ c } for c in s ] ) );
