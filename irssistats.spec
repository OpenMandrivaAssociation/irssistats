%define	name	irssistats
%define	version	0.75
%define release	3

Name:		%name
Summary:	This tool generates HTML IRC stats based on irssi logs
Version:	%version
Release:	%release
Url:		https://royale.zerezo.com/irssistats/
Source:		http://royale.zerezo.com/%{name}/%{name}-%{version}.tar.gz
Group:		Networking/IRC
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-buildroot

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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.75-2mdv2011.0
+ Revision: 612416
- the mass rebuild of 2010.1 packages

* Mon Feb 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.75-1mdv2010.1
+ Revision: 506083
- Clean spec file
- Update to 0.75

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.73-4mdv2010.0
+ Revision: 429572
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.73-3mdv2009.0
+ Revision: 247270
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.73-1mdv2008.1
+ Revision: 127175
- kill re-definition of %%buildroot on Pixel's request

  + Nicolas Vigier <nvigier@mandriva.com>
    - new version
    - Import irssistats



* Tue Feb 08 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.71-1mdk
- from Antoine Jacquet <royale@zerezo.com> : 
	- Fixed group in the spec file

* Mon Feb 07 2005 Antoine Jacquet <royale@zerezo.com> 
- Added spec file
