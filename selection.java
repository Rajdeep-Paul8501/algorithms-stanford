//O(n)random selection algorithm(^.^)

import java.util.Random;

class alg3_rselect{
	public static int [] swap(int []arr,int a,int b){
		int temp=arr[a];
		arr[a]=arr[b];
		arr[b]=temp;
		return arr;
	}

	public static int  partition(int []arr, int l,int h){
		Random rand=new Random();
		int rand_pivot_index=(rand.nextInt(h-l+1)+l);
		int i=l-1;int pivot=arr[rand_pivot_index];
		arr=swap(arr,rand_pivot_index,h);
		for(int j=l;j<h;j++){
			if(arr[j]<pivot){
				i++;
				arr=swap(arr,j,i);
			}

		}
		arr=swap(arr,h,i+1);
		int partition_index=i+1;
		return(partition_index);		


	}
	public static int find(int[]arr,int l,int h,int i){
		
		while(l<=h){
		if(l==h)return arr[l];
		
		int partition_index=partition(arr,l,h);
		if(partition_index==i)
			return arr[partition_index];
		else if(partition_index<i){
			l=partition_index+1;
			i=i-partition_index;

	}
		else if(partition_index>i){
			h=partition_index-1;
		}
	}
	return -1;



	
}
public static void main(String[] args){
	int[] arr={32,4,2,1,54,68,56,31};
	System.out.println(find(arr,0,arr.length-1,6));
}


}
