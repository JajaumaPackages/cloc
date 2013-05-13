Name:           cloc
Version:        1.58
Release:        3%{?dist}
Summary:        Count lines of code

Group:          Development/Tools
License:        GPLv2 and Artistic
URL:            http://cloc.sourceforge.net/

Source0:         http://downloads.sourceforge.net/project/%{name}/%{name}/v%{version}/cloc-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl(Pod::Checker)
Requires:       perl
Requires:       perl(Regexp::Common)
Requires:       perl(Algorithm::Diff)
# Stop trying to find the optional Win32::File dep.
%filter_from_requires /perl(Win32::File)/d;
%{?perl_default_filter}

%description
A tool to count lines of code in various languages from a given directory.

%prep
%setup -q -c

%build

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
/usr/share/man/man1/%{name}.1.*

%changelog
* Mon May 13 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-3
- Refer to pod2man BR by path, the package name varies.

* Mon May 13 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-2
- Use the tarball release instead.
- Fix license field.

* Mon May 13 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-1
- Latest upstream release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-5
- Remove the %clean section altogether.

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-4
- Remove specfile actions that are no longer needed for post-EL5.

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-3
- Let rpmbuild compress the manpage automatically.

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-2
- Include documentation generated from a pod file.

* Fri May 25 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-1
- Initial build.
