# Day 16

## Objectives

- Continuing with webservices

## Resources

- Mostly: <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-define-a-wcf-service-contract>
- <https://docs.microsoft.com/en-us/dotnet/framework/wcf/bindings-overview>
- <https://www.tutorialspoint.com/wcf/> (Look into iis hosting etc)
- Make sure you configure the client and that you split the solution so that you can run the host and the client seperatly.

### Setup

- vs c# project file, with the necessary files.

### Suggested plan for tomorrow

- Writing xml files
  - <https://csharp.net-tutorials.com/xml/writing-xml-with-the-xmlwriter-class/>
- Do some more stuff with wcf
  - composite types to service operations
- Do something with c# attributes
- Cover a few design patterns: Like the proxy pattern (This might not relate, <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-create-a-wcf-client> but check it out (The proxy section that is (Svcutil.exe section)))
- Read up on how to use the Svcutil.exe tool (To create the source and config file)
- wcf service configuration editor (Look at how this tool functions as well. Under tools vs)
- Cover the 'See Also' section under: <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-use-a-wcf-client>

### Random Notes

Use the following command to create the proxy class as well as the config file
This is very important for creating service contracts (basically map the service so that you can use it correctly - TODO, learn how to use this without the service util)

```cmd
svcutil.exe /language:cs /out:generatedProxy.cs /config:app.config http://localhost:8000/ServiceModelSamples/service
```