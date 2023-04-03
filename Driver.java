
import java.util.ArrayList;

public class Driver {

    public static void main(String[] args) {

	Graph G = new Graph(args[0]);

	System.out.println("\nGraph structures, h, N and w:\n");

	System.out.println("h = " + G.get_h() + "\n");
	System.out.println("N = " + G.getN() + "\n");
	System.out.println("w = " + G.get_w() + "\n");

	Search search = new Search(G);

	System.out.println("Search orders:\n");

	ArrayList<String> order = search.BFS("s","g");
	System.out.println("BFS: " + order);

	order = search.DFS("s","g");
	System.out.println("DFS:    " + order);

	order = search.DFSrec("s","g");
	System.out.println("DFSrec: " + order);
    }
}
