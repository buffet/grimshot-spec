%define commit c6f601bc76b487b29bfa264a259e15d2ff9f3d65

Name:           grimshot
Version:        20230824
Release:        %{autorelease}
Summary:        A helper for screenshots within sway

License:        MIT
URL:            https://github.com/OctopusET/sway-contrib
Source0:        https://github.com/OctopusET/sway-contrib/archive/%{commit}.tar.gz

BuildArch:      noarch
Requires:       grim jq libnotify slurp wl-clipboard

%description
Grimshot is an easy-to-use screenshot utility for sway. It provides a
convenient interface over grim, slurp and jq, and supports storing the
screenshot either directly to the clipboard using wl-copy or to a file.

%prep
%setup -q -n sway-contrib-%{commit}


%build


%install
install -Dm 755 grimshot %{buildroot}/%{_bindir}/grimshot
install -Dm 644 grimshot.1 %{buildroot}/%{_mandir}/man1/grimshot.1


%files
%{_bindir}/grimshot
%{_mandir}/man1/grimshot.1.*

%license LICENSE
%doc README.md


%changelog
* Sat Aug 26 2023 buffet <niclas@countingsort.com>
- Init at 20230824
