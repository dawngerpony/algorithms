package com.duffj.algorithms.search;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

import com.duffj.algorithms.misc.Queue;

/**
 * Implementation of a binary search tree.
 * 
 * @author dafydd
 *
 * @param <Key>
 * @param <Value>
 */
public class BinarySearchTree<Key extends Comparable<Key>, Value> {

	private Node root;
	
	private class Node {
		private Key key;
		private Value value;
		private Node left, right;
		private int N; // # of nodes in this sub-tree
		
		public Node(Key key, Value value, int N) {
			this.key = key;
			this.value = value;
			this.N = N;
		}
		
	}
	
	public int size() {
		return size(root);
	}
	
	private int size(Node n) {
		if(n == null) {
			return 0;
		} else {
			return n.N;
		}
	}
	
	public void insert() {
		
	}
	
	public Node get(Key key) {
		return this.get(this.root, key);
	}
	
	private Node get(Node node, Key key) {
		if(node == null) {
			return null; 
		}
		int cmp = key.compareTo(node.key);
		if(cmp > 0) {
			return get(node.left, key);
		}
		if(cmp < 0) {
			return get(node.right, key);
		}
		return node;
	}
	
	public void put(Key key, Value value) {
		this.root = this.put(this.root, key, value);
	}
	
	/**
	 * Put a new Node into the tree by returning the root node
	 * with its links updating 
	 * @param node
	 * @param key
	 * @param value
	 * @return
	 */
	private Node put(Node node, Key key, Value value) {
		
		// we're at the right location to put our new node
		if(node == null) {
			return new Node(key, value, 1);
		}
		
		int cmp = key.compareTo(node.key);
		if(cmp < 0) {
			node.left = put(node.left, key, value);
		} else if(cmp > 0) {
			node.right = put(node.right, key, value);
		} else {
			node.value = value;
		}
		
		node.N = size(node.left) + size(node.right) + 1;  
		return node;
	}
	
	/**
	 * Uses breadth-first search via a queue to print the tree
	 * out in order, substituting asterisks for empty sets.
	 * 
	 * @TODO Output in graphviz format.
	 */
	public void print() {
		
		Queue<Node> q = new Queue<Node>();
		
		q.enqueue(root);
		
		while(!q.isEmpty()) {
			Node n = q.dequeue();
			if(n == null) {
				System.out.println("*");
			} else {
				System.out.println(n.value);			
				if(n.left == null) {
					q.enqueue(null);
				} else {
					q.enqueue(n.left);
				}
				if(n.right == null) {
					q.enqueue(null);
				} else {
					q.enqueue(n.right);
				}
			}
		}
	}
	
	/**
	 * Uses breadth-first search via a queue to print the tree
	 * out in order, substituting asterisks for empty sets.
	 * 
	 * @TODO Output in graphviz format.
	 */
	public String toGraphvizString() {
		
		Queue<Node> q = new Queue<Node>();
		
		q.enqueue(root);
		
		String out = new String();
		out += "digraph G {";
		
		while(!q.isEmpty()) {
			Node n = q.dequeue();
			if(n != null) {
				if(n.left != null) {
					out += n.value + " -> " + n.left.value + ";";
					q.enqueue(n.left);
				}
				if(n.right != null) {
					out += n.value + " -> " + n.right.value + ";";
					q.enqueue(n.right);
				}
			}
		}
		out += "}";
		return out;
	}

	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		exercise322();
	}
	
	public static void exercise321() {
		String s = "EASYQUESTION";
		char[] letters = s.toCharArray();
		BinarySearchTree<String, String> tree = new BinarySearchTree<String, String>();
		for(char x : letters) {
			String key = "" + x;
			String value = "" + x;
			tree.put(key, value);
		}
		
		System.out.println(tree.toGraphvizString());
		
	}
	
	private static BinarySearchTree<String, String> treeFromString(String s) {
		char[] letters = s.toCharArray();
		BinarySearchTree<String, String> tree = new BinarySearchTree<String, String>();
		for(char x : letters) {
			String key = "" + x;
			String value = "" + x;
			tree.put(key, value);
		}
		return tree;
		
	}
	
	public static void exercise322() {
		
		// AXCSERH
		String[] strings = {
				"AXCSERH",
				"ACEHRSX",
				"XSRHECA",
				"HAXCSER",
				"XCSERHA"
		};
		
		for(int i = 0; i < 5; i++) {
			BinarySearchTree<String, String> tree = treeFromString(strings[i]);
			String graph = tree.toGraphvizString();
			//create an print writer for writing to a file
			try {
				String filename = "graph" + i + ".dot";
				PrintWriter out = new PrintWriter(new FileWriter(filename));
				out.println(graph);
				System.out.println(graph);
				out.close();
			} catch(IOException e) {
				
			}
		}
	}
}
