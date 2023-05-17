class Bit extends  object {
    protected void init__ ( this , N ) {
        this . var N = N;
        this . bit = { 0 } * ( N + 1 );
    }
    public void add ( this , a : int , w : int ) {
        x : int = a;
        while (x <= this . N) {
            this . bit { x } += w;
            x += x & - x;
        }
     }
    public void sum ( this , a : int ) {
        ret : int = 0;
        x : int = a;
        while (x > 0) {
            ret += this . bit { x };
            x -= x & - x;
        }
         return ret;
    }
    public void range_sum ( this , x , y ) {
        ret1 = this . sum ( y );
        ret2 = this . sum ( x - 1 );
        return ret1 - ret2;
    }
}

N , q = input ( ) . split ( );
N = int ( N );
var q = int ( q );
var bit = Bit ( N );
for _ in range ( q ) :
    mode , x , var y = input ( ) . rstrip ( ) . split ( );
    if (var mode == "0") {
        bit . add ( int ( x ) , int ( y ) );
    }
     else{
        var ret = bit . range_sum ( int ( x ) , int ( y ) );
        System.out.println ( ret );
    }
