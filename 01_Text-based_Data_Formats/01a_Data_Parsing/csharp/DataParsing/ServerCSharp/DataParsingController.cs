using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.IO;
using YamlDotNet.Serialization;
using System.Net.Http;
using System.Threading.Tasks;

namespace DataParsingApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class DataParsingController : ControllerBase
    {
        private readonly string baseDirectory = Directory.GetCurrentDirectory();
        private readonly HttpClient httpClient = new HttpClient();
        private readonly string serverBUrl = "http://localhost:8000";

        [HttpGet("csv")]
        public IActionResult GetCsv()
        {
            var filePath = Path.Combine(baseDirectory, "meC.csv");
            var data = FileParser.ParseCsv(filePath);
            return Ok(data);
        }

        [HttpGet("json")]
        public IActionResult GetJson()
        {
            var filePath = Path.Combine(baseDirectory, "meC.json");
            var data = FileParser.ParseJson(filePath);
            return Ok(data);
        }

        [HttpGet("yaml")]
        public IActionResult GetYaml()
        {
            var filePath = Path.Combine(baseDirectory, "meC.yaml");
            var data = FileParser.ParseYaml(filePath);
            return Ok(data);
        }

        [HttpGet("xml")]
        public IActionResult GetXml()
        {
            var filePath = Path.Combine(baseDirectory, "meC.xml");
            var data = FileParser.ParseXml(filePath);
            return Ok(data);
        }

        [HttpGet("txt")]
        public IActionResult GetTxt()
        {
            var filePath = Path.Combine(baseDirectory, "meC.txt");
            var data = FileParser.ParseTxt(filePath);
            return Ok(data);
        }

        [HttpGet("proxy/{fileType}")]
        public async Task<IActionResult> ProxyToServerB(string fileType)
        {
            var response = await httpClient.GetAsync($"{serverBUrl}/{fileType}");
            var content = await response.Content.ReadAsStringAsync();
            return Content(content, response.Content.Headers.ContentType.ToString());
        }
    }
}