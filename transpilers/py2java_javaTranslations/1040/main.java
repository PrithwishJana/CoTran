var number = int ( input ( ) );
var arr = list ( map ( int , input ( ) . split ( ) ) );
var counter = 0;
data = { "found" : "NO" , 'first' : 0 };
for i in range ( 0 , number ) :
    x = int ( arr { i } );
    if (x == 1) {
        if (counter == 0) {
            counter = 1;
        }
         if (data { 'found' } == "yes") {
            y = i - data { 'first' };
            counter = counter * y;
            data { 'first' } = i;
        }
         else{
            data { 'found' } = "yes";
            data { 'first' } = i;
        }
    }
 System.out.println ( counter );
