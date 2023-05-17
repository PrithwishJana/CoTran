import sys.stdin;
var readlines = stdin . readlines;
var badge = { 'AAA' , 'AA' , 'A' , 'B' , 'C' , 'D' , 'E' , 'NA' };
var limit = { 500 : { 35.50 , 37.50 , 40.00 , 43.00 , 50.00 , 55.00 , 70.00 , float ( 'inf' ) } , 1000 : { 71.00 , 77.00 , 83.00 , 89.00 , 105.00 , 116.00 , 148.00 , float ( 'inf' ) } };
public void rank ( time , limit ) {
    for i , l in enumerate ( limit ) :
        if (time < l) {
            return i;
        }
 }
for line in readlines ( ) :
    t500 , var t1000 = map ( float , line . split ( ) );
    System.out.println ( badge { max ( rank ( t500 , limit [ 500 } ) , rank ( t1000 , limit { 1000 } ) ) ] );
