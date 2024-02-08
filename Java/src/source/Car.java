package source;

class Car {
	
	//attributes
	int number;
	String name;
	String fuelType;
	
	// Constructor 
	Car(int num,String name,String type)
	{
		this.number =num;
		this.name=name;
		this.fuelType =type;
	}
	// over-loading constructors
	Car(int num,String fuel)
	{
		this.number= num;
		this.fuelType =fuel;
	}
	
	//Method
	void display()
	{
		System.out.println("Car-number: " +this.number+"| name: "+this.name+"| FuelType: "+this.fuelType);
	}
}