public void findMaxGuests ( arrl , exit , n ) {
    arrl . sort ( ) ;;
    exit . sort ( ) ;;
    var guests_in = 1 ;;
    max_guests = 1 ;;
    time = arrl { 0 } ;;
    i = 1 ;;
    j = 0 ;;
    while (( i < n and j < n )) {
        if (( arrl { i } <= exit { j } )) {
            guests_in = guests_in + 1 ;;
            if (( guests_in > max_guests )) {
                max_guests = guests_in ;;
                time = arrl { i } ;;
            }
             i = i + 1 ;;
        }
         else{
            guests_in = guests_in - 1 ;;
            var j = j + 1 ;;
        }
    }
     System.out.println ( "Maximum Number of var Guests =" , max_guests , "at time" , time );
}
var arrl = { 1 , 2 , 10 , 5 , 5 } ;;
var exit = { 4 , 5 , 12 , 9 , 12 } ;;
var n = len ( arrl ) ;;
findMaxGuests ( arrl , exit , n ) ;;
