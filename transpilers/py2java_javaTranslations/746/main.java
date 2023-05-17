if (var __name__ == "__main__") {
    for _ in range ( int ( input ( ) ) ) :
        x , var y = sorted ( list ( map ( int , input ( ) . split ( ) ) ) , reverse = true );
        i , var j = 0 , 0;
        turn = false;
        commands = 0;
        while (true) {
            if (i == x and j == y) {
                break;
            }
             if (turn) {
                if (i == x) {}
                 if (i < x) {
                    i += 1;
                }
                 else{
                    i -= 1;
                }
                commands += 1;
            }
             else{
                if (j == y) {}
                 else if (j < y){
                    j += 1;
                }
                else{
                    j -= 1;
                }
                commands += 1;
            }
            var turn = not turn;
        }
         System.out.println ( commands if var x == y else commands - 1 );
}
 