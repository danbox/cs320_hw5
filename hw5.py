__author__ = 'Dan Boxler'

'''
This is an implementation of the adjacency-list representation of a graph
where the vertices are numbered from 0 through n-1.

The class has an integer variable _m that records the number m of edges,
and it has a list _verts of length n of lists of integers.
The list that appears in position i of this list is the list of neighbors
of vertex i.  For example, if _verts is [[1,2], [], [0]], then
there are three vertices, since there are three lists in it.  Vertex 0
has neighbors 1 and 2, vertex 1 has no neighbors, and vertex has 0 as
its only neighbor.

Unlike in Java, where you can often omit mention of 'this', you must
always name the object before the dot.  Therefore, you have to name
'self' a lot.  Also, 'self' appears in the list of parameters, even though
this parameter is passed in by putting an object before the dot.

For example, he first method getn(self), when called on graph object 'G',
is called as follows:  'G.self()'.  The object referenced by 'G' appears
in the formal parameter list of the definition, and is referenced using
'self' inside the method.
'''
class Graph:
    ''' 'self' is similar to 'this' in Java.  If you call G.getn(), then
        G is 'self'.  You have to list 'self' in the formal parameter list. '''
    def getn(self):
        return len(self._verts)

    def getm(self):
        return self._m

    ''' constructor.  __init__ is a reserved keyword identifying it
        as a constructor.  numVerts tells how many vertices it should have.
        edgeList is a list of ordered pairs, one for each edge, in any order.
        Example: numVerts = 3 and edgeList = [(0,1), (1,2), (0,2), (2,0)]'''
    def __init__ (self, numVerts, edgeList):
        self._m = len(edgeList)
        self._verts = [[] for i in range(numVerts)]
        for u, v in edgeList:
            self._verts[u].append(v)


    ''' Return the transpose of the graph, that is, the result of reversing
        all the edges '''
    def transpose (self):
        #create new list for transpose
        transpose = [[] for i in range(self.getn())]

        for index, vertex in enumerate(self._verts):
            for adjacent in vertex:
                transpose[adjacent].append(index)

        return transpose

    ''' This is similar to the Java toString() for the class.
        The string '__str__ 'is a reserved string, just as 'toString' is in Java.'''
    def __str__(self):
        return 'n = ' + str(self.getn()) + ' m = ' + str(self.getm()) + '\n' + str(self._verts)


    ''' DFS.  colored[j] = True if vertex j is colored, and it's False if j is
        white.  The parameter i is the vertex number of the vertex to start
        at, and it must be white '''
    def dfs(self, i, colored):
        colored[i] = True
        for j in self._verts[i]:
            if not colored[j]:
                self.dfs(j, colored)

    '''  Determine whether the graph is strongly connected '''
    def stronglyConnected(self):
        # fill in code here

        #create list for colored
        colored = [False for i in range(self.getn())]

        reachable = self._verts[vertex]


        return True

    ''' This is a variant on DFS that returns a list of vertices that
        were blackened during the call, in the order in which they finished. '''
    def finishOrder(self, i, colored, finished):
        # fill in code here
        return finished

    ''' Go through each in the graph in the order given by vertOrder,
        calling DFS on the vertex if it's still white.  If no vertOrder
        parameter is given, then go through them in ascending order of
        vertex number.   Return a list L of lists, where each list in L
        is the vertices blackened by one of the calls to DFS generated
        from the main loop of blacken.

        Being able to specify the order in which you go through them is
        useful for the strongly-connected componentns algorithm. '''
    def blacken(self, vertOrder = None):
        finished = []
        # fill in code here
        return finished

    ''' Return the strongly-connected components, as a list L of lists of
        integers.  Each list in L has the vertices in one strongly-connected
        components. '''
    def scc(self):
        # fill in code here
        return []

'''  Read a graph in from a file.  The format of the file is as follows:
     The first line gives the number of vertices.
     Each subsequent line gives an ordered pair of vertices, separated by
     a comma, indicating a directed edge.

     Example:
     ----
     3
     0,1
     1,2
     0,2
     2,0
     ----

     This gives a graph with three vertices and four directed edges,
     (0,1), (1,2), (0,2), (2,0)
'''

def readGraph(filename):
    edgeList = []
    fp = open(filename, 'r')
    n = int(fp.readline())
    for line in fp:
        u,v  = [int(x) for x in line.split(',')]
        edgeList.append((u,v))
    return Graph(n, edgeList)

''' This is what executes when you run the command python -i hw5.py '''

if __name__ == '__main__':

    G = readGraph('input.txt')
    print(G)
