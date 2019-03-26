Summary:	Parallel implementation of gzip
Name:		pigz
Version:	2.4
Release:	7
Group:		Archiving/Compression
License:	zlib
Url:		http://www.zlib.net/pigz/
Source0:	http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pigz-2.4-Makefile.patch
BuildRequires:	pkgconfig(zlib)
# (tpg) by default use pigz as system-wide gzip
Conflicts:	gzip < 1.9-3

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when compressing data.

%prep
%autosetup -p1

%build
%make_build CC="%{__cc}" AR="%{__ar}" RANLIB="%{__ranlib}" CFLAGS="%{optflags} -O3" LDFLAGS="%{ldflags} -lz -lm"

%install
install -p -m755 pigz -D %{buildroot}/bin/pigz
install -p -m755 unpigz -D %{buildroot}/bin/unpigz
install -p -m644 pigz.1 -D %{buildroot}%{_datadir}/man/man1/pigz.1

# (tpg) install replacement files to use pigz instead of gzip
ln -sf /bin/pigz %{buildroot}/bin/gzip
ln -sf /bin/unpigz %{buildroot}/bin/gunzip
mkdir -p %{buildroot}%{_bindir}
ln -sf /bin/unpigz %{buildroot}%{_bindir}/gunzip

%files
%doc README
/bin/pigz
/bin/unpigz
/bin/gzip
/bin/gunzip
%{_bindir}/gunzip
%{_mandir}/man1/pigz.*
