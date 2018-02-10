package LinkedList;


class Node<T>{
	
	T data;
	Node<T> next;
	Node(T data){
		this.data =data;
	}
}

class MyLinkedList<T>{
	
	private Node<T> head;
	private int count=0;
	
	public void add(T data){
		count++;
		if(head==null){
			Node<T> node = new Node<>(data);
			node.next = null;
			head = node;
		}else{
			Node<T> s = head;
			while(s.next!=null){
				s=s.next;
			}
			Node<T> node = new Node<>(data);
			node.data = data;
			node.next = null;
			s.next = node;
		}
	}
	public void addFirst(T data){
		count++;
		Node<T> node = new Node<>(data);
		node.next = head;
		head = node;
	}
	public void addLast(T data){
		count++;
		Node<T> node = new Node<>(data);
		node.next = null;
		Node<T> tmp = head;
		while(tmp.next !=null){
			tmp = tmp.next;
		}
		tmp.next = node;
	}
	
	public void insert(int index, T data){
		count++;
		Node<T> tmp = head;
		Node<T> prev = tmp;
		while(index > 1){
			index--;
			prev = tmp;
			tmp=tmp.next;
		}
		Node<T> newNode = new Node<>(data);
		newNode.next = tmp;
		prev.next = newNode;
	}
	
	public T remove(T data){
		
		if(head.data.equals(data)){
			T val = (T) head.data;
			Node<T> tmp = head.next;
			head.next=null;
			head  = tmp;
			count--;
			return val;
		}
		Node<T> tmp = head.next;
		Node<T> prev = head;
		while(tmp.next!=null){
			if(tmp.data.equals(data)){
				T val = (T) tmp.data;
				prev.next = tmp.next;
				tmp.next = null;
				count--;
				return val;
			}
			prev=tmp;
			tmp=tmp.next;
		}
		return null;
	}
	public int size(){
		return count;
	}
	@Override
	public String toString() {
		Node<T> s = head;
		StringBuffer sb = new StringBuffer();
		while(s!=null){
			sb.append(" "+ s.data + ",");
			s=s.next;
		}
		sb.deleteCharAt(sb.lastIndexOf(","));
		return "MyLinkedList [" + sb.toString() + "]";
	}
	
	
}

public class LinkedListExample {

	public static void main(String[] args) {

		MyLinkedList<String> s = new MyLinkedList<>();
		s.add("Java");
		System.out.println(s);
		s.addFirst("Spring");
		System.out.println(s);
		
		s.addLast("Hibernate");
		System.out.println(s);
		
		s.insert(2, "Ajax");
		System.out.println(s);
		
		String val = s.remove("Java");
		System.out.println("Item deleted :" + val);
		System.out.println(s);
		System.out.println("size of linked list is : " + s.size());
		
		MyLinkedList<Integer> intList = new MyLinkedList<>();
		intList.add(10);
		intList.add(20);
		System.out.println(intList);
		intList.addFirst(5);
		intList.addLast(25);
		System.out.println(intList);
		intList.insert(3, 30);
		System.out.println(intList);
		intList.remove(30);
		System.out.println(intList);
		System.out.println("size of linked list is: " + intList.size());
	}

}
