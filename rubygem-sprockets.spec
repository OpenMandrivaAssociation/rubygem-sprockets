%define gemname sprockets
Summary:	Sprockets is a Rack-based asset packaging system
Name:		rubygem-%{gemname}
Version:	2.3.0
Release:	%mkrel 2
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{gemname}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
Provides:       rubygem(%{gemname}) = %{version}

%description
Sprockets is a Rack-based asset packaging system that concatenates 
and serves JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{bindir}/sprockets
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{gemdir}/doc/%{gemname}-%{version}
