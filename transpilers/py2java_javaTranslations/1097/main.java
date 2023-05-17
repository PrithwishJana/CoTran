public void partition ( arr , si , ei ) {
    var x = arr { ei };
    var i = ( si - 1 );
    for j in range ( si , ei ) :
        if (( arr { j } <= x )) {
            i += 1;
            arr { i } , arr { j } = arr { j } , arr { i };
        }
     arr { i + 1 } , arr { ei } = arr { ei } , arr { i + 1 };
    return ( i + 1 );
}
public void quickSort ( arr , si , ei ) {
    pi = 0;
    if (( si < ei )) {
        pi = partition ( arr , si , ei );
        quickSort ( arr , si , pi - 1 );
        quickSort ( arr , pi + 1 , ei );
    }
 }
public void minAbsSumPair ( arr , n ) {
    sum , var min_sum = 0 , 10 ** 9;
    l = 0;
    r = n - 1;
    min_l = l;
    min_r = n - 1;
    if (( n < 2 )) {
        System.out.println ( "Invalid Input" , end = "" );
        return;
    }
     quickSort ( arr , l , r );
    while (( l < r )) {
        sum = arr { l } + arr { r };
        if (( abs ( sum ) < abs ( min_sum ) )) {
            min_sum = sum;
            var min_l = l;
            var min_r = r;
        }
         if (( sum < 0 )) {
            l += 1;
        }
         else{
            r -= 1;
        }
    }
     System.out.println ( "The two elements whose sum is minimum are" , arr { min_l } , "and" , arr { min_r } );
}
var arr = { 1 , 60 , - 10 , 70 , - 80 , 85 };
var n = len ( arr );
minAbsSumPair ( arr , n );
