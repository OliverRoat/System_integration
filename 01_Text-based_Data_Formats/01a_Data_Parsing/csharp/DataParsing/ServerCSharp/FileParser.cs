using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Xml.Linq;
using CsvHelper;
using Newtonsoft.Json;
using YamlDotNet.Serialization;

public static class FileParser
{
    public static List<Dictionary<string, string>> ParseCsv(string filePath)
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

    public static Dictionary<string, object> ParseJson(string filePath)
    {
        var json = File.ReadAllText(filePath);
        var jsonObject = JsonConvert.DeserializeObject<Dictionary<string, object>>(json);

        // Convert hobbies to a list of strings
        if (jsonObject.ContainsKey("hobbies") && jsonObject["hobbies"] is Newtonsoft.Json.Linq.JArray hobbiesArray)
        {
            jsonObject["hobbies"] = hobbiesArray.ToObject<List<string>>();
        }

        return jsonObject;
    }

    public static dynamic ParseYaml(string filePath)
    {
        var yaml = File.ReadAllText(filePath);
        var deserializer = new Deserializer();
        return deserializer.Deserialize<dynamic>(yaml) ?? new object();
    }

    public static Dictionary<string, object> ParseXml(string filePath)
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

    public static string ParseTxt(string filePath)
    {
        return File.ReadAllText(filePath);
    }
}