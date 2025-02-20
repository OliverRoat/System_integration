using System;

class DateTimeExample
{
    static void Main(string[] args)
    {
        // Get the current date and time
        DateTime now = DateTime.Now;

        // Print the current date and time
        Console.WriteLine("Current date and time: " + now);

        // Print the current date
        Console.WriteLine("Current date: " + now.ToShortDateString());

        // Print the current time
        Console.WriteLine("Current time: " + now.ToShortTimeString());

        // Print the current date and time in a custom format
        Console.WriteLine("Custom format: " + now.ToString("yyyy-MM-dd HH:mm:ss"));
    }
}