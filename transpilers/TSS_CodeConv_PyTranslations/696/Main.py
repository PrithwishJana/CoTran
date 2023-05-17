import math

class Main:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        Main.IN = java.util.Scanner(System.in)
        Main._sc = None
        Main.IN = Scanner(System.in)
        Main._sc = java.util.Scanner(System.in)
        Main.INF = 1 << 28
        self.EPS = 1e-10
        Main.MOD = 1000000
        self.es = [[ 0, 1, 2, 3 ], [ 0, 1, 2 ], [ 0, 1, 2, 4 ], [ 2, 3 ], [ 0, 4 ]]
        self.len = 5
        self.scan = None
        Main._N = 0
        Main.MOD = 1000000007
        self._node = None
        Main.n = 0
        self.t = [0 for _ in range(10)]
        Main.INF = 1 << 30
        Main._sc = Scanner(System.in)
        self.EPS = 1e-9
        Main.m = 0
        Main.a = None
        Main._MAX = 'Z' - 'A' + 1
        self.inDeg = None
        self.outDeg = None
        Main.vis = None
        self.nei = None
        Main.INF = Integer.MAX_VALUE
        Main.MOD = 1000000007
        self.TOKENS = ["A", "C", "G", "T"]
        Main.memo = None
        Main._N = 12
        self.ofs = [[ 1, 0 ], [ 0, - 1 ], [ - 1, 0 ], [ 0, 1 ]]
        self.log = None
        self.result = System.out
        self.systemin = None
        self.graph = None
        self.visited = None
        self.color = None
        self.one = 0
        self.bipartite = 0
        Main.count = 0
        self.mujun = False
        self.maxes = None
        self.len = 393
        Main.h = 0
        Main.w = 0
        Main.map = None
        self.v = None
        self.dy = [- 1, - 1, 0, 0, 1, 1]
        self.dx1 = [0, 1, - 1, 1, 0, 1]
        self.dx2 = [- 1, 0, - 1, 1, - 1, 0]
        Main.grid = None
        Main.B = False
        self.W = False
        self.countB = 0
        self.countW = 0
        self.dx = [1, - 1, 0, 0]
        self.dy = [0, 0, 1, - 1]
        self.from_ = '\0'
        self.to = '\0'
        self.countGrid = 0

    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = BufferedInputStream(DataInputStream(System.in))
        reader = BufferedReader(InputStreamReader(in_))
        tasks = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray()
        taskList = java.util.concurrent.LinkedBlockingQueue()
        events = PriorityQueue(tasks [0])
        taskDur = [0 for _ in range(tasks [0])]
        i = 0
        while i < tasks [0]:
            taskInput = Arrays.stream(reader.readLine().split(" ")).mapToLong(Long :: parseLong).toArray()
            taskDur [i] = taskInput [1]
            events.add(taskInput [0] * 2 + 1)
            i += 1
        sol = [0 for _ in range(tasks [0])]
        nextTask = 0
        while events.size() > 0:
            event = events.poll()
            time = math.trunc(event / float(2))
            if math.fmod(event, 2) == 0:
                taskId = taskList.poll()
                sol [taskId] = time
                if not taskList.isEmpty():
                    events.add((time + taskDur [taskList.peek()]) * 2)
            else:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: int task = nextTask ++;
                task = nextTask 
                nextTask += 1
                if taskList.size() <= tasks [1]:
                    taskList.add(task)
                    if taskList.size() == 1:
                        events.add((time + taskDur [task]) * 2)
                else:
                    sol [task] = - 1
        print(Arrays.stream(sol).boxed().map(Object :: toString).collect(java.util.stream.Collectors.joining(" ")))
