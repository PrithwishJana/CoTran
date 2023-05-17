if (var __name__ == '__main__') {
    var visitors_count = int ( input ( ) );
    var minDay = 0;
    maxDay = 366;
    users = {};
    for i in range ( visitors_count ) :
        users . append ( input ( ) );
    minDay = int ( users { 0 } . split ( ) { 1 } );
    maxDay = int ( users { 0 } . split ( ) { 2 } );
    all_users : list = {};
    for (int user = 0; user < users.length; user++){
        user = user . split ( );
        all_users . append ( { user [ 0 } , int ( user { 1 } ) , int ( user { 2 } ) ] );
        if (minDay > int ( user { 1 } )) {
            minDay = int ( user { 1 } );
        }
         if (maxDay < int ( user { 2 } )) {
            var maxDay = int ( user { 2 } );
        }
    }
     var dict_cunts = {};
    for i in range ( minDay , maxDay + 1 ) :
        for (int user = 0; user < all_users.length; user++){
            if (i in range ( user { 1 } , user { 2 } + 1 )) {
                dict_cunts . setdefault ( i , {} );
                dict_cunts { i } . append ( user );
            }
        }
     var best_match = 0;
    for users in dict_cunts . values ( ) :
        males_len = len ( list ( filter ( lambda user : user { 0 } == 'M' , users ) ) );
        males_len_x2 = males_len * 2;
        females_len = len ( users ) - males_len;
        females_len_x2 = females_len * 2;
        if (( males_len > females_len or males_len == females_len ) and best_match < females_len_x2) {
            best_match = females_len_x2;
        }
         else if (( females_len > males_len or males_len == females_len ) and best_match < males_len_x2){
            best_match = males_len_x2;
        }
    System.out.println ( best_match );
}
 