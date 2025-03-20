using Microsoft.AspNetCore.Mvc;
using System;
using System.Threading.Tasks;

namespace ServerSentEvents.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class SseController : ControllerBase
    {
        [HttpGet("synchronizetime")]
        public async Task SynchronizeTime()
        {
            Response.Headers.Add("Content-Type", "text/event-stream");

            while (!HttpContext.RequestAborted.IsCancellationRequested)
            {
                var timeStr = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
                await Response.WriteAsync($"data: {timeStr}\n\n");
                await Response.Body.FlushAsync();
                await Task.Delay(1000);
            }
        }
    }
}