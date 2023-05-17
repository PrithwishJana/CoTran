var p_speed = int ( input ( ) );
var d_speed = int ( input ( ) );
var time = int ( input ( ) );
var wait = int ( input ( ) );
var distence = int ( input ( ) );
var position_p = time * p_speed;
var position_d = 0;
var counter = 0;
time_counter = 0;
while (position_p < distence and d_speed > p_speed) {
    var time_d = position_p / ( d_speed - p_speed );
    position_p += ( time_d * p_speed );
    if (position_p >= distence) {
        break;
    }
     var t_back = position_p / d_speed + wait;
    position_p += ( t_back * p_speed );
    counter += 1;
}
 System.out.println ( counter );
