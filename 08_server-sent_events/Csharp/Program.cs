var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

var app = builder.Build();

app.UseHttpsRedirection();
app.UseStaticFiles(); // Serve static files
app.UseAuthorization();
app.MapControllers();

app.Run();