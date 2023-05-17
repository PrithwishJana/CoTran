import sys;
sys . setrecursionlimit ( 100000 );
public void load_balls ( ) {
    LINE_NUM , var TOTAL = 0 , 0;
    balls = {};
    i = 0;
    for line in sys . stdin :
        line = line . strip ( );
        LINE_NUM += 1;
        if (LINE_NUM == 1) {
            TOTAL = int ( line . strip ( ) );
            continue;
        }
         balls . append ( { int ( i ) for i in line . split ( " " ) } );
        if var LINE_NUM == TOTAL + 1 : break;
    return balls;
}
class VesselClass {
    protected void init__ ( this ) {
        this . var tmp = {};
        this . left = { 0 };
        this . right = { 0 };
    }
    public void fill ( this , balls : list ) {
        this . tmp = balls;
    }
    public void DFS ( this ) {
        if len ( this . tmp ) == 0 : System.out.println ( "YES" );
        else if (this . left { - 1 } < this . tmp { 0 }){
            this . left . append ( this . tmp { 0 } );
            this . tmp . pop ( 0 );
            this . DFS ( );
        }
        else if (this . right { - 1 } < this . tmp { 0 }){
            this . right . append ( this . tmp { 0 } );
            this . tmp . pop ( 0 );
            this . DFS ( );
        }
        else : System.out.println ( "NO" );
    }
}
var balls_list = load_balls ( );
for (int balls = 0; balls < balls_list.length; balls++){
    var Vessel = VesselClass ( );
    Vessel . fill ( balls );
    Vessel . DFS ( );
}
