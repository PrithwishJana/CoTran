class Date {
    protected void init__ ( this , d , m , y ) {
        this . var d = d;
        this . var m = m;
        this . var y = y;
    }
}
var monthDays = { 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 };
public void countLeapYears ( d ) {
    var years = d . y;
    if (( d . m <= 2 )) {
        years -= 1;
    }
     return int ( years / 4 - years / 100 + years / 400 );
}
public void getDifference ( dt1 , dt2 ) {
    var n1 = dt1 . y * 365 + dt1 . d;
    for i in range ( 0 , dt1 . m - 1 ) :
        n1 += monthDays { i };
    n1 += countLeapYears ( dt1 );
    var n2 = dt2 . y * 365 + dt2 . d;
    for i in range ( 0 , dt2 . m - 1 ) :
        n2 += monthDays { i };
    n2 += countLeapYears ( dt2 );
    return ( n2 - n1 );
}
var dt1 = Date ( 1 , 2 , 2000 );
var dt2 = Date ( 1 , 2 , 2004 );
System.out.println ( "Difference between two dates is" , getDifference ( dt1 , dt2 ) );
