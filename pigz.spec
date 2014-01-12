Name:			pigz
Version:		2.3
Release:		5
Summary:		Parallel implementation of gzip
Group:			Archiving/Compression
License:		zlib
URL:			http://www.zlib.net/pigz/
Source0:		http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:		zlib-devel
Patch1:			ldflags.patch

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when compressing data.

%prep
%setup -q
%apply_patches

%build
%make CC="%{__cc}" AR="%{__ar}" RANLIB="%{__ranlib}"  CFLAGS="%{optflags} -O3" LDFLAGS="%{ldflags} -lm"

%install
install -p -m755 pigz -D %{buildroot}%{_bindir}/pigz
install -p -m755 unpigz -D %{buildroot}%{_bindir}/unpigz
install -p -m644 pigz.1 -D %{buildroot}%{_datadir}/man/man1/pigz.1

%files
%doc pigz.pdf README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_datadir}/man/man1/pigz.*


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.2.4-1
+ Revision: 787074
- version update 2.2.4

* Fri Aug 12 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.1.6-3
+ Revision: 694064
- fix group
- imported package pigz

