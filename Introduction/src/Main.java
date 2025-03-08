public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        //declare unchangeable variables keyword 'final'
        final int myNum = 15;
        //myNum = 20;  // will generate an error: cannot assign a value to a final variable
        System.out.println(myNum);
        //assign the same value to multiple variables
        int x, y, z;
        x = y = z = 50;
        System.out.println(x + y + z);

        // Student data
        String studentName = "John Doe";
        int studentID = 15;
        int studentAge = 23;
        float studentFee = 75.25f;
        char studentGrade = 'B';

        // Print variables
        System.out.println("Student name: " + studentName);
        System.out.println("Student id: " + studentID);
        System.out.println("Student age: " + studentAge);
        System.out.println("Student fee: " + studentFee);
        System.out.println("Student grade: " + studentGrade);

        // add 'f' at the end of a float number, 'L' for long and 'd' for double
        float myNum1 = 5.75f;
        System.out.println(myNum);
        double myNum2 = 19.99d;
        System.out.println(myNum2);
        double myNum3 = 19.99d;
        System.out.println(myNum3);
        long myNum4 = 15000000000L;
        System.out.println(myNum4);
        // u can enter the ascii value of a character in char
        char myVar1 = 65, myVar2 = 66, myVar3 = 67, myVar4 = 97;
        System.out.println(myVar1);
        System.out.println(myVar2);
        System.out.println(myVar3);
        System.out.println(myVar4);

        //casting
        //widening casting
        int myInt = 9;
        double myDouble = myInt; // Automatic casting: int to double

        System.out.println(myInt);      // Outputs 9
        System.out.println(myDouble);   // Outputs 9.0
        //narrowing casting
        double myDouble2 = 9.78d;
        int myInt2 = (int) myDouble2; // Manual casting: double to int

        System.out.println(myDouble2);   // Outputs 9.78
        System.out.println(myInt2);      // Outputs 9

        // incrementation
        int  i = 10;
        ++i;
        System.out.println(i);

        //String manipulation
        String txt = "Hello World";
        System.out.println(txt.toUpperCase());
        System.out.println(txt.toLowerCase());
        //get string length
        String txt1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.println("The length of the txt string is: " + txt1.length());
        //returns the index (the position) of the first occurrence of a specified text in a string
        String txt2 = "Please locate where 'locate' occurs!";
        System.out.println(txt2.indexOf("locate"));
        //the concat() method to concatenate two strings
        String firstName = "John ";
        String lastName = "Doe";
        System.out.println(firstName.concat(lastName));
        //Special Characters in strings
        String txt3 = "We are the so-called \"Vikings\" from the north.";
        System.out.println(txt3);
        String txt4 = "The character \\ is called backslash.";
        System.out.println(txt4);


    }
}