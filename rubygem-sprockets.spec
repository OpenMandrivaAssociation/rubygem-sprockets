%define __noautoreq '!=|1.3.0'

%define gemname sprockets
Summary:	Sprockets is a Rack-based asset packaging system
Name:		rubygem-%{gemname}
Version:	2.12.0
Release:	8
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
Sprockets is a Rack-based asset packaging system that concatenates 
and serves JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%prep
%setup -c

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%defattr(-,root,root)
%{_bindir}/sprockets
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.0-4
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 2.3.0-3
+ Revision: 769822
- Fix file list

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 2.3.0-2
+ Revision: 769775
- Manual provides

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 2.3.0-1
+ Revision: 769722
- First mdv package
- Created package structure for 'rubygem-sprockets'.

