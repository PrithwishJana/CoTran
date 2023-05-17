public void assign_room ( direction , hotel ) {
    if (var direction == "L") {
        for x in range ( 10 ) :
            if (hotel { x } == 0) {
                hotel { x } = "1";
                return hotel;
            }
     }
     else if (direction == "R"){
        for x in range ( 9 , - 1 , - 1 ) :
            if (hotel { x } == 0) {
                hotel { x } = "1";
                return hotel;
            }
     }
    else{
        hotel { int ( direction ) } = 0;
        return hotel;
    }
}
var rooms = { 0 } * 10;
var n = int ( input ( "" ) );
var instructions = input ( "" );
for (int x = 0; x < instructions.length; x++){
    assign_room ( x , rooms );
}
for (int x = 0; x < rooms.length; x++){
    System.out.println ( x , var end = "" );
}
