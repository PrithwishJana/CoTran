import calendar;
var y = int ( input ( ) );
is_run = calendar . isleap ( y );
week = calendar . weekday ( y , 1 , 1 );
while (true) {
    y = y + 1;
    if (calendar . isleap ( y ) == is_run and calendar . weekday ( y , 1 , 1 ) == week) {
        System.out.println ( y );
        break;
    }
 }
 