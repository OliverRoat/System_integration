using System;
using System.Collections.Generic;
using System.IO;
using System.Xml.Linq;
using Newtonsoft.Json;
using YamlDotNet.Serialization;
using CsvHelper;
using System.Globalization;

class Program
{
    static void Main()
    {
        var csvData = ParseCsv("meC.csv");
        var jsonData = ParseJson("meC.json");
        var yamlData = ParseYaml("meC.yaml");
        var xmlData = ParseXml("meC.xml");
        var txtData = ParseTxt("meC.txt");

        Console.WriteLine("CSV Data:");
        PrintCsvData(csvData);
        Console.WriteLine("JSON Data: " + JsonConvert.SerializeObject(jsonData, Formatting.Indented));
        Console.WriteLine("YAML Data: " + JsonConvert.SerializeObject(yamlData, Formatting.Indented));
        Console.WriteLine("XML Data: " + JsonConvert.SerializeObject(xmlData, Formatting.Indented));
        Console.WriteLine("TXT Data: " + txtData);
    }

    static List<Dictionary<string, string>> ParseCsv(string filePath)
    {
        using (var reader = new StreamReader(filePath))
        using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
        {
            var records = new List<Dictionary<string, string>>();
            csv.Read();
            csv.ReadHeader();
            while (csv.Read())
            {
                var record = new Dictionary<string, string>();
                foreach (var header in csv.HeaderRecord)
                {
                    record[header] = csv.GetField(header);
                }
                records.Add(record);
            }
            return records;
        }
    }

    static void PrintCsvData(List<Dictionary<string, string>> csvData)
    {
        foreach (var row in csvData)
        {
            foreach (var kvp in row)
            {
                Console.Write($"{kvp.Key}: {kvp.Value}, ");
            }
            Console.WriteLine();
        }
    }

    static dynamic ParseJson(string filePath)
    {
        var json = File.ReadAllText(filePath);
        return JsonConvert.DeserializeObject(json);
    }

    static dynamic ParseYaml(string filePath)
    {
        var yaml = File.ReadAllText(filePath);
        var deserializer = new Deserializer();
        return deserializer.Deserialize<dynamic>(yaml) ?? new object();
    }

    static Dictionary<string, object> ParseXml(string filePath)
    {
        var xml = XDocument.Load(filePath);
        var root = xml.Root;
        var data = new Dictionary<string, object>();

        void ParseElement(XElement element, Dictionary<string, object> dict)
        {
            if (element == null) return;

            foreach (var child in element.Elements())
            {
                if (child.HasElements)
                {
                    var childDict = new Dictionary<string, object>();
                    ParseElement(child, childDict);
                    dict[child.Name.LocalName] = childDict;
                }
                else
                {
                    if (dict.ContainsKey(child.Name.LocalName))
                    {
                        if (dict[child.Name.LocalName] is List<string> list)
                        {
                            list.Add(child.Value ?? string.Empty);
                        }
                        else
                        {
                            dict[child.Name.LocalName] = new List<string> { (string)dict[child.Name.LocalName], child.Value ?? string.Empty };
                        }
                    }
                    else
                    {
                        dict[child.Name.LocalName] = child.Value ?? string.Empty;
                    }
                }
            }
        }

        if (root != null)
        {
            ParseElement(root, data);
        }
        return data;
    }

    static string ParseTxt(string filePath)
    {
        return File.ReadAllText(filePath);
    }
}