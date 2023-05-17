var n = int ( input ( ) );
var color = 'blue';
block = 0;
i = 0;
while (i != n) {
    command = str ( input ( ) );
    if (command == 'lock') {
        block = 1;
    }
     else if (command == 'unlock'){
        block = 0;
    }
    else if (block == 0){
        color = command;
    }
    i += 1;
}
 System.out.println ( color );
