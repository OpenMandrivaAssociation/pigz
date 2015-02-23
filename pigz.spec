Summary:	Parallel implementation of gzip
Name:		pigz
Version:	2.3.3
Release:	1
Group:		Archiving/Compression
License:	zlib
Url:		http://www.zlib.net/pigz/
Source0:	http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(zlib)

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
%{_mandir}/man1/pigz.*

