
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Collections;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

/*

  for loading and visualizing graphs G = (V,E) stored in a CSV format.
  Graphs have vertices V with integer heuristic values h(v), for each
  v in V, and edges E with integer weights w(e), for each e in E

*/

public class Graph {

    // attributes
    private HashMap<String,Integer> h; // heuristic value h(v)
    private HashMap<String,ArrayList<String>> N; // set N(v)
    private HashMap<String,HashMap<String,Integer>> w; // weight w(e)

    // construct the graph (attributes h, N and w)
    public Graph(String filename) {

	h = new HashMap<String,Integer>();
	HashMap<String,HashSet<String>> N_ = new HashMap<String,HashSet<String>>();
	w = new HashMap<String,HashMap<String,Integer>>();

	try {

	    BufferedReader reader = new BufferedReader(new FileReader(filename));

	    // process header

	    String line = reader.readLine();
	    String[] s = line.split(",");

	    assert s[0].trim().equals("v");
	    String es = s[1].trim();
	    String orientation = s[2].trim();

	    boolean heur = false;
	    if(es.equals("h")) {
		heur = true;

		es = orientation;
		orientation = s[3].trim();
	    }

	    assert es.equals("es");

	    boolean undir = false;
	    if(orientation.equals("undir"))
		undir = true;
	    else
		assert orientation.equals("dir");

	    // process remaining lines

	    String v;
	    int i;
	    line = reader.readLine();
	    while(line != null) {

		s = line.split(",");
		v = s[0].trim();

		i = 1;
		h.put(v, 0); // h(v) by default
		if(heur) {
		    h.put(v, Integer.valueOf(s[1].trim()));
		    ++i;
		}

		if(!N_.containsKey(v))
		    N_.put(v, new HashSet<String>());

		String[] t;
		String u;
		Integer W;
		while(i < s.length) {

		    t = s[i].split(":");
		    u = t[0].trim();

		    N_.get(v).add(u);
		    if(undir) {
			if(!N_.containsKey(u))
			    N_.put(u, new HashSet<String>());

			N_.get(u).add(v);
		    }

		    if(!w.containsKey(v))
			w.put(v, new HashMap<String,Integer>());

		    w.get(v).put(u, 1); // w(e) 1 by default
		    if(t.length > 1) {

			W = Integer.valueOf(t[1].trim());
			w.get(v).put(u, W);

			if(undir) {

			    if(w.containsKey(u)) {
				if(w.get(u).containsKey(v))
				    assert w.get(u).get(v).intValue() == W.intValue() :
				    "\n\nundirected graph with w("+v+","+u+") = "+W+
					" yet w("+u+","+v+") = "+w.get(u).get(v);
			    }
			    else
				w.put(u, new HashMap<String,Integer>());

			    w.get(u).put(v, W);
			}
		    }

		    ++i;
		}

		// next line
		line = reader.readLine();
	    }

	    N = new HashMap<String,ArrayList<String>>();
	    for(String key : N_.keySet()) {

		N.put(key, new ArrayList<String>(N_.get(key)));
		Collections.sort(N.get(key));
	    }
	}
	catch (IOException e) {
	    e.printStackTrace();
	}
    }
	
    // obtain heuristic value h(v), for each v in V
    public HashMap<String,Integer> get_h() {
	return this.h;
    }

    // obtain set N(v) of neighbours of v
    public HashMap<String,ArrayList<String>> getN() {
	return this.N;
    }

    // obtain weight w(e) for each edge e
    public HashMap<String,HashMap<String,Integer>> get_w() {
	return this.w;
    }
}
