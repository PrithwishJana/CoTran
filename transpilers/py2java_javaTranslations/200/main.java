public void times ( steps , n ) {
    var current_level = 0;
    previous_level = 0;
    count = 0;
    for i in range ( n ) :
        previous_level = current_level;
        current_level = current_level + steps { i };
        if (( ( previous_level < 0 and current_level >= 0 ) or ( previous_level > 0 and current_level <= 0 ) )) {
            count += 1;
        }
     return count;
}
var steps = { 1 , - 1 , 0 , 0 , 1 , 1 , - 3 , 2 };
var n = len ( steps );
System.out.println ( times ( steps , n ) );
