%define name irssistats
%define version 0.73
%define release %mkrel 3

Name: %name
Summary: This tool generates HTML IRC stats based on irssi logs
Version: %version
Release: %release
Url: http://royale.zerezo.com/irssistats/
Source: http://royale.zerezo.com/%{name}/%{name}-%{version}.tar.gz
Group: Networking/IRC
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
irssistats is a tool that make HTML stats from irssi logfiles.
The statistics generated display many useful and funny informations 
about the channel.

%prep 
%setup -q

%build 
%make

%install 
make install PRE=$RPM_BUILD_ROOT/usr

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%doc COPYING README
%{_bindir}/irssistats
%{_mandir}/man1/*
%_datadir/%name
