using System;
using System.Text;

class EncodingDecodingExample
{
    static void Main(string[] args)
    {
        string originalMessage = "hallå";

        // Encode the string into bytes
        byte[] encodedMessage = Encoding.UTF8.GetBytes(originalMessage);

        // Decode the bytes back into a string
        string decodedMessage = Encoding.UTF8.GetString(encodedMessage);

        // Print the encoded bytes and the decoded string
        Console.WriteLine("Encoded message (bytes): " + BitConverter.ToString(encodedMessage));
        Console.WriteLine("Decoded message: " + decodedMessage);
    }
}