public void is_correct ( hourMax , minuteMax , time ) {
    h , var m = time . split ( ":" );
    mirrored = { "0":"0" , "1":"1" , "2":"5" , "3":"" , "4":"" , "5":"2" , "6":"" , "7":"" , "8":"8" , "9":"" };
    mirrored_h = mirrored { h [ 1 } ] + mirrored { h [ 0 } ];
    mirrored_m = mirrored { m [ 1 } ] + mirrored { m [ 0 } ];
    if (len ( mirrored_h ) == 2 and int ( mirrored_h ) < minuteMax and len ( mirrored_m ) == 2 and int ( mirrored_m ) < hourMax) {
        return mirrored_m + ":" + mirrored_h;
    }
     return false;
}
var N = int ( input ( ) );
for _ in range ( N ) :
    hourMax , var minuteMax = map ( int , input ( ) . split ( ) );
    hourNow , var minuteNow = map ( int , input ( ) . split ( ":" ) );
    var result = "00:00";
    flag = false;
    for hour in range ( hourNow , hourMax ) :
        start = minuteNow if hour == hourNow else 0;
        for minute in range ( start , minuteMax ) :
            time = "0" * ( 2 - len ( str ( hour ) ) ) + str ( hour ) + ":" + "0" * ( 2 - len ( str ( minute ) ) ) + str ( minute );
            mirrored = is_correct ( hourMax , minuteMax , time );
            if (mirrored) {
                result = time;
                var flag = true;
                break;
            }
         if flag : break;
    System.out.println ( result );
