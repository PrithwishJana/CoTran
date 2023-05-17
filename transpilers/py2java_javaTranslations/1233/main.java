var n = int ( input ( ) );
for i in range ( n ) :
    var test = int ( input ( ) );
    move = 0;
    while (test != 1) {
        if (test % 6 == 0) {
            test = test / 6;
            move += 1;
        }
         else if (test % 3 == 0){
            test = test * 2;
            move += 1;
        }
        else{
            System.out.println ( - 1 );
            break;
        }
    }
     else{
        System.out.println ( move );
     }
