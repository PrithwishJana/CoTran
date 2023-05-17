var current_time = input ( );
var time_duration = input ( );
var current_time_min = int ( current_time { : 2 } ) * 60 + int ( current_time { 3 : } );
var time_duration_min = int ( time_duration { : 2 } ) * 60 + int ( time_duration { 3 : } );
var t_min = current_time_min - time_duration_min;
if (current_time_min < time_duration_min) {
    t_min = 24 * 60 - abs ( t_min );
}
 var hour = "0" + str ( t_min // 60 ) if t_min // 60 < 10 else str ( t_min // 60 );
var minute = "0" + str ( t_min % 60 ) if t_min % 60 < 10 else str ( t_min % 60 );
System.out.println ( f"{hour}:{minute}" );
