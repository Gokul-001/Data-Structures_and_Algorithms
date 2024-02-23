package source;

public class oops {

	public static void main(String[] args) {
		// create objects
		Car car1=new Car(100,"BMW","Petrol");
		Car car2=new Car(101,"Petrol");
		Car car3=new Car(102,"Honda","Diesel");

		// Array of Objects 	
		Car[] carList = {car1,car2,car3};
		
		for (Car i :carList)
		{
			i.display();
		}
		
	
	
	
	}

}
/*
	Order to be followed :
	
	1. car : 
	
		attributes 
		constructor
			overloading constructor (same name + different arguments)
		array of objects  Car[] carList = {car1,car2,car3} 
		Method
	
	 
}*/