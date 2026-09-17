FROM mcr.microsoft.com/dotnet/sdk:10.0-alpine AS builder

RUN apk add --no-cache git

WORKDIR /src
RUN git clone --depth 1 https://github.com/TechnitiumSoftware/TechnitiumLibrary.git
RUN git clone --depth 1 https://github.com/TechnitiumSoftware/DnsServer.git

# DnsServer references sibling TechnitiumLibrary/bin/*.dll.
# Skip Windows-only projects (e.g. Net.Firewall) that fail on Alpine.
WORKDIR /src/TechnitiumLibrary
RUN dotnet build TechnitiumLibrary/TechnitiumLibrary.csproj -c Release \
 && dotnet build TechnitiumLibrary.ByteTree/TechnitiumLibrary.ByteTree.csproj -c Release \
 && dotnet build TechnitiumLibrary.IO/TechnitiumLibrary.IO.csproj -c Release \
 && dotnet build TechnitiumLibrary.Net/TechnitiumLibrary.Net.csproj -c Release \
 && dotnet build TechnitiumLibrary.Security.OTP/TechnitiumLibrary.Security.OTP.csproj -c Release

WORKDIR /src/DnsServer
RUN dotnet publish DnsServerApp/DnsServerApp.csproj -c Release -o /publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0-alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /publish /DnsServer
WORKDIR /DnsServer

ENTRYPOINT ["dotnet", "DnsServerApp.dll"]
