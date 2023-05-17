class measure {
    protected void init__ ( this , init , station_count ) {
        this . var init = init;
        this . station_count = station_count;
    }
    public void clockwise ( this , pos ) {
        return ( this . station_count - this . init + pos ) % this . station_count;
    }
    public void anticlockwise ( this , pos ) {
        return ( this . station_count + this . init - pos ) % this . station_count;
    }
}
import sys;
import bisect.bisect;
f = sys . stdin;
n , _ , init = map ( int , f . readline ( ) . split ( ) );
var d = sorted ( list ( map ( int , f ) ) );
var m = measure ( init , n );
var dist = {};
var n_pos = bisect ( d , init ) if d { 0 } < init < d { - 1 } else 0;
dist . append ( m . anticlockwise ( d { n_pos } ) );
var p_pos = n_pos - 1;
dist . append ( m . clockwise ( d { p_pos } ) );
for di , dj in zip ( d , d { - 1 : } + d { : - 1 } ) :
    dist . append ( m . anticlockwise ( di ) * 2 + m . clockwise ( dj ) );
    dist . append ( m . anticlockwise ( di ) + 2 * m . clockwise ( dj ) );
System.out.println ( min ( dist ) * 100 );
