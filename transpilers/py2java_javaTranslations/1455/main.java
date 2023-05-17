var numbers = list ( map ( int , input ( ) . split ( ) ) );
var columns = numbers { 0 };
var rows = numbers { 1 };
var counter = - 1;
data = {};
stop = 0;
for i in range ( 0 , columns ) :
    x = input ( );
    g = "not";
    s = 'not';
    count = 0;
    for j in range ( 0 , rows ) :
        if (x { j } == "S") {
            if (g == "found") {
                counter = count + 1 ;;
                if (not f"{counter}" in data) {
                    data { f"{counter}" } = 1;
                }
             }
             else{
                var stop = 1;
            }
            break;
        }
         else if (x { j } == 'G'){
            g = 'found';
            count = 0;
        }
        else{
            count += 1;
        }
System.out.println ( - 1 if len ( data ) == 0 or stop == 1 else len ( data ) );
