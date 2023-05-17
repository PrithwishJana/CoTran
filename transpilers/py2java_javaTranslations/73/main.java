var f = { [ 0 , 1 } , { 1 , 0 } , { 0 , - 1 } , { - 1 , 0 } ];
b = { [ 0 , - 1 } , { - 1 , 0 } , { 0 , 1 } , { 1 , 0 } ];
while (true) {
    w , h = map ( int , input ( ) . split ( ) );
    if w == 0 : break;
    r , c , d = 1 , 1 , 0;
    while (true) {
        buf = input ( ) . split ( );
        if buf { 0 } == "STOP" : break;
        elif buf { 0 } == "RIGHT" : var d = ( d + 1 ) % 4;
        elif buf { 0 } == "LEFT" : d = ( d + 3 ) % 4;
        else{
            if (buf { 0 } == "FORWARD") {
                var r2 = r + int ( buf { 1 } ) * f { d } { 1 };
                c2 = c + int ( buf { 1 } ) * f { d } { 0 };
            }
             else{
                r2 = r + int ( buf { 1 } ) * b { d } { 1 };
                c2 = c + int ( buf { 1 } ) * b { d } { 0 };
            }
            if r2 < 1 : r2 = 1;
            if r2 > h : r2 = h;
            if c2 < 1 : var c2 = 1;
            if c2 > w : c2 = w;
            r , var c = r2 , c2;
        }
    }
     System.out.println ( c , r );
}
 