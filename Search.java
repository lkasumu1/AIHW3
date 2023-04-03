
import java.util.ArrayList;
import java.util.Collections;

/*

  for performing various search strategies on graphs G = (V,E) of
  vertices V and edges E, input as the set N(v) of neighbours for each
  v in V

*/

public class Search {

    // attributes
    private Graph G; // the graph G = (V,E) that we will search

    // construct a search object (load the graph)
    public Search(String filename) {

	G = new Graph(filename);
    }

    public Search(Graph G) {

	this.G = G;
    }
    
    // perform breadth-first search (BFS) on graph G for a goal vertex
    // starting from some start vertex
    public ArrayList<String> BFS(String start, String goal) {

	// the order in which vertices are visited
	ArrayList<String> order = new ArrayList<String>();

	ArrayList<String> queue = new ArrayList<String>();
	queue.add(start);

	String v;
	while(!queue.isEmpty()) {

	    v = queue.remove(0);
	    order.add(v);

	    if(v.equals(goal))
		break;

	    queue.addAll(this.G.getN().get(v));
	}

	return order;
    }

    // perform depth-first search (DFS) on graph G for a goal vertex
    // starting from some start vertex
    public ArrayList<String> DFS(String start, String goal) {

	// the order in which vertices are visited
	ArrayList<String> order = new ArrayList<String>();

	ArrayList<ArrayList<String>> stack = new ArrayList<ArrayList<String>>();
	stack.add(new ArrayList<String>());
	stack.get(0).add(start);

	String v;
	ArrayList<String> temp;
	while(!stack.isEmpty()) {

	    // should the list at the top of the stack be empty
	    if(stack.get(stack.size()-1).isEmpty()) {
		stack.remove(stack.size()-1);
		continue;
	    }

	    temp = stack.get(stack.size()-1);
	    v = temp.remove(temp.size()-1);
	    order.add(v);

	    if(v.equals(goal))
		break;

	    temp = new ArrayList<String>(this.G.getN().get(v));
	    Collections.reverse(temp);
	    stack.add(temp);
	}

	return order;
    }

    // perform depth-first search (DFS) for a goal vertex starting
    // from some start vertex, using recursion to do so
    public ArrayList<String> DFSrec(String start, String goal) {

	// the order in which vertices are visited
	ArrayList<String> order = new ArrayList<String>();

	DFSaux(order, start, goal);

	return order;
    }

    // auxiliary function for DFSrec which does the actual recursion
    // (see python)
    public boolean DFSaux(ArrayList<String> order, String v, String goal) {

	order.add(v);

	if(v.equals(goal))
	    return true;

	for(String u : this.G.getN().get(v))
	    if(DFSaux(order, u, goal))
		return true;

	return false;
    }
}
