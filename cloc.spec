Name:           cloc
Version:        1.56
Release:        7%{?dist}
Summary:        Count lines of code

Group:          Development/Tools
License:        GPLv2+
URL:            http://cloc.sourceforge.net/

Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/v%{version}/%{name}-%{version}.pl
Source1:        http://downloads.sourceforge.net/project/%{name}/%{name}/v%{version}/%{name}.1.pod
Source2:        http://downloads.sourceforge.net/project/%{name}/%{name}/v%{version}/release-%{version}.txt
BuildArch:      noarch
BuildRequires:  /usr/bin/pod2man
Requires:       perl
Requires:       perl(Regexp::Common)
Requires:       perl(Algorithm::Diff)
# Stop trying to find the optional Win32::File dep.
%filter_from_requires /perl(Win32::File)/d;
%{?perl_default_filter}

%description
A tool to count lines of code in various languages from a given directory.

%prep

%build
pod2man %{SOURCE1} > %{name}.1
cp %{SOURCE2} release-%{version}.txt

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc release-%{version}.txt
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}


%changelog
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
