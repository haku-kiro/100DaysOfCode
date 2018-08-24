# Day 19

## Objectives

- Working with dynamic types and unmanaged code.

## Resources

- Using microsoft 483 Programming in c# textbook.

### Setup

- Create a c# proj to demonstrate the examples.

### Suggested plan for tomorrow

- Writing xml files
  - <https://csharp.net-tutorials.com/xml/writing-xml-with-the-xmlwriter-class/>
- Do some more stuff with wcf
  - composite types to service operations
- Cover a few design patterns: Like the proxy pattern (This might not relate, <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-create-a-wcf-client> but check it out (The proxy section that is (Svcutil.exe section)))
- Read up on how to use the Svcutil.exe tool (To create the source and config file)
- wcf service configuration editor (Look at how this tool functions as well. Under tools vs)
- Cover the 'See Also' section under: <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-use-a-wcf-client>
- Do some work with async and await, or some threading - parallel tasks etc
- Do something with reflection

### Random Notes

- Also messed around with findstr (like grep, but for windows (Still prefer grep :D )).

(Note the following Inital command is powershell)
For example, the following finds all the services that have the word wind in them and are running:

```powershell
Get-Service * | findstr Running | findstr -ir \wind
```

(This would be a cmd specific example)
And this example, finds all the tasks that are running that have the char `s` in them:

```cmd
tasklist | findstr -ir \s
```

Neat ! :)