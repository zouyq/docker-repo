FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS builder

RUN apk add git

RUN git clone https://github.com/TechnitiumSoftware/TechnitiumLibrary.git
RUN git clone https://github.com/TechnitiumSoftware/DnsServer.git

RUN dotnet build TechnitiumLibrary/TechnitiumLibrary.ByteTree/TechnitiumLibrary.ByteTree.csproj -c Release
RUN dotnet build TechnitiumLibrary/TechnitiumLibrary.Net/TechnitiumLibrary.Net.csproj -c Release

RUN dotnet publish DnsServer/DnsServerApp/DnsServerApp.csproj -c Release

FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /DnsServer/DnsServerApp/bin/Release/publish /DnsServer
WORKDIR /DnsServer

ENTRYPOINT ["dotnet", "DnsServerApp.dll"]