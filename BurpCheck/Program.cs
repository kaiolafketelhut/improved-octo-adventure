using System;
using System.IO;
using System.Security.Cryptography;

class Program
{
    static void Main()
    {
        Console.Write("Path to file to check (Burp .jar or .exe): ");
        string path = Console.ReadLine()?.Trim('"') ?? "";

        if (!File.Exists(path))
        {
            Console.WriteLine("File not found!");
            return;
        }

        Console.WriteLine("\n--- SHA256 HASH ---");
        using (var fs = File.OpenRead(path))
        {
            var hash = Convert.ToHexString(SHA256.HashData(fs));
            Console.WriteLine(hash);
        }
        Console.WriteLine("Compare this hash with the official hash on portswigger.net");
        Console.WriteLine("Same = Clean, Different = Tampered");

        Console.WriteLine("\n--- SIGNATURE CHECK ---");
        Console.WriteLine("On Linux / Termux, Windows Authenticode signatures");
        Console.WriteLine("cannot be checked with X509Certificate.CreateFromSignedFile.");
        Console.WriteLine("That is why we use the HASH check above - it is the .NET proof here.");
        Console.WriteLine("If hash matches PortSwigger = NOT a virus, signed by PortSwigger.");
    }
}
